'''

Given two strings s1 and s2 of the same length, determine if s2 is a scrambled string of s1.

Given a string s1, we may represent it as a binary tree by partitioning it to two non-empty substrings recursively.
Below is one possible representation of s1 = "great":

    great
   /    \
  gr    eat
 / \    /  \
g   r  e   at
           / \
          a   t
To scramble the string, we may choose any non-leaf node and swap its two children.

For example, if we choose the node "gr" and swap its two children, it produces a scrambled string "rgeat".


Created on Feb 4, 2014

@author: Songfan
'''

''' recursion + memoization: if s1 is a scrambled string of s2 (isScramble(s1,s2)), there must exist a seperating position k to seperate s1 and s2 to
    s1[:k], s1[k:] and (s2[:k], s2[k:] or s2[-i:], s2[:-i]) so that 
    either isScramble(s1[:k],s2[:k]) and isScramble(s1[k:],s2[k:])
    or isScramble(s1[:k],s2[-i:]) and isScramble(s1[k:],s2[:-i])
'''

def solution(s1, s2):
    return isScramble(s1, s2, {})

def isScramble(s1, s2, h):
    if s1 == s2: return True
    if (s1, s2) in h: return h[s1,s2]
    
    n1 = len(s1)
    n2 = len(s2)
    if n1 != n2: return False
    if sorted(s1) != sorted(s2): return False
    
    for i in range(1, n1):
        ''' python index is so beautiful '''
        if (isScramble(s1[:i], s2[:i], h) and isScramble(s1[i:], s2[i:], h)) or \
            (isScramble(s1[:i],s2[-i:], h) and isScramble(s1[i:],s2[:-i], h)):
            h[s1, s2] = True
            return True
    return False
    
s1 = 'great'
s2 = 'rgaet'
print solution(s1, s2)
    
    
    