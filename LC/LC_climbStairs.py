'''
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Created on Jan 2, 2014

@author: Songfan
'''
''' recur + memoization '''
def climbStairs(n):
    assert(isinstance(n,int) and n>0),'input error'
    return _cs(n, {})

def _cs(n, h):
    if n == 1: return 1
    if n == 2: return 2
    if n in h: return h[n]
    h[n] = _cs(n-1, h) + _cs(n-2, h)
    return h[n]

''' dp
f(n) = f(n-1) + f(n-2)
roll over strategy, O(1) space
 '''
def solution(n):
    if n == 1: return 1
    if n == 2: return 2
    p1, p2 = 2, 1
    for _ in range(2,n):
        tmp = p1
        p1 += p2
        p2 = tmp
    return p1


''' unittest '''
print climbStairs(3), 'should be 3'
print climbStairs(5), 'should be 8'
print climbStairs(10), 'should be 89'
print climbStairs(19), 'should be 6765'

print solution(3)
print solution(5)
print solution(10)
print solution(19)
