'''

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

For example, 
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.

Created on Feb 2, 2014

@author: Songfan
'''

''' for a specific A[i], the water it can trapped depends on the largest height on its left and right (actually min of those two),
    as well as A[i] itself. More precisely, trapped[i] = min(min(leftHighest, rightHighest) - A[i], 0) '''

def solution(A):
    n = len(A)
    
    ''' cannot trap any water '''
    if n <= 2: return 0
    
    ''' 1st run to calculate the highest bar on the left of each bar '''
    lmh = [0]*n
    maxh = A[0]
    for i in range(1, n):
        lmh[i] = maxh
        if maxh < A[i]:
            maxh = A[i]
    trapped = 0
    
    ''' 2nd run from right to left, calculate the highest bar on the right of each bar and compute trapped water simutaniouly '''
    maxh = A[n-1]
    for i in range(n-2, 0, -1):
        left = lmh[i]
        right = maxh
        container = min(left, right)
        if container > A[i]:
            trapped += container - A[i]
        if maxh < A[i]:
            maxh = A[i]
            
    return trapped
    
    
A = [0,1,0,2,1,0,1,3,2,1,2,1]
print solution(A), 'should be 6'
    
    
    
    
    
    
    
    
    
    
            
    