'''
Given a stream of integers, 
all of which come in pairs except for one, find the integer without a duplicate

Created on Mar 17, 2014

@author: Songfan
'''

'''
one pass, xor
'''

def findUnique(stream):
    res = 0
    for s in stream:
        res ^= s
    return res

print findUnique([1,2,1,3,2,5,3])