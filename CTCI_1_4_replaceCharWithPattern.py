'''
CTCI P73 1-4
Replace all space in a string with '%20', assuming sufficient space to hold the string after modification, and 'true' length of the stirng is known

Created on Nov 20, 2013

@author: Songfan
'''
''' thought: find position of char that needs to be replaced. Then work from end to front '''

import unittest
def replaceCharWithPattern(s, sLen, c, pattern):
    if(isinstance(s, basestring) and sLen>0 and isinstance(pattern, basestring)):
        pLen = len(pattern)
        patternPosition = []
        for i in range(sLen):
            if(s[i]==c):
                patternPosition.append(i)
        patternPtr = len(patternPosition)
        if patternPtr==0:
            return
        patternPtr -= 1
        # assume pattern length > 1
        s = list(s)
        p = list(pattern)
        for i in range(sLen-1, -1, -1):
            if patternPtr>=0 and i<patternPosition[patternPtr]:
                patternPtr -= 1
            if i>patternPosition[patternPtr]:
                offset = (patternPtr+1)*(pLen-1)
                s[i+offset] = s[i]
            elif i==patternPosition[patternPtr]:
                offset = (pLen-1)*patternPtr
                s[i+offset:i+offset+pLen] = p
        s = "".join(s)
        return s
        
s = 'Mr John Smith    '
sLen = 13
c = ' '
pattern = '%'

s = 'aa bb  '
sLen = 5
c = ' '
pattern = '20%'

s = replaceCharWithPattern(s, sLen, c, pattern)
print s

# class testReplaceCharWithPattern(unittest.TestCase):
#     def testNonStringInput(self):
#         self.assertEqual(replaceCharWithPattern(s,sLen,c,pattern), 'aa220%bb')
# 
# unittest.main()