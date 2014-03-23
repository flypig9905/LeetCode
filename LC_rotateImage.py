'''

You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Follow up:
Could you do this in-place?

Created on Feb 3, 2014

@author: Songfan
'''

''' consider the outer elements as 1st layer, rotate each layer 
    be careful with indices
'''

def solution(M):
    n = len(M)
    if n == 0 or n == 1: return M
    # if n is even, layerNum = n//2
    # if n is odd, layerNum = n//2 + 1, but there is no need to change the center element for this case
    for l in range(n // 2):
        m = n - 1 - l * 2   # the length of element of current layer - 1
        for i in range(m):
            tmp = M[l][i+l] # up
            M[l][i+l] = M[n-l-1-i][l]    # left
            M[n-l-1-i][l] = M[n-l-1][n-l-1-i]    # down
            M[n-l-1][n-l-1-i] = M[i+l][n-l-1]  # right
            M[i+l][n-l-1] = tmp
    return M
            
    
    
    
    
M = [[1,2,3,4,5],[2,3,4,5,6],[3,4,5,6,7],[4,5,6,7,8],[5,6,7,8,9]]
print 'original matrix'
for m in M:
    print m

print 'right rotation 90 degree'
M1 = solution(M)
for m in M1:
    print m