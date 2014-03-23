'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

"((()))", "(()())", "(())()", "()(())", "()()()"

Created on Jan 10, 2014

@author: Songfan
'''
''' algorithm: recursion '''

def genParen(n):
    assert(isinstance(n,int) and n >= 0),'input error'
    return _genParen(n, {})

def _genParen(n, h):
    if n == 0: return []
    if n == 1: return ['()']
    if n in h: return h[n]
    prev = _genParen(n-1, h)
    curr = []
    for s in prev:
        for i in range(len(s)):
            tmp = s[:i] + '()' + s[i:]
            if tmp not in curr:
                curr.append(tmp)
    h[n] = curr
    return h[n]

print genParen(4)