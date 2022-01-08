from vector import *

class point:

	#Note: DIR does not need to be normalized. Infact, it shouldn't!
	def __init__(self, ori, dir):
		self.ori = ori
		self.dir = dir

	def __str__(self):
		return "Ori: ( %s , %s ) , Dir: ( %s , %s )" % (self.ori.x, self.ori.y, self.dir.x, self.dir.y)


