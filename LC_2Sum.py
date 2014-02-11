'''
Given an array of integers, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, 
where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2

Created on Dec 29, 2013

@author: Songfan
'''

''' O(N) solution: use a map to store number as key, index as value, for every key, check if 'targe-k' is also a key '''
def twoSum1(arr, target):
    h = {}
    for i in range(len(arr)):
        h[arr[i]] = i+1
        
    for k in h:
        # if target - k is also a key, then it is the answer
        if target - k in h:
            idx1 = min(h[target-k], h[k])
            idx2 = max(h[target-k], h[k]) 
            return idx1, idx2
    return None, None


def SF_sort(aList):
    val = []
    idx = []
    for i in sorted(enumerate(aList), key = lambda x:x[1]):
        idx.append(i[0]) 
        val.append(i[1])
    return val, idx

''' O(N**2) algorithm: sort the list, then two pointer '''
''' on a second look, no need to sort '''

def twoSum(arr, target):
    # assume correct input
    arrSorted, idx = SF_sort(arr)
    arrLen = len(arr)
    for i in range(arrLen):
        for j in range(i,arrLen):
            if arrSorted[i] + arrSorted[j] == target:
                idx1 = min(idx[i]+1, idx[j]+1)
                idx2 = max(idx[i]+1, idx[j]+1)
                return idx1, idx2
            elif arrSorted[i] + arrSorted[j] > target:
                break
    return None, None



numbers = [9, 7, 2, 11, 15]
target = 9
print twoSum(numbers, target)
print twoSum1(numbers, target)
          
            
            
            
            
            
            
            
            
            
            
            