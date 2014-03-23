'''

Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

For example:
Given array A = [2,3,1,1,4]

The minimum number of jumps to reach the last index is 2. (Jump 1 step from index 0 to 1, then 3 steps to the last index.)

Created on Feb 2, 2014

@author: Songfan
'''

''' DP: O(N^2)
    Greedy: O(N)
        key idea: all the positions before the maximum reachable distance would be able to be reached in minimum steps
        keey three variables
        (1) the current maximum reach distance (currMax)
        (2) the number of steps to reach this current maximum distances (step)
        (3) the next maximum reachable distance (nextMax)
'''

def solution(A):
    n = len(A)
    if n == 0: return -1
    
    currMax = 0
    nextMax = 0
    step = 0
    for i in range(n):
        if i > currMax:
            ''' we are now beyond the currMax, 
            need to take one step, update currMax '''
            currMax = nextMax
            step += 1
        nextMax = max(nextMax, A[i] + i)
    return step
            
A = [2,3,1,1,4]
print solution(A), 'should be 2'













