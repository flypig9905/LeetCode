'''

Write a function to find the longest common prefix string amongst an array of strings.

Created on Feb 12, 2014

@author: Songfan
'''

''' compare each position of every string until unequal '''

def solution(strs):
    n = len(strs)
    if n == 0: return ''
    if n == 1: return strs[0]
    
    # find minimum length of the strings
    minLen = len(strs[0])
    for s in strs:
        tmpLen = len(s)
        if tmpLen < minLen:
            minLen = tmpLen
    
    res = ''
    for i in range(minLen):   # position
        c = strs[0][i]
        for j in range(1, n):   # strings
            if c != strs[j][i]:
                return res
        res += c
        
    return res

strs = ['abc','ab','acd']
print solution(strs)