'''

Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

For "(()", the longest valid parentheses substring is "()", which has length = 2.

Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.

Created on Feb 6, 2014

@author: Songfan
'''

''' dp + stack: '''

from stack import Stack

def solution(S):
    n = len(S)
    if n <= 1: return 0
    s = Stack()
    maxLen = 0
    last = -1
    for i in range(n):
        if S[i] == '(':
            s.push(i)
        else:
            if s.isEmpty():
                last = i
            else:
                s.pop()
                # global best vs. current best
                if s.isEmpty():
                    maxLen = max(maxLen, i - last)  
                else:
                    maxLen = max(maxLen, i - s.peek())
    return maxLen
                    
S = '())(())'
print solution(S),'should be 4'
        
        
        
        
        