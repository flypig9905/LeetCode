'''
CTCI P109 9_4

return all subsets of a set

Created on Dec 2, 2013

@author: Songfan
'''

def subsets(s):
    assert(isinstance(s,str)),'input error: take string input'
    length = len(s)
    if length==0: return ['']
    if length==1: return [s,'']
    h = {}  #cache
    if s in h.keys():   return h[s]
    else:
        tmp = s[0]
        result = subsets(s[1:])
        result.extend([p + tmp for p in result])
        h[s] = result
    return result


def subsets1(s):
    ''' correct dp algorithm '''
    assert(isinstance(s,str)),'input error: take string input'
    return _subsets(s,{})

def _subsets(s,h):
    length = len(s)
    if length==0: return ['']
    if length==1: return [s,'']
    if s in h.keys():   return h[s]
    else:
        tmp = s[0]
        result = subsets(s[1:])
        result.extend([p + tmp for p in result])
        h[s] = result
    return result

s = 'abcd'
print subsets1(s)
print subsets(s)