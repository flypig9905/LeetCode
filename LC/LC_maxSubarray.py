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
import sys

def maxSubarrayDP(A):
    # assume correct input
    f = 0
    result = -sys.maxint
    for i in range(len(A)):
        ''' decide if add the previous consecutive array to current element A[i] or start a new subarray with A[i] '''
        f = max(f + A[i], A[i])
        ''' store the current best '''
        result = max(f, result)
    return result

A = [-2,1,-3,4,-1,2,1,-5,4]
print maxSubarrayDP(A), 'should be 6'


A = [1,-2,4,-3,5,2,-5,4]
print maxSubarrayDP(A), 'should be 8'