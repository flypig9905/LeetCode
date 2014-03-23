'''

Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place, do not allocate extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
1,2,3 -> 1,3,2
3,2,1 -> 1,2,3
1,1,5 -> 1,5,1

Created on Feb 1, 2014

@author: Songfan
'''
'''
Step 1: From right to left, find the first digit (partitionNum) which violate the increase trend. 
    If not exist, this is the last permutation. (in this problem just reverse the vector and return.)
Step 2: From right to left, find the first digit which is larger than PartitionNumber, call it changeNum
Step 3: Swap partitionNum and changeNum.
Step 4: Reverse the digit on the right of partition index.
'''

def nextPerm(A):
    n = len(A)
    if n == 0 or n == 1: return A 
    ''' step 1 '''
    idx = n - 1
    while idx > 0:
        if A[idx] > A[idx - 1]:
            break
        idx -= 1
    if idx == 0:
        ''' no voilation of increase order, reverse list and return '''
        A = A[::-1]
        return A
    partitionIdx = idx - 1
    
    ''' step 2, should use binary search, for simplicity, just linear scan '''
    idx = n - 1
    while idx > 0:
        if A[idx] > A[partitionIdx]:
            changeIdx = idx
            break
        idx -= 1
    
    ''' step 3 '''
    tmp = A[changeIdx]
    A[changeIdx] = A[partitionIdx]
    A[partitionIdx] = tmp
    
    ''' step 4 '''
    A[partitionIdx+1:].reverse()    # no assignment needed
    
    return A


A = [1,2,3]
print nextPerm(A), 'should be [1,3,2]'
A = [3,2,1]
print nextPerm(A), 'should be [1,2,3]'
A = [1,1,5]
print nextPerm(A), 'should be [1,5,1]'

    
    
    
    
    
    
    
    
    
    
    
    