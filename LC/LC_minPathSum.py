'''

Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Created on Jan 27, 2014

@author: Songfan
'''

''' memoization '''

def minPathSum(Grid):
    row = len(Grid)
    col = len(Grid[0])
    return _minSumDP(Grid, row - 1, col - 1, {})

def _minSumDP(Grid, k, l, h):
    tot = 0
    if k == 0:
        for j in range(l+1):
            tot += Grid[0][j]
        return tot
    if l == 0:
        for i in range(k+1):
            tot += Grid[i][0]
        return tot
    if (k,l) in h: return h[k,l]
    ''' min path from left or from top, add the current value '''
    tot = min(_minSumDP(Grid, k - 1, l, h), _minSumDP(Grid, k, l - 1, h)) + Grid[k][l]
    h[k,l] = tot
    return tot    
    
''' unittest '''    
Grid = [[1,1,2,2],[2,1,1,1],[2,2,2,1],[2,2,2,1]]
print minPathSum(Grid)