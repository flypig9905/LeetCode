'''
Created on Nov 3, 2013

@author: Songfan
'''
from stack import Stack

def doMath(op, op1, op2):
    if op=='+':
        return op1+op2
    elif op=='-':
        return op1-op2
    elif op=='*':
        return op1*op2
    elif op=='/':
        return op1/op2
#     else:
#         raise OperationNotSupportedError
# 
# class OperationNotSupportedError(Exception):
#     def __init__(self,message):
#         super(OperationNotSupportedError,self).__init__(message)
#         self.message = message
    

def postfixEval(postfixExpr):
    pe = postfixExpr.split()
    s = Stack()
    for p in pe:
        if p in "0123456789":
            s.push(p)
        elif p in "+-*/":
            if not s.isEmpty():
                if not s.peek().isdigit():
                    return False
            else:
                return False
            op2 = int(s.pop())
            if not s.isEmpty():
                if not s.peek().isdigit():
                    return False
            else:
                return False
            op1 = int(s.pop())
            s.push(str(doMath(p,op1,op2)))
        print "unrecognized character"
        return 
    if s.size()==1:
        return s.peek().isdigit()
    else:
        return False
            
print(postfixEval('7 8 + 3 4 + 3 2 + /'))