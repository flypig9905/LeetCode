'''

Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

For example,
Given the following matrix:

[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
You should return [1,2,3,6,9,8,7,4,5].

Created on Feb 3, 2014

@author: Songfan
'''
''' similar idea as rotate image, from outter layer inwards, set up variable called beginX, endX, beginY, endY
    while loop, update each variable and check validity after each step of up, right, down, left order '''
def solution(M):
    beginR = 0
    beginC = 0
    endR = len(M) - 1
    endC = len(M[0]) - 1

    res = []
    while True:
        ''' get elements layer by layer '''
        # up
        for i in range(beginC,endC + 1):
            res.append(M[beginR][i])
        beginR += 1 # just finished beginning row, updated
        if beginR > endR: break
        
        # left
        for i in range(beginR, endR + 1):
            res.append(M[i][endC])
        endC -= 1   # just finished add the elements in the end column
        if beginC > endR: break
        
        # down
        for i in range(endC, beginC - 1, -1):
            res.append(M[endR][i])
        endR -= 1
        if beginR > endR: break
        # left
        for i in range(endR, beginR - 1, -1):
            res.append(M[i][beginC])
        beginC += 1
        if beginC > endC: break
        
    return res
        
''' unittest '''
M = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
print solution(M)
    