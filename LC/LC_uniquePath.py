'''

Unique Path

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. 
The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

Created on Jan 26, 2014

@author: Songfan
'''
def solution(m, n):
    return _uniquePath(m - 1, n - 1, {})

def _uniquePath(i, j, h):
    if i == 0 or j == 0: return 1
    if (i,j) in h: return h[i,j]
    h[i,j] = _uniquePath(i - 1, j, h) + _uniquePath(i, j - 1, h)
    return h[i,j]

m = 4
n = 3
print solution(m, n)