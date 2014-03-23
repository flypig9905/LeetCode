'''

Given a string s and a dictionary of words dict, add spaces in s to construct a sentence where each word is a valid dictionary word.

Return all such possible sentences.

For example, given
s = "catsanddog",
dict = ["cat", "cats", "and", "sand", "dog"].

A solution is ["cats and dog", "cat sand dog"].

Created on Dec 28, 2013

@author: Songfan
'''
def wordBreak(s,d):
    assert(isinstance(s,str)),"input error"
    isTrue, result =  _wordBreak(s,d,{})
    if isTrue:
        return result

def _wordBreak(s,d,h):
    if s in d:
        return True, [s]
    if s in h:  # if word in map, return True and the value corresponding in map
        return True, h[s]
    for i in range(1,len(s)):
        s1 = s[:i]
        s2 = s[i:]
        # individually check the front part and end part, s1 and s2 is a list of words
        inDict1, s1List = _wordBreak(s1,d,h)    
        inDict2, s2List = _wordBreak(s2,d,h)
        if inDict1 and inDict2:
            for e1 in s1List:
                for e2 in s2List:
                    tmp = e1+' '+e2
                    if s in h:  # if word is the key to map 
                        if tmp not in h[s]:  # if tmp word is not in the list of h[s], just append the tmp word, CANNOT COMBINE WITH THE PREVIOUS IF STATEMENT
                            h[s].append(tmp)
                    else:   # else means word is not a key to map, init the list contains only the tmp word
                        h[s] = [tmp]
    if s in h:
        return True, h[s]
    else:
        return False, [s]
    

# unittest 1: pass
s = "catsanddog"
d = {"cat":1, "cats":1, "and":1, "sand":1, "dog":1}
print wordBreak(s, d)

s = 'abba'
d = {'ab':1,'ba':1,'a':1,'b':1}
print wordBreak(s, d)
