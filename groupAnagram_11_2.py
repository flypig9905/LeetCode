'''
CTCI 11-2, group anagram together from a string list

Created on Dec 7, 2013

@author: Songfan
'''
def groupAnagram(sList):
    assert(isinstance(sList,list)),'input error'
    h = {}
    for s in sList:
        ss = ''.join(sorted(s))
        if h.has_key(ss) and s not in h[ss]:
            h[ss].append(s)
        elif not h.has_key(ss):
            h[ss] = [s]
    result=[]
    for k in h.keys():
        result.extend(h[k])
    return result


sList = ['abc','cb','cba','bcc','bc']
print groupAnagram(sList)