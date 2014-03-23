'''
Created on Nov 4, 2013

@author: Songfan
'''
def checkPalindrome(s):
    s = "".join(s.lower().split(" "))
    if len(s)<=1:
        return True
    else:
        return s[0]==s[-1] and checkPalindrome(s[1:-1])

print checkPalindrome('kayak')
print checkPalindrome('Live not on evil')
print checkPalindrome('Live')
print "".split(" ")