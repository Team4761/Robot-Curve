# Looks eirely similar to shadertoy doesn't it?

class vec2:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __str__(self):
        return "( %s , %s )" % (self.x, self.y)

    def __add__(self, o):
        return vec2(self.x + o.x, self.y + o.y)

    def __sub__(self, o):
        return vec2(self.x - o.x, self.y - o.y)

    def __mul__(self, o):
        return vec2(self.x * o.x, self.y * o.y)

    def __truediv__(self, o):
        return vec2(self.x / o.x, self.y / o.y)

    #operations with scalars
    def __add__(self, o):
        return vec2(self.x + o, self.y + o)

    def __sub__(self, o):
        return vec2(self.x - o, self.y - o)

    def __mul__(self, o):
        return vec2(self.x * o, self.y * o)

    def __truediv__(self, o):
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
