'''

Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). 
n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). 
Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container.

Created on Jan 31, 2014

@author: Songfan
'''

''' two pointer from beginning and end moving towards middle, move which ever is smaller every time.
    The reason for this is because that there will be no volume larger if we don't move smaller '''
    
def solution(A):
    n = len(A)
    if n == 0 or n == 1: return None
    first = 0
    last = n - 1
    maxVol = 0
    while first < last:
        currVol = (last - first) * min(A[first], A[last])
        maxVol = max(currVol, maxVol)
        if A[first] < A[last]:
            first += 1
        else:
            last -= 1
    return maxVol

A = [2,3,1000,4]
print solution(A), 'should be 6'