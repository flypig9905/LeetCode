'''
palindrome partitioning II

Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

For example, given s = "aab",
Return 1 since the palindrome partitioning ["aa","b"] could be produced using 1 cut.

Created on Dec 29, 2013

@author: Songfan
'''

''' DFS '''
class Solution:
    # @param s, a string
    # @return a list of lists of string
    def partition(self, s):
        result = []
        self.dfs(s, 0, [], result)
        return result
    
    def dfs(self, s, startIdx, currRes, result):
        n = len(s)
        if startIdx == n:
            result.append(currRes)
        for i in range(startIdx, n):
            tmpS = s[startIdx:i]
            if self.isParlin(tmpS):
                currRes.append(tmpS)
                self.dfs(s, startIdx + 1, currRes, result)
                currRes.pop()

    def isParlin(self, s):
        sLen = len(s)
        if sLen == 0:
            return False
        if sLen == 1:
            return True
        for i in range(0,sLen//2):
            if s[i] != s[-i-1]:
                return False
        return True


ss = Solution()
s = 'aabba'
print ss.partition(s)
s = 'abcd'
print ss.partition(s)


''' recursion + memoization: TLE '''
#def parlindromePartition2(s):
#    assert(isinstance(s,str)),'input error'
#    return _pp(s, {})
#
#def _pp(s, hCut):
#    sLen = len(s)
#    if sLen == 0:
#        return 0
#    if s in hCut:
#        return hCut[s]
#    if isParlin(s):
#        hCut[s] = 0
#        return 0
#    minCut = sLen
#    for i in range(1, sLen+1):
#        s1 = s[:i]
#        s2 = s[i:]
#        
#        curCut = _pp(s1, hCut) + _pp(s2, hCut)
#        if s not in hCut:
#            curMin = curCut + 1
#        else:
#            curMin = min(curCut, hCut[s]) + 1
#        
#        if minCut > curMin:
#            minCut = curMin
#            hCut[s] = minCut    # has to init hCut[s] in this way, otherwise stuck in infinite loop
#    return hCut[s]
#
#def isParlin(s):
#    sLen = len(s)
#    if sLen == 0:
#        return False
#    if sLen == 1:
#        return True
#    for i in range(0,sLen//2):
#        if s[i] != s[-i-1]:
#            return False
#    return True
#
#s = 'aabba'
#print parlindromePartition2(s)
#s = 'abcd'
#print parlindromePartition2(s)