'''

Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

For example,
Given n = 3,

You should return the following matrix:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]

Created on Feb 3, 2014

@author: Songfan
'''
def solution(n):
    M = {}
    num = 1
    first = 0
    last = n - 1
    while first < last:
        # up
        for i in range(first, last):
            M[first,i] = num
            num += 1
        # right
        for i in range(first, last):
            M[i,last] = num
            num += 1
        # down
        for i in range(last, first, -1):
            M[last,i] = num
            num += 1
        # left
        for i in range(last, first, -1):
            M[i,first] = num
            num += 1
        first += 1
        last -= 1
    
    if first == last:
        M[first,first] = num
    return M

n = 4   
M = solution(n)    
for i in range(n):
    tmp = []
    for j in range(n):
        tmp.append(M[i,j])
    print tmp