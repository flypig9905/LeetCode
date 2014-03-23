'''

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

For example,

"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.

Created on Jan 2, 2014

@author: Songfan
'''

''' thought: two pointer from begin and end, meet together '''

def isAlphaNum(s):
    return s.isalpha() or s.isdigit()

def isValidParlin(s):
    assert(isinstance(s,str)),'input error'
    n = len(s)
    if n == 1: return True
    s = s.lower()
    p1 = 0
    p2 = n - 1
    while p1 < p2:
        if not isAlphaNum(s[p1]):
            p1 += 1
            continue
        elif not isAlphaNum(s[p2]):
            p2 -= 1
            continue
        elif s[p1] != s[p2]:
            return False
        else:
            p1 += 1
            p2 -= 1
    return True
            
s = 'A man, a plan, a canal: Panama'
print isValidParlin(s), 'should be True'
s = 'race a car'
print isValidParlin(s), 'should be False'


            