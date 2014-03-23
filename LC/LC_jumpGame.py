'''

Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

For example:
A = [2,3,1,1,4], return true.

A = [3,2,1,0,4], return false.

Created on Feb 2, 2014

@author: Songfan
'''

''' start from left and jump right, check every possible location and find out max reach position (currMax), if currMax >= n in the end, return True

'''

def solution(A):
    n = len(A)
    if n == 0: return False
    
    currMax = 0
    for i in range(n):
        if i > currMax:
            ''' we cannot even reach i '''
            return False
        currMax = max(currMax, A[i] + i)
    return currMax >= n - 1

A = [2,3,1,1,4]
print solution(A), 'should be True'
    
A = [3,2,1,0,4]
print solution(A), 'should be False'
    
    