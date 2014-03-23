'''

Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, 
with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note:
You are not suppose to use the library's sort function for this problem.


Follow up:
A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.

Could you come up with an one-pass algorithm using only constant space?

Created on Feb 3, 2014

@author: Songfan
'''

''' O(N) time, O(1) space, 2 pass: counting sort: counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.
    O(N) time, O(1) space, 1 pass: double pointer from front and back '''
    
def solution(A):
    # assume correct input
    n = len(A)
    zeroPtr = 0
    twoPtr = n - 1
    i = 0
    ''' be careful with the comparison, should be compared to twoPtr '''
    while i < twoPtr:
        if A[i] == 0:
            tmp = A[i]
            A[i] = A[zeroPtr]
            A[zeroPtr] = tmp
            zeroPtr += 1
        elif A[i] == 2:
            tmp = A[i]
            A[i] = A[twoPtr]
            A[twoPtr] = tmp
            twoPtr -= 1
        else:
            i += 1
    
    return A
            
            
A = [1,0,2,0,1,2,1]
print solution(A)
            
            
            
            