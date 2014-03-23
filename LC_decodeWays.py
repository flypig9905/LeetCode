'''

A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given an encoded message containing digits, determine the total number of ways to decode it.

For example,
Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).

The number of ways decoding "12" is 2.

Created on Jan 13, 2014

@author: Songfan
'''

''' thought: DP or recursion'''

def decodeWays(s):
    return _decode(s, len(s) - 1, {})

def _decode(s, idx, h):
    n = len(s)
    assert(n > idx),'input error'
    ''' caveat: idx should be one less than n '''
    if idx == -1: return 0
    if idx == 0: return 1
    if idx == 1:
        if int(s[0]) == 1 or (int(s[0]) == 2 and int(s[1]) <= 6): return 2
        else: return 1
    if idx in h: return h[idx]
    prev2 = _decode(s, idx - 2, h)
    prev1 = _decode(s, idx - 1, h)
    
    if int(s[idx - 1]) == 1 or (int(s[idx - 1]) == 2 and int(s[idx]) <= 6):
        ''' only satisfy this condition can we have another way of decoding '''
        h[idx] = prev1 + prev2
    else:
        h[idx] = prev1
        
    return h[idx]
        
        
''' unittest '''
s = '12'
print decodeWays(s), 'should be 2'

s = '124'
print decodeWays(s), 'shoule be 3'

s = '1212'
print decodeWays(s), 'should be 5'