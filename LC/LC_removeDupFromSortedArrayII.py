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
    if n <= 1: return A
    occ, slow, fast = 1, 0, 1
    while fast < n:
        if A[slow] == A[fast]:
            if occ < K:
                occ += 1
                slow += 1
        else:
            occ = 1
            slow += 1
        A[slow] = A[fast]
        fast += 1
    return A[:slow+1]
    
    

A = [1,1,1,2,2,3,5,6,6,6,6,7]
print solution(A, 2), 'should be [1, 1, 2, 2, 3, 5, 6, 6, 7]'

A = [1,1,1,1,3,3]
print solution(A, 2), 'should be [1, 1, 3, 3]'
   
A = [1,2]
print solution(A, 2), 'should be [1, 2]'
        
A = [1,1]
print solution(A, 2), 'should be [1, 2]'        
        