'''

Given a string, find the length of the longest substring without repeating characters. 

For example, the longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3. 
For "bbbbb" the longest substring is "b", with the length of 1.

Created on Jan 30, 2014

@author: Songfan
'''

''' two pointer + hashtable
    while currChar:
        store (nextChar, position) to hashtable until nextChar is duplicated with previous,
        store the longest length
        update currChar to the next position of duplicates

    Summary: for unordered sequence and occurance, think about hashtable
'''
def solution(A):
    n = len(A)
    if n == 0 or n == 1: return n
    curr = 0
    longest = 0
    tmpLen = 0
    h = {}
    while curr < n:
        if A[curr] not in h:
            h[A[curr]] = curr
            curr += 1
            tmpLen += 1
        else:
            prevPos = h[A[curr]]
            curr = prevPos + 1
            longest = max(tmpLen, longest)
            # update tmp var
            h = {}
            tmpLen = 0
            
    return longest

A = 'abcabcbb'
print solution(A), 'should be 3'

A = 'bbbb'
print solution(A), 'should be 1'
            
            
            
            
            
            
            
            
            
            
            
            