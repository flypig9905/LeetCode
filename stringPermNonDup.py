'''
CTCI P54. Variation: Print all permutation of a string with unique characters
On Note page N1


Created on Nov 18, 2013

@author: Songfan
'''

def removeEmptyKey(h):
    keys = h.keys()
    for k in keys:
        if h[k]==0:
            h.pop(k)

def permHelper(h):
    result = []
    keys = h.keys()
    for key in keys:
        if h[key]>0:
            h[key]-=1
            sList = permHelper(h)
            h[key]+=1
            if sList:
                result.extend([key+s for s in sList])
            else:
                result = key
    return result
                
def perm(s):
    h = {}
    for c in s:
        h[c] = h.get(c,0)+1
    print h
    return permHelper(h)

s = 'ab'*2
print perm(s)