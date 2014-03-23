'''
Created on Nov 4, 2013

@author: Songfan
'''
def reverseString(s):
    if not s:
        return ""
    else:
        return reverseString(s[1:])+s[0]
    

print reverseString('I am a boy')