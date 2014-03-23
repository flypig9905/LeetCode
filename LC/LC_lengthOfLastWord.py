'''

Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

For example, 
Given s = "Hello World",
return 5.

Created on Feb 12, 2014

@author: Songfan
'''

''' have a ptr track the position of last space '''
class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
        n = len(s)
        if n == 0: return 0
        ptrRear = n
        hasWord = False
        i = n - 1
        while i >= 0:
            if s[i] != ' ':
                hasWord = True
                if ptrRear == n:
                    ptrRear = i
            elif s[i] == ' ' and hasWord:
                break
            i -= 1
        
        if hasWord:
            return ptrRear - i
        else:
            return 0
        
ss = Solution()
print ss.lengthOfLastWord('ab bc'),'should be 2'
print ss.lengthOfLastWord('ab bc '),'should be 2'
print ss.lengthOfLastWord('abbc'),'should be 4'



