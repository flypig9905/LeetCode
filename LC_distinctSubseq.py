'''

Given a string S and a string T, count the number of distinct subsequences of T in S.

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).

Here is an example:
S = "rabbbit", T = "rabbit"

Return 3.

Created on Feb 6, 2014

@author: Songfan
'''

''' 2d DP: let N[i][j] be the number of distinct subseq of T[:j] in S[:i]
    1. init
        N[0][j] = 0, because there cannot be any subseq of 'a' in ''
        N[i][0] = 1, because there is exactly 1 subseq of '' in 'abcd', i.e., delete all chars in 'abcd'
    2. if S[i] != T[j]:
        N[i][j] = N[i-1][j], since we are not getting any more options by acquiring S[i]
       else:
        N[i][j] = N[i-1][j-1] + N[i-1][j], we can choose to take S[i] into account, or we can ignore it and hope for any upcoming char will qulify this for subseq
'''

def solution(T, S):
    m = len(T)
    n = len(S)
    if m > n: return False
    if m == n: return S == T
    
    N = {}
    
    N[-1,-1] = 1    # the subseq of '' in ''    
    for i in range(n):
        N[i,-1] = 1
    for j in range(m):
        N[-1,j] = 0    # for index 0 to m-1
    
    for i in range(n):
        for j in range(m):
            if S[i] != T[j]:
                N[i,j] = N[i-1,j]
            else:
                N[i,j] = N[i-1,j-1] + N[i-1,j]
                
    return N[n-1,m-1]



S = "rabbbit"
T = "rabbit"
print solution(T, S) 