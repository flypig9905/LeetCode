'''
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Created on Jan 2, 2014

@author: Songfan
'''
''' algorithm: classic DP '''
def climbStairs(n):
    assert(isinstance(n,int) and n>0),'input error'
    return _cs(n, {})

def _cs(n, h):
    if n == 1: return 1
    if n == 2: return 2
    if n in h: return h[n]
    h[n] = _cs(n-1, h) + _cs(n-2, h)
    return h[n]

''' unittest '''
n = 3
print climbStairs(n)
n = 5
print climbStairs(n)
n = 10
print climbStairs(n)
n = 19
print climbStairs(n)