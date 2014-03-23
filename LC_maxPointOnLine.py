'''
Given n points on a 2d plane, find the maximum number of points that lie on the same straight line

Created on Dec 11, 2013

@author: Songfan
'''
import math

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        
    def __str__(self):
        return '('+str(self.x)+','+str(self.y)+')'
        
def computeLineParas(p1,p2):
    if p1.x == p2.x:
        b = 0
        a = 1
        c = -p1.x
    else:
        b = 1
        a = (p2.y-p1.y)/(p1.x-p2.x)
        c = -a*p1.x - b*p1.y
    return a,b,c


def maxPointOnLine(points):
    assert(isinstance(points,list)),'error'
    ptsSize = len(points)
    if ptsSize<2:
        return False
    h = {}
    for i in range(ptsSize):
        for j in range(i+1,ptsSize):
            a,b,c = computeLineParas(points[i], points[j])
            if not h.has_key((a,b,c)):
                h[(a,b,c)] = [points[i],points[j]]
            else:
                if points[i] not in h[(a,b,c)]:
                    h[(a,b,c)].append(points[i])
                if points[j] not in h[(a,b,c)]:
                    h[(a,b,c)].append(points[j])
    v = [len(e) for e in h.values()]
    return max(v)


def maxPointOnLineHough(points):
    ptsSize = len(pts)
    if ptsSize<2:
        return False
    h = {}
    for p in pts:
        for a in range(0,361):
            r = p.x*math.cos(math.radians(a))+p.y*math.sin(math.radians(a))
            r = round(r*10)/10 # adjust precision
            h[(a,r)] = h.get((a,r),0)+1
    vs = h.values()
    return max(vs)


pts = []
pts.append(Point(1,0))
pts.append(Point(1,1))
pts.append(Point(2,0))
pts.append(Point(2,1))
pts.append(Point(2,2))
print maxPointOnLine(pts)
print maxPointOnLineHough(pts)

pts.append(Point(0,0))
pts.append(Point(3,0))
print maxPointOnLine(pts)
print maxPointOnLineHough(pts)