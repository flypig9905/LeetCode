'''

Given an unsorted integer array, find the first missing positive integer.

For example,
Given [1,2,0] return 3,
and [3,4,-1,1] return 2.

Your algorithm should run in O(n) time and uses constant space.

Created on Feb 2, 2014

@author: Songfan
'''

''' thought process:
    1. O(NlogN) time, O(1) space: sort and scan
    2. O(N) time, O(N) space: hash + linear scan 
    3. O(N) time, O(1) space: linear scan and swap element to the correct index
    
'''

def solution(A):
    n = len(A)
    if n == 0: return -1
    i = 0
    while i < n:
        ''' be careful with the index, ex: A[2] = 3 '''
        if A[i] > 0 and A[i] != i + 1:
            tmp = A[i]
            A[i] = A[tmp - 1]
            A[tmp - 1] = tmp
        else:
            i += 1
    for i in range(n):
        if A[i] != i + 1:
            return i + 1
    return -1

''' unittest '''
A = [1,2,0]
print solution(A), 'should be 3'

A = [3,4,-1,1]
print solution(A), 'should be 2'