'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

Created on Dec 30, 2013

@author: Songfan
'''
from stack import Stack

''' use stack '''
def validParen(s):
    stk = Stack()
    for e in s:
        if e in '([{':  # push left-sided parens
            stk.push(e)
        else:
            # stack shouldn't be empty given a right-sided paren
            if stk.isEmpty(): return False  
            if e == ')' and stk.peek() != '(': return False
            if e == ']' and stk.peek() != '[': return False
            if e == '}' and stk.peek() != '{': return False
            stk.pop()
    return stk.isEmpty()    # elegent

            
''' unittest '''
s = '()[]{}'
print validParen(s), 'should be True'
s = '([])({})'
print validParen(s), 'should be True'
s = ')[]{}'
print validParen(s), 'should be False'
s = '([)]{}'
print validParen(s), 'should be False'
s = '()[]{'
print validParen(s), 'should be False'



