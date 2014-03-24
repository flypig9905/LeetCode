'''

Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

For example,
Given input array A = [1,1,2],

Your function should return length = 2, and A is now [1,2].

Created on Jan 14, 2014

@author: Songfan
'''

''' algorithm: two pointers '''
class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        n = len(A)
        if n == 0: return A
        if n == 1: return A
        idx1, idx2 = 0, 1
        while idx2 != n:
            if A[idx1] == A[idx2]:
                idx2 += 1
            else:
                idx1 += 1
                A[idx1] = A[idx2]
                idx2 += 1
        return A[:idx1+1]
    
ss = Solution()
A = [1, 1, 2]
print ss.removeDuplicates(A), 'should be [1, 2]'

A = [1, 2, 2]
print ss.removeDuplicates(A), 'should be [1, 2]'

            