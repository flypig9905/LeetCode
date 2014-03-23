'''
CTCI 9-1
One child can hop 1,2,or 3 stairs on a n staircase. How many ways of hops is possible?

Created on Dec 2, 2013

@author: Songfan
'''
def hops(n,h):
    assert(n>0 and isinstance(n,int)),"Input Error: number of staircase should be positive integer"
    if n==1: return 1
    elif n==2: return 2
    elif n==3: return 3
    if n is h.keys():
        return h[n]
    else:
        h[n] = hops(n-3,h)+hops(n-2,h)+hops(n-1,h)
    return h[n]

def hops1(n):
    assert(n>0 and isinstance(n,int)),"Input Error: number of staircase should be positive integer"
    if n==1: return 1
    elif n==2: return 2
    elif n==3: return 3
    h = {}
    if n is h.keys():
        return h[n]
    else:
        h[n] = hops1(n-3)+hops1(n-2)+hops1(n-1)
    return h[n]

# n = 6
# print hops(n,{})
# 
# n = 10
# print hops(n,{})

n = 25
print hops(n,{})
print hops1(n)