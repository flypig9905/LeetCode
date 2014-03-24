'''

A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given an encoded message containing digits, determine the total number of ways to decode it.

For example,
Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).

The number of ways decoding "12" is 2.

Created on Jan 13, 2014

@author: Songfan
'''

''' thought: DP or recursion'''

class Solution:
    # @param s, a string
    # @return an integer
    def numDecodings(self, s):
        n = len(s)
        if n == 0 or s[0] == '0': return 0
        if n == 1: return self.checkChar(s[0])
        prevPrev = self.checkChar(s[0])
        prev = prevPrev * self.checkChar(s[1]) + self.checkChar2(s[0], s[1])
        
        for i in range(2,n):
            tmp = 0
            if self.checkChar(s[i]): tmp += prev
            if self.checkChar2(s[i-1], s[i]): tmp += prevPrev
            prevPrev = prev
            prev = tmp
            
        return prev

    def checkChar(self, c):
        if int(c) >= 1 and int(c) <= 9: return 1
        else: return 0
    
    def checkChar2(self, c1, c2):
        if (int(c1) == 1 and int(c2) >= 0 and int(c2) <= 9) or \
            (int(c1) == 2 and int(c2) >= 0 and int(c2) <= 6):
            return 1
        else:
            return 0

    



''' unittest '''
ss = Solution()
print ss.numDecodings('12'), 'should be 2'
print ss.numDecodings('110'), 'shoule be 1'
print ss.numDecodings('1212'), 'should be 5'
