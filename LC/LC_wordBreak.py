'''
Given a string s and a dictionary of words dict, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

For example, given
s = "leetcode",
dict = ["leet", "code"].

Return true because "leetcode" can be segmented as "leet code".

Created on Dec 28, 2013

@author: Songfan
'''
import time

def wordBreak(s,d):
    assert(isinstance(s,str)),'input error'
    if s in d:
        return True
    for i in range(len(s)):
        if s[:i] in d and wordBreak(s[i:],d):
            return True
    return False

def wordBreakDP(s,d):
    assert(isinstance(s,str)),'input error'
    return _wordBreakDP(s,d,{})

def _wordBreakDP(s,d,h):
    if s in d:
        return True
    if s in h:
        return h[s]
    for i in range(1,len(s)):
        s1 = s[:i]
        s2 = s[i:]
        h[s] = _wordBreakDP(s1,d,h) and _wordBreakDP(s2,d,h)
    
    # s could end up being not a key of h
    if s in h:
        return h[s]
    else:
        return False

''' unit test '''
# s = 'iloveleetcode'
# d = {}
# d['leet'] = 1
# d['code'] = 1
# d['i'] = 1
# d['love'] = 1
# print wordBreak(s,d)

# test 2
s = 'a'*20+'b'+'a'*20
d = {"a":1,"aa":1,"aaa":1,"aaaa":1,"aaaaa":1,"aaaaaa":1,"aaaaaaa":1,"aaaaaaaa":1,"aaaaaaaaa":1,"aaaaaaaaaa":1}

st = time.time()
print wordBreak(s,d)
print 'non-DP:',time.time() - st,'seconds'

st = time.time()
print wordBreakDP(s,d)
print 'DP:',time.time() - st,'seconds'