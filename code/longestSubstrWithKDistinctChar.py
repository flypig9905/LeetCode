'''
find the longest substring which contains k distinct words


Created on Mar 23, 2014

@author: Songfan
'''

'''
two pointer + hashtable

increase front ptr,
    update hashtable
    if hashtable contains less than or equal to 2 distinct words
        update longest substring
    while hashtable contains more than 2 distinct words
        increase rear ptr
        update hashtable
        
'''

def substrWithDistinctWords(s, k):
    n = len(s)
    if n <= k: return s # for string with length less than k, it has to satisfy
    front, rear, h, substr = 0, 0, {}, ''
    
    while front < n:
        h[s[front]] = h.get(s[front],0) + 1
        if len(h.keys()) <= 2:
            if len(substr) < front-rear+1:
                substr = s[rear:front+1]
        front += 1
        while len(h.keys()) > 2:
            tmpChar = s[rear]
            rear += 1
            h[tmpChar] -= 1
            if h[tmpChar] == 0: h.pop(tmpChar)
            
    return substr

s = 'abcbcbcbcbcddd'
print substrWithDistinctWords(s, 2), 'should be bcbcbcbcbc'
s = 'abbbcccbbbcccd'
print substrWithDistinctWords(s, 2), 'should be bbbcccbbbccc'
