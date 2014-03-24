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

class Solution:
    # @param A, a list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        n = len(A)
        if n == 0: return 1
        i = 0
        while i < n:
            ''' index, ex: A[2] = 3 '''
            while A[i] != i+1:
                if A[i] < 0 or A[i] >= n or A[i]==A[A[i]-1]: break
                tmp = A[i]-1
                A[i], A[tmp] = A[tmp], A[i]
            i += 1
        for i in range(n):
            if A[i] != i + 1:
                return i + 1
        return n+1  # all positive number presents

''' unittest '''
ss = Solution()
A = [1,2,0]
print ss.firstMissingPositive(A), 'should be 3'

A = [3,4,-1,1]
print ss.firstMissingPositive(A), 'should be 2'

A = [2]
print ss.firstMissingPositive(A), 'should be 1'
