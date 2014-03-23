'''

Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

For example,
Given:
s1 = "aabcc",
s2 = "dbbca",

When s3 = "aadbbcbcac", return true.
When s3 = "aadbbbaccc", return false.

Created on Feb 5, 2014

@author: Songfan
'''
''' DP '''
def isInterleave(self, s1, s2, s3):
    n1, n2, n3 = len(s1), len(s2), len(s3)
    if n1 == 0: return s2 == s3
    if n2 == 0: return s1 == s3
    if n1 + n2 != n3: return False
    R = {}
    R[-1,-1] = True
    for i in range(n1):
        R[i,-1] = R[i-1,-1] and s1[i]==s3[i]
    for j in range(n2):
        R[-1,j] = R[-1,j-1] and s2[j]==s3[j]
        
    for i in range(n1):
        for j in range(n2):
            R[i,j] = (s3[i+j+1]==s1[i] and R[i-1,j]) or \
                        (s3[i+j+1]==s2[j] and R[i,j-1])
    return R[n1-1,n2-1]



''' recur: TLE '''
def solution(s1, s2, s3):
    return isInterleaving(s1, s2, s3, {})

def isInterleaving(s1, s2, s3, h):
    n1 = len(s1)
    n2 = len(s2)
    if n1 == 0: return s2 == s3
    if n2 == 0: return s1 == s3
    if (s1, s2, s3) in h: return h[s1,s2,s3]
    if s3[0] != s1[0] and s3[0] != s2[0]: return False  # pruning
    
    
    match1 = False
    match2 = False
    
    if s3[0] == s1[0]:
        match1 = isInterleaving(s1[1:], s2, s3[1:], h)
    
    if s3[0] == s2[0]:
        match2 = isInterleaving(s1, s2[1:], s3[1:], h)
    h[s1, s2, s3] = match1 or match2
    return h[s1, s2, s3]
    
    
s1 = "aabcc"
s2 = "dbbca"
 
s3 = "aadbbcbcac"
print solution(s1, s2, s3), 'should be True'
 
s3 = "aadbbbaccc"
print solution(s1, s2, s3), 'should be False'

s1 = 'aca'
s2 = 'db'

print solution(s1, s2, 'adbac'), 'should be False'    