'''
Implement strStr().

Returns a pointer to the first occurrence of needle in haystack, or null if needle is not part of haystack.

haystack = "ABACDDA"
needle = "ACD"

Created on Jan 1, 2014

@author: Songfan
'''

''' O(m*n) algorithm: iterate through all element in haystack and compare '''

def strStr(s, p):
    if not p: return s
    n, m = len(s), len(p)
    if n < m: return
    for i in range(n-m):
        if s[i:i+m] == p:
            return i
               
               
s = 'ABACDDA'
p = 'ACD'
print strStr(s, p) 