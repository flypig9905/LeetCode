'''

Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [-2, 1, -3, 4, -1, 2, 1, -5, 4]
the contiguous subarray [4,-1,2,1] has the largest sum = 6.

click to show more practice.

More practice:
If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

Created on Jan 24, 2014

@author: Songfan
'''

''' DP: let f[j] be the maximum subarray at j,
        f[j] = max{f[j-1]+A[j], A[j]}
        target = max{f[j]}
'''
class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxSubArray(self, A):
        # let f[i] be the max subarray at i
        # f[i] = max(f[i-1]+A[i], A[i])
        # result = max(f[i])
        n = len(A)
        if n == 0: return
        if n == 1: return A[0]
        res, f = A[0], A[0]
        for i in range(1,n):
            f = max(f + A[i], A[i])
            res = max(res, f)
        return res

''' unittest '''
ss = Solution()
A = [-2,1,-3,4,-1,2,1,-5,4]
print ss.maxSubArray(A), 'should be 6'


A = [1,-2,4,-3,5,2,-5,4]
print ss.maxSubArray(A), 'should be 8'