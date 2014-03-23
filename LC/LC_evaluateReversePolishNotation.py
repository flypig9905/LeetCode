'''
Evaluation a expression in reverse notation, LeetCode

Created on Dec 4, 2013

@author: Songfan
'''
from stack import Stack

class Solution:
    # @param tokens, a list of string
    # @return an integer

    
    def isExpr(self, e):
        return e in '+-*/'

    def exprEval(self, op1,op2,op):
        op1 = int(op1)
        op2 = int(op2)
        if op=='+': return op1+op2
        if op=='-': return op1-op2
        if op=='*': return op1*op2
        if op=='/': return op1/op2
    
    def isValidNum(self, s):
        return s.isdigit() or ((s[0] == '-' or s[0] == '+') and s[1:].isdigit())
    
    def evalRPN(self, tokens):
        s = Stack()
        for e in tokens:
            if self.isValidNum(e): s.push(e)
            elif self.isExpr(e):
                if not s.isEmpty():
                    op2 = s.pop()
                else: return 'Error: wrong expression!'
                if not s.isEmpty():
                    op1 = s.pop()
                else: return 'Error: wrong expression'
                val = self.exprEval(op1, op2, e)
                s.push(val)
        return int(s.pop())


aList = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
ss = Solution()
print ss.evalRPN(aList), 'should be 22'