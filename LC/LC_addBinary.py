'''

Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".

Created on Jan 12, 2014

@author: Songfan
'''

''' thought: two pointer track from the back '''

def addBinary(a, b):
    assert(isinstance(a,str) and isinstance(b,str)), 'input error'
    na = len(a)
    nb = len(b)
    res = ''
    carry = 0
    while(na > 0 or nb > 0):
        ''' mistake track: since we decrement na and nb, we need to judge 'na > 0' instead of 'na == 0' '''
        if na > 0: v1 = int(a[na-1])
        else: v1 = 0
        if nb > 0: v2 = int(b[nb-1])
        else: v2 = 0
        
        tmpTotal = v1 + v2 + carry
        tmpV = tmpTotal % 2
        carry = tmpTotal // 2
        
        res = str(tmpV) + res
        
        na -= 1
        nb -= 1
    if carry:
        res = '1' + res
    return res

a = '11'
b = '1'
print addBinary(a, b)