'''
CTCI P81 3-6
sort a stack using only one additional stack and stack operations

Created on Nov 22, 2013

@author: Songfan
'''
from stack import Stack
# 
# def sortStack(s):
#     assert(isinstance(s,Stack)),"Input Error: input must be a stack"
#     if s.isEmpty():
#         return s
#     s1 = Stack()
#     s1.push(s.pop())
#     while(not s.isEmpty()):
#         tmp = s.pop()
#         counter = 0                 # can be improved, counter is not needed since we can compare the number by peeking
#         while(not s1.isEmpty()):
#             if tmp<s1.peek():
#                 s.push(s1.pop())
#                 counter += 1
#             else:
#                 break               # break in while can be added to while()
#         s1.push(tmp)
#         while(counter!=0):
#             s1.push(s.pop())
#             counter -= 1
#     return s1

def sortStack(s):
    assert(isinstance(s,Stack)),"Input Error: input must be a stack"
    if s.isEmpty():
        return s
    s1 = Stack()
    s1.push(s.pop())
    while(not s.isEmpty()):
        tmp = s.pop()
        while(not s1.isEmpty() and tmp<s1.peek()):
            s.push(s1.pop())
        s1.push(tmp)
        while(not s.isEmpty() and s.peek()>=s1.peek()):
            s1.push(s.pop())
    return s1


aStack = Stack()
print aStack
# test empty stack
print sortStack(aStack)
# test normal case
from random import randrange
test_items = [randrange(100) for x in xrange(20)]
for i in test_items:
    aStack.push(i)

print aStack
print sortStack(aStack)