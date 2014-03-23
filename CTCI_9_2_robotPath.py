'''
robot path using 'Down' and 'Right' to reach (X,Y) from (0,0). There could be 'off-limit' points

Created on Dec 2, 2013

@author: Songfan
'''

def _path(destination, limits,h):
    x = destination[0]
    y = destination[1]
    if (x,y) in limits or (x==0 and y==0): return ''
    if y==0: return ['R'*x] # handle multiple move right
    if x==0: return ['D'*y]
    if (x,y) in h.keys(): return h[(x,y)]
    if (x-1,y) not in limits:
        # work the way backwards, find the left position if it is off limit
        prevPath = _path((x-1,y),limits,h)
        h[(x,y)] = [p+'R' for p in prevPath]
    if (x,y-1) not in limits:
        prevPath = _path((x,y-1),limits,h)
        if (x,y) in h.keys():
            # there could be a path already from (x-1,y). However, there is no path from (x-1,y) when we firt process it. Therefore, no need to check existance for (x-1,y) case 
            h[(x,y)].extend([p+'D' for p in prevPath])
        else:
            h[(x,y)] = [p+'D' for p in prevPath]
    return h[(x,y)]

def path(destination,limits):
    x = destination[0]
    y = destination[1]
    assert(x>=0 or y>=0),"input error: desination must be non-negative"
    return _path(destination,limits,{})

des = (3,3)
limits = [(1,1),(2,2)]
print path(des,limits)