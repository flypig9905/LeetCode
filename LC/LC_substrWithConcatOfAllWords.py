'''

You are given a string, S, and a list of words, L, that are all of the same length. Find all starting indices of substring(s) in S that is a concatenation of each word in L exactly once and without any intervening characters.

For example, given:
S: "barfoothefoobarman"
L: ["foo", "bar"]

You should return the indices: [0,9].
(order does not matter).

Created on Feb 13, 2014

@author: Songfan
'''

''' iterative solution. (recursive solution will get TLE) Use two hashtable to maintain the current dictionary '''
class Solution:
    # @param S, a string
    # @param L, a list of string
    # @return a list of integer
    def findSubstring(self, S, L):
        n = len(S)
        m = len(L)
        if n == 0 or m == 0: return []
        
        wordLen = len(L[0])
        if n < wordLen: return []

        dictionary = {}
        dictWordLen = 0
        for l in L:
            dictionary[l] = dictionary.get(l, 0) + 1
            dictWordLen += len(l)
        
        res = []
        # consider every position as the starting of our checkig procedure
        for i in range(n):
            d = dictionary.copy()
            if n - i < dictWordLen: return res  # pruning, very import for not TLE
            if self._checkSubstr(S, i, wordLen, d):
                res.append(i)
        return res
        
    def _checkSubstr(self, S, i, wordLen, d):
        ptr = i
        while ptr + wordLen <= len(S):
            currWord = S[ptr:ptr+wordLen]
            if currWord in d:
                d[currWord] -= 1
                if d[currWord] == 0: d.pop(currWord)
                if not d: return True
            elif currWord not in d:
                return False
            ptr += wordLen
            
        return False
        
        
S = "barfoothefoobarman"
L = ["foo", "bar"]        
ss = Solution()
print ss.findSubstring(S, L), 'should be [0,9]'
print ss.findSubstring('a', ['a','a']), 'should be []'   
print ss.findSubstring('a', ['a']), 'should be [0]'         