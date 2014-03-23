'''

Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

For example,
Given [100, 4, 200, 1, 3, 2],
The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.

Your algorithm should run in O(n) complexity.

Created on Jan 30, 2014

@author: Songfan
'''

''' O(NlogN): sort and find
    O(N): since unorder think of hashtable;
        use a hashtable to store if each element is appearred; for each element in hashtable search left and right until unconsecutiveness breaks, then store longest 
    Need to discuss with Lao Jin
        '''
    
def solution(A):
    h = {}
    for a in A:
        h[a] = True
    
    longest = 1
    for a in h:
        tmpVal = a + 1
        tmpLen = 1
        while tmpVal in h:
            tmpLen += 1
            tmpVal += 1
        
        tmpVal = a - 1
        while tmpVal in h:
            tmpLen += 1
            tmpVal -= 1
        
        if tmpLen > longest:
            longest = tmpLen
            
    return longest

A = [10,4,20,1,3,2]
print solution(A)