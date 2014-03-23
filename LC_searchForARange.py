'''

Given a sorted array of integers, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].

Created on Jan 24, 2014

@author: Songfan
'''

''' thought: two similar binary search method, one for lower bound, one for upper bound
lower bound method: if A[mid] == target, keep on searching left, until A[mid-1] < A[mid]
upper bound method: if A[mid] == target, keep on searching right, until A[mid] < A[mid+1]
'''

def searchRange1(A, t):
    ''' method 1 '''
    upper = _upper(A, t)
    lower = _lower(A, t)

    if upper == -1 or lower == -1: return [-1,-1]
    else: return [lower, upper]

def _lower(A, t):
    n = len(A)
    if n == 0: return -1
    left = 0
    right = n - 1
    while left <= right:
        mid = (left + right) // 2
        if A[mid] == t:
            if mid == 0: return mid
            if A[mid-1] == t: 
                right = mid - 1
            else:
                return mid 
        elif A[mid] < t: 
            left = mid + 1
        else: 
            right = mid - 1
    return -1
        
def _upper(A, t):
    n = len(A)
    if n == 0: return -1
    left = 0
    right = n - 1
    while left <= right:
        mid = (left + right) // 2
        if A[mid] == t:
            if mid == n - 1: return mid
            if A[mid + 1] == t: left = mid + 1
            else: return mid
        elif A[mid] < t: 
            left = mid + 1
        else: 
            right = mid - 1
    return -1


print 'method 1'
A = [5, 7, 7, 8, 8, 10]
print searchRange1(A, 8), 'should be [3,4]'
print searchRange1(A, 7), 'should be [1,2]'
print searchRange1(A, 3), 'should be [-1,-1]'

A = [1,2,2,2,3]
print searchRange1(A, 1), 'should be [0,0]'
print searchRange1(A, 2), 'should be [1,3]'
print searchRange1(A, 3), 'should be [4,4]'
print searchRange1(A, 0), 'should be [-1,-1]'
print searchRange1(A, 4), 'should be [-1,-1]'
