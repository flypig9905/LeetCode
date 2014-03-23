'''

Given a string S, find the longest palindromic substring in S. 
You may assume that the maximum length of S is 1000, and there exists one unique longest palindromic substring.

Created on Jan 31, 2014

@author: Songfan
'''

''' classic problem, multiple solutions '''

''' solution1 O(N^2): consider each char as the center, expand to both sides (Notice there are 2N-1 center, since 'b' and 'bb' are both center)
        Therefore, during linear scan, one consider only one letter as center, the other consider two letter '''

def solution1(S):
    n = len(S)
    if n == 0 or n == 1: return n
    
    longest = S[0]
    
    for i in range(1, n - 1):
        ''' one char case '''
        tmp1 = expand(S, i, i)
        if len(tmp1) > len(longest):
            longest = tmp1
            
        ''' two char case '''
        tmp2 = expand(S, i, i + 1)
        if len(tmp2) > len(longest):
            longest = tmp2
    
    return longest
        
        
def expand(S, left, right):
    while left >= 0 and right < len(S) and S[left] == S[right]:
        left -= 1
        right += 1
    return S[left + 1:right]
                                                           
''' solution 2 O(N): 
    http://leetcode.com/2011/11/longest-palindromic-substring-part-ii.html
    http://www.felix021.com/blog/read.php?2040 
    discuss with LJ

'''                                                        
                                                           
S = 'abacdfgdcaba'
print solution1(S), 'should be aba'