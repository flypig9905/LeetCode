'''
Given an array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Created on Dec 28, 2013

@author: Songfan
'''

''' use extra memory '''
def singleInt(arr):
    # assuem correct input
    h = {}
    for e in arr:
        if e not in h:
            h[e] = 1
        else:
            h[e] -= 1
    
    for k in h:
        if h[k] == 1:
            return k
        
''' without extra memory: This problem can be solved using X-OR operations because (A)^(B)^(A) = B.'''
def singleInt1(arr):
    r = 0
    for e in arr:
        r ^= e
    return r


arr = [1,1,2,3,2]
print singleInt(arr)
print singleInt1(arr)