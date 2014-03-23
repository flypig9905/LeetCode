'''
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:
Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.

Created on Feb 9, 2014

@author: Songfan
'''

''' DP from bottom, replace elements in place. A[i,j] represents the minimum cost start from Triangle[i,j] down '''

def solution(Tri, n):

    for i in range(n-2, -1, -1):
        for j in range(i + 1):
            Tri[i, j] = min(Tri[i + 1,j], Tri[i + 1, j + 1]) + Tri[i, j]
    return Tri[0, 0]


Tri = {}
Tri[0,0] = 2
Tri[1,0] = 3
Tri[1,1] = 4
Tri[2,0] = 5
Tri[2,1] = 6
Tri[2,2] = 7
Tri[3,0] = 4
Tri[3,1] = 1
Tri[3,2] = 8
Tri[3,3] = 3

print solution(Tri, 4)