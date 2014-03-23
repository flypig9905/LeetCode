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
    slower = 0
    faster = 0
    cnt = 0
    while faster < n:
        ''' check cnt '''
        if A[faster] == A[slower] and cnt < K:
            cnt += 1
            faster += 1
        elif A[faster] == A[slower]:
            faster += 1
        else:
            slower += cnt
            A[slower] = A[faster]
            faster += 1
            cnt = 1
    return A[:slower+1]

A = [1,1,1,2,2,3,5,6,6,6,6,7]
print solution(A, 2), 'should be [1, 1, 2, 2, 3, 5, 6, 6, 7]'
        
        
        
        
        