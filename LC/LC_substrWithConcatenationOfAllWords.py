'''

You are given a string, S, and a list of words, L, that are all of the same length. Find all starting indices of substring(s) in S that is a concatenation of each word in L exactly once and without any intervening characters.

For example, given:
S: "barfoothefoobarman"
L: ["foo", "bar"]

You should return the indices: [0,9].
(order does not matter).

Created on Feb 12, 2014

@author: Songfan
'''

''' hashtable storing the available words in L, recursion '''

class Solution:
    # @param S, a string
    # @param L, a list of string
    # @return a list of integer
    def findSubstring(self, S, L):
        n = len(S)
        m = len(L)
        if n == 0 or m == 0: return []
        wdLen = len(L[0])
        if n < len(L[0]): return []
        h = {}
        for l in L:
            h[l] = h.get(l, 0) + 1
        res = []
        for i in range(n):



 
#S = "barfoothefoobarman"
#L = ["foo", "bar"]
#ss = Solution()
#print ss.findSubstring(S, L)
    
    
S = "a"
L = ["a", "a"]  
ss = Solution()
print ss.findSubstring(S, L)
        
        
        
        