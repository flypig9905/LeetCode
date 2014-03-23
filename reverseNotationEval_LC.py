'''
Evaluation a expression in reverse notation, LeetCode

Created on Dec 4, 2013

@author: Songfan
'''
from stack import Stack

def isExpr(e):
    return e in '+-*/'

def exprEval(op1,op2,op):
    op1 = float(op1)
    op2 = float(op2)
    if op=='+': return op1+op2
    if op=='-': return op1-op2
    if op=='*': return op1*op2
    if op=='/': return op1/op2


def reverseNotationEval(aList):
    assert(isinstance(aList,list)),"Input Error"
    s = Stack()
    for e in aList:
        if e.isdigit(): s.push(e)
        if isExpr(e):
            if not s.isEmpty():
                op2 = s.pop()
            else: return 'Error: wrong expression!'
            if not s.isEmpty():
                op1 = s.pop()
            else: return 'Error: wrong expression'
            val = exprEval(op1, op2, e)
            s.push(val)
    return s.pop()


aList = ['7','1','-','3','/','21','+']
print reverseNotationEval(aList)