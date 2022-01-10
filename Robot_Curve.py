#This ENTIRE script is almost DIRECLY based off an identical project I made in desmos!
#Look through it here! https://www.desmos.com/calculator/o7vr5z7o8y

#NOTE: t would be the variable that desmos would use to graph it. 
#So we're assuming that a, b, and t are the same across the whole function

#TODO: Incorporate stringing beziers together!

from vector import *
from ray import *
from constants import *
import sys

#first bit, make the bezier curve function
#a: first point. b: second point. t: trajectory (0 = start pt, 1 = endpt)
def bezier(a, b, t):
	
	#define the points
	pt1 = a.ori
	pt2 = a.ori + a.dir
	pt3 = b.ori - b.dir
	pt4 = b.ori

	#Bezier Curve Iteration 1
	c1_1 = (pt2 * t) + (pt1 * (1 - t))
	c1_2 = (pt3 * t) + (pt2 * (1 - t))
	c1_3 = (pt4 * t) + (pt2 * (1 - t))

	#Bezier Curve Iteration 2
	c2_1 = (c1_2 * t) + (c1_1 * (1 - t))
	c2_2 = (c1_3 * t) + (c1_2 * (1 - t))

	#Bezier Curve Iteration 3 (and final iteration!)
	curve = (c2_2 * t) + (c2_1 * (1 - t))
	
	return curve

def morph_bezier(a, b, t, offset, height):
	
	# using a secant line instead of a tangent line to save us time and whiteboard space
	curve_1 = bezier(a,b,height)
	curve_2 = bezier(a,b,height + ep)

	# derivative
	d_curve = (curve_1 - curve_2) / (-ep)
	
	# normal line
	n_curve = rotate90(d_curve)

	ret = ( normalize(n_curve) * offset * t) + bezier(a,b,height)

	return ret

#left and right motor paths, as a vec2
def get_right_motor_path(a, b, t, robot_width):

	o = -(robot_width / 2.0)
	morph = morph_bezier(a,b, o, 1.0, t)
	return morph

def get_left_motor_path(a, b, t, robot_width):

	o = (robot_width / 2.0)
	morph = morph_bezier(a,b, o, 1.0, t)
	return morph


def get_motor_length(a,b,t,robot_width,motor_side):

	# one "piece" of the integral
	def f(a,b,t,robot_width,motor_side):

		path_1 = vec2(0,0)
		path_2 = vec2(0,0)

		#get path
		if motor_side == "right":
			path_1 = get_right_motor_path(a,b,t,robot_width)
			path_2 = get_right_motor_path(a,b,t+ep,robot_width)
		elif motor_side == "left":
			path_1 = get_left_motor_path(a,b,t,robot_width)
			path_2 = get_left_motor_path(a,b,t+ep,robot_width)
		else:
			raise Exception("Motor side %s does not exist" % motor_side)

		d_path = (path_1 - path_2) / (-ep)

		# center path derivative
		curve_1 = bezier(a,b,t)
		curve_2 = bezier(a,b,t+ep)

		d_curve = (curve_1 - curve_2) / (-ep)

		# get the sign of both
		s = min(sign(d_curve * d_path))

		# the sign shouldn't be 0.
		# the only time this is possible is if the vector is set up like (0,1)
		# d_curve is changing, but this is the one place where our sign check fails at
		if s == 0.0:
			s = 1.0

		#integration variable
		integrate = s * length(d_curve)
		return integrate

	v = 0.0
	v2 = 0.0
	for n in range(1,int_N+1):
		dt = (n-0.5)*(t/int_N)
		v += f(a,b,dt,robot_width,motor_side)
	v2 = (t/int_N)*v


	return v2

def get_left_motor_length(a,b,t,robot_width):
	return get_motor_length(a,b,t,robot_width,"left")

def get_right_motor_length(a,b,t,robot_width):
	return get_motor_length(a,b,t,robot_width,"right")

#the trajectory of one bezier curve
#omni-potent count variable
count = 5
def curve_trajectory(a,b,robot_width,outdir=None):
	
	# generate the list of set points
	t = []
	i = 1
	while( i <= count):
		t.append(i / count)
		i+=1

	#left and right lists
	l = []
	r = []

	for p in t:
		l.append(get_left_motor_length(a,b,p,robot_width))
		r.append(get_right_motor_length(a,b,p,robot_width))

	if outdir is None or outdir == "console":

		print("new bezier curve")
		o = 0
		while o < len(t):
			print("Setpoint:", t[o], "Left:", l[o], "Right:",r[o])
			o+=1

	elif outdir == "port":

		print("Currently cannot pass to a wifi port")

	else:

		outfile = open(outdir,'a')
		
		outfile.write("new bezier curve \n")
		o = 0
		while o < len(t):
			outfile.write(str(l[o]) + "," + str(r[o]) + "\n")
			o+=1
		outfile.close()


def debug_main():
	a = point(vec2(0,0),vec2(0.1,0.1))
	b = point(vec2(1,1),vec2(0.1,0.1))
	robot_width = 0.528

	curve_trajectory(a,b,robot_width)


#main
def __main__():

	dir = "null"
	outdir = "null"

	#get the function arguments
	if sys.argv[1] == "-fd":
		dir = sys.argv[2]

	try:
		if sys.argv[3] == "-out":
			outdir = sys.argv[4]
	except Exception as E:
		print("No out file. Printing to console...")
		outdir = "console"


	#open the file
	bezierfile = open(dir,'r')
	
	# get list of each line
	lines = bezierfile.readlines()

	#first line is robot width
	robot_width = float(lines[0].replace("\n",""))
	#rest of the lines are points
	points = lines[1:]

	prevpt = empty_point
	currpt = empty_point
	for point in points:
		#skips the first loop, where previous point is null
		#TODO: parse string into point
		if prevpt == empty_point:
			prevpt = parse_string(point)
			continue

		currpt = parse_string(point)
		curve_trajectory(prevpt, currpt, robot_width,outdir)
		prevpt = currpt

	
__main__()

