from vector import *

class point:

	#Note: DIR does not need to be normalized. Infact, it shouldn't!
	def __init__(self, ori, dir):
		self.ori = ori
		self.dir = dir

	def __str__(self):
		return "Ori: ( %s , %s ) , Dir: ( %s , %s )" % (self.ori.x, self.ori.y, self.dir.x, self.dir.y)

empty_point = point(vec2(0,0),vec2(0,0))

def parse_string(pt):
	pt = pt.replace('(','')
	pt = pt.replace(')','')
	pt = pt.replace('\n','')
	pt = pt.replace(' ','')
	
	string_literal = pt.split(',')
	n = []
	for char_literal in string_literal:
		n.append(float(char_literal))

	ori = vec2(n[0],n[1])
	dir = vec2(n[2],n[3])
	ray = point(ori,dir)
	#print(ray)
	return ray
