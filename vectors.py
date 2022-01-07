#Remaking all the stuff that'd I'd use for shadertoy and the desmos program

class vec2:

    x = 0
    y = 0
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __stir__(self):
        return "( %s , %s )" % (self.x, self.y)
    
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
    

