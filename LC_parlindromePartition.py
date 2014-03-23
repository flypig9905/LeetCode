'''
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

For example, given s = "aab",
Return

  [
    ["aa","b"],
    ["a","a","b"]
  ]

Created on Dec 28, 2013

@author: Songfan
'''

''' thought: recursion '''
class Solution:
    # @param s, a string
    # @return a list of lists of string
    def partition(self, s):
        return self._pp(s,{})


    def _pp(self, s, h):
        if not s:   # this base case matters, we want to take care the case where s is a parlindrome itself, 'aba' = 'aba' + ''
            return [[]]
        if len(s) == 1:
            return [[s]]    # be careful with the list of list data structure
        if s in h:
            return h[s]
        for i in range(1,len(s)+1):
            s1 = s[:i]
            s2 = s[i:]
            s1List = self._pp(s1,h)
            s2List = self._pp(s2,h)
            ''' caveat, add the parlindrome string to the list '''
            if self.isParlin(s1) and [s1] not in s1List:
                s1List.append([s1])
            if self.isParlin(s2) and [s2] not in s2List:
                s2List.append([s2])
            
            # combine elements in the both list
            for e1 in s1List:
                for e2 in s2List:
                    tmp = e1[:]
                    tmp.extend(e2)
                    if s in h:
                        if tmp not in h[s]:
                            h[s].append(tmp)
                    else:
                        h[s] = [tmp]
        return h[s]

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

''' unittest: isPalin '''
# all pass
# s = 'a'
# print isPalin(s)
# s = 'aba'
# print isPalin(s)
# s = 'abab'
# print isPalin(s)
 
''' unittest parlindromePart '''
s = 'aabb'
ss = Solution()
print ss.partition(s)
    
    
    
    
    