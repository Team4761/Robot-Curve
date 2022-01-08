#This ENTIRE script is almost DIRECLY based off an identical project I made in desmos!
#Look through it here! https://www.desmos.com/calculator/o7vr5z7o8y

#NOTE: t would be the variable that desmos would use to graph it. 
#So we're assuming that a, b, and t are the same across the whole function

#TODO: Incorporate stringing beziers together!

from vector import *
from ray import *

#first bit, make the bezier curve function
#a: first point. b: second point. t: trajectory (0 = start pt, 1 = endpt)
def bezier(a, b, t):

	#no glitches for you!
	if t > 1 or t < 0:
		raise Exception("Error thrown, t cannot be less that 0 or greater than 1")
	
	#define the points
	pt1 = a.ori
	pt2 = a.ori + a.dir
	pt3 = b.ori - b.dir
	pt4 = b.ori

	#Bezier Curve Iteration 1
	c1_1 = (pt2 * t) - (pt1 * (1 - t))
	c1_2 = (pt3 * t) - (pt2 * (1 - t))
	c1_3 = (pt4 * t) - (pt2 * (1 - t))

	#Bezier Curve Iteration 2
	c2_1 = (c1_2 * t) - (c1_1 * (1 - t))
	c2_2 = (c1_3 * t) - (c1_2 * (1 - t))

	#Bezier Curve Iteration 3 (and final iteration!)
	curve = (c2_2 * t) - (c2_1 * (1 - t))
	
	return curve

def morph_bezier(a, b, t, offset, height):
	
	# using a secant line instead of a tangent line to save us time and whiteboard space
	ep = 0.00001
	curve_1 = bezier(a,b,t)
	curve_2 = bezier(a,b,t + ep)

	# derivative
	d_curve = (curve_1 - curve_2) / (ep)
	
	# normal line
	n_curve = rotate90(d_curve)

	return (offset * normalize(n_curve)) + bezier(a,b,height)

#left and right motor paths, as a vec2
# TODO: double check my negatives!
def get_right_motor_path(a, b, t, robot_width):

	o = - (robot_width / 2)
	return morph_bezier(a,b, o, 1, t)

def get_left_motor_path(a, b, t, robot_width):

	o = (robot_width / 2)
	return morph_bezier(a,b, o, 1, t)

#left and right motor lengths. Now finally returns the value that we need as a float
def get_right_motor_length(a,b,t,robot_width):
	return 1

def get_left_motor_length(a,b,t,robot_width):
	return 1

def debug():
	p = vec2(5,2)
	pt = point(vec2(0,0),vec2(1,1))

	q = p * 5

	print(pt)

	print(p)


#the actual main function
def __main__():
	debug()

__main__()