'''
CTCI 11-2, group anagram together from a string list

Created on Dec 7, 2013

@author: Songfan
'''

''' algorithm: use a hashtable to add anagram to the same key '''

def groupAnagram(sList):
    assert(isinstance(sList,list)),'input error'
    h = {}
    for s in sList:
        ss = ''.join(sorted(s))
        if ss in h and s not in h[ss]:
            h[ss].append(s)
        elif ss not in h:
            h[ss] = [s]
    result=[]
    for k in h.keys():
        result.extend(h[k])
    return result


sList = ['abc','cb','cba','bcc','bc']
print groupAnagram(sList)