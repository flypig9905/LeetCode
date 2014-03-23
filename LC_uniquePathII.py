'''

Follow up for "Unique Paths":

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

Created on Jan 26, 2014

@author: Songfan
'''

''' assume the obstacle is given in vector ex: [(1,2),(2,2)] '''

def solution(m, n, Obs):
    return _uniquePath(m - 1, n - 1, Obs, {})

def _uniquePath(i, j, Obs, h):
    if i == 0 or j == 0:
        ''' in this case, have to check if every position along the boudary is in the Obs ''' 
        for k in range(i + 1):
            for l in range(j + 1):
                if (k, l) in Obs: return 0
        return 1
    if (i, j) in h: return h[i,j]
    total = 0
    if (i - 1, j) not in Obs:
        total += _uniquePath(i - 1, j, Obs, h)
    if (i, j - 1) not in Obs:
        total += _uniquePath(i, j - 1, Obs, h)
    h[i,j] = total
    return total

m = 3
n = 3
Obs = [(1,1)]
print solution(m, n, Obs)