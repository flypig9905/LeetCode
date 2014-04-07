'''

Follow up for "Remove Duplicates":
What if duplicates are allowed at most twice?

For example,
Given sorted array A = [1,1,1,2,2,3],

Your function should return length = 5, and A is now [1,1,2,2,3].

Created on Feb 4, 2014

@author: Songfan
'''

''' 2 ptr + have a counter track the occurance '''

def solution(A, K):
    n = len(A)
    if n == 0 or n == 1: return A
    faster, slower, cnt = 1, 0, 0
    cur = A[0]
    while faster < n:
        if A[faster] == cur and cnt < K:
            A[slower] = cur
            cnt += 1
            slower += 1
        elif A[faster] != cur:
            cur = A[faster]
            A[slower] = cur
            cnt = 1
            slower += 1
        faster += 1

    return A[:slower]

A = [1,1,1,2,2,3,5,6,6,6,6,7]
print solution(A, 2), 'should be [1, 1, 2, 2, 3, 5, 6, 6, 7]'

A = [1,1,1,1,3,3]
print solution(A, 2), 'should be [1, 1, 3, 3]'
   
        
        
        
        