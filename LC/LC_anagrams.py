'''

Given an array of strings, return all groups of strings that are anagrams.

Note: All inputs will be in lower-case.

Created on Jan 12, 2014

@author: Songfan
'''

''' thoughts: hashtable where the key is the tuple (keyword, keyword occurance times)) 
time: O(n*k), n is the number of word in string list, k is the avg length of each word
space: O(n)
'''

def anagrams(S):
    # assume correct input
    h = {}  # group anagrams
    for word in S:
        ha = {} # check anagram
        for c in word:
            ha[c] = ha.get(c,0) + 1
        
        ''' caveat: sort key based on letter, and convert list to tuple (tuple can be key to dictionary but list cannot) '''
        tmpKey = sorted(ha.items(), key = lambda s : s[0])
        tmpKey = tuple(tmpKey)
        tmpVal = h.get(tmpKey, [])
        tmpVal.append(word)
        h[tmpKey] = tmpVal
    
    # arrange result
    res = []
    for v in h.values():
        res.append(v)
    return res

S = ['cat', 'dog', 'tac', 'god']
print anagrams(S)
