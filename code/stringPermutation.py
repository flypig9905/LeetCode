'''
CTCI P54. Variation: Print all permutation of a string with unique characters
On Note page 1 (N1)

Cannot handle string with duplicated characters

Created on Nov 18, 2013

@author: Songfan
'''

def _insertAllPosition(c,aString):
    result = []
    for s in aString:
        for i in range(len(s)+1):
            curr_s = s[:i]+c+s[i:]
            result.append(curr_s)
    return result
 
def perm(s):
    assert(type(s) is str),"Input Error: the input should only be a string"
    if len(s)<=1:
        return s
    else:
        return _insertAllPosition(s[-1],perm(s[:-1]))

s = 'ab'*2
print s
print perm(s)