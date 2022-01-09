# Looks eirely similar to shadertoy doesn't it?
import math

class vec2:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __str__(self):
        return "( %s , %s )" % (self.x, self.y)

    def __add__(self, o):
        if type(o) is vec2:
            return vec2(self.x + o.x, self.y + o.y)
        else:
            return vec2(self.x + o, self.y + o)

    def __sub__(self, o):
        if type(o) is vec2:
            return vec2(self.x - o.x, self.y - o.y)
        else:
            return vec2(self.x - o, self.y - o)

    def __mul__(self, o):
        if type(o) is vec2:
            return vec2(self.x * o.x, self.y * o.y)
        else:
            return vec2(self.x * o, self.y * o)

    def __truediv__(self, o):
        if type(o) is vec2:
            return vec2(self.x / o.x, self.y / o.y)
        else:
            return vec2(self.x / o, self.y / o)
    
    #operations with right side scalars
    def __radd__(self, o):
        if type(o) is vec2:
            return vec2(self.x + o.x, self.y + o.y)
        else:
            return vec2(self.x + o, self.y + o)

    def __rsub__(self, o):
        if type(o) is vec2:
            return vec2(o.x - self.x, o.y - self.y)
        else:
            return vec2(o - self.x, o - self.y)

    def __rmul__(self, o):
        if type(o) is vec2:
            return vec2(self.x * o.x, self.y * o.y)
        else:
            return vec2(self.x * o, self.y * o)

    def __rtruediv__(self, o):
        if type(o) is vec2:
            return vec2(o.x / self.x, o.y / self.y)
        else:
            return vec2(self.x / o, self.y / o)

# all the other vector functions that we'll need
def length(v):
    return math.sqrt(v.x*v.x + v.y*v.y);

def dot(v1, v2):
    dotx = v1.x * v2.x
    doty = v1.y * v2.y
    
    return dotx + doty
    
def normalize(v):
    l = length(v)
    
    return vec2(v.x/l,v.y/l)
    
def rotate90(v):
    return vec2(-v.y,v.x)

def sign(v):
    ret = vec2(0,0)

    #This code is in substitute for getting sign, because math.sign() nor math.abs() exist :(
    if v.x > 0: 
        ret.x = 1 
    elif v.x < 0: 
        ret.x = -1 
    else: 
        v.x = 0

    if v.y > 0: 
        ret.y = 1 
    elif v.y < 0: 
        ret.y = -1 
    else: 
        v.y = 0

    return ret

# Compares the two components
def min(v):
    if v.x < v.y:
        return v.x
    else:
        return v.y

def max(v):
    if v.x > v.y:
        return v.x
    else:
        return v.y