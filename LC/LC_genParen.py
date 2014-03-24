'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

"((()))", "(()())", "(())()", "()(())", "()()()"

Created on Jan 10, 2014

@author: Songfan
'''
''' algorithm: recursion '''

class Solution:
    # @param an integer
    # @return a list of string
    def generateParenthesis(self, n):
        assert(isinstance(n,int) and n >= 0),'input error'
        return self._genParen(n, {})
    
    def _genParen(self, n, h):
        if n == 0: return []
        if n == 1: return ['()']
        if n in h: return h[n]
        prev = self._genParen(n-1, h)
        curr = []
        for s in prev:
            for i in range(len(s)):
                tmp = s[:i] + '()' + s[i:]
                if tmp not in curr:
                    curr.append(tmp)
        h[n] = curr
        return h[n]

''' unittest '''
ss = Solution()
print ss.generateParenthesis(4)