'''

Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
For example,

Consider the following matrix:

[
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
Given target = 3, return true.

Created on Jan 27, 2014

@author: Songfan
'''
''' thought: binary search on the first column to find the correct row, then binary search on the correct row '''
''' since this special property 'The first integer of each row is greater than the last integer of the previous row', we can consider the matrix as 
a big sorted list, need to compute the row and col from mid carefully'''

class Solution:
    # @param matrix, a list of lists of integers
    # @param target, an integer
    # @return a boolean
    def searchMatrix(self, M, t):
        row = len(M)
        col = len(M[0])
        if row == 0 or col == 0: return False
        first = 0
        last = row * col - 1
        while(first <= last):
            mid = (first + last) // 2
            r = mid // col
            c = mid % col
            if M[r][c] == t: return True
            elif M[r][c] < t: first = mid + 1
            else: last = mid - 1
        return False


''' unittest '''
M = [[1,   3,  5,  7],
     [10, 11, 16, 20],
     [23, 30, 34, 50]]
ss = Solution()
print ss.searchMatrix(M, 3),   'should be True'
print ss.searchMatrix(M, 50),  'should be True'
print ss.searchMatrix(M, 4),   'should be False'

M = [[-9,-8],[-5,-3],[-1,1],[4,4]]
print ss.searchMatrix(M, -15),   'should be False'  
        
print ss.searchMatrix([[1, 1]], 1),   'should be True'        
        
        
        
        
        
        