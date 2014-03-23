'''

Given two words word1 and word2, find the minimum number of steps required to convert word1 to word2. (each operation is counted as 1 step.)

You have the following 3 operations permitted on a word:

a) Insert a character
b) Delete a character
c) Replace a character

Created on Jan 27, 2014

@author: Songfan
'''

''' algorithm: 
        h[i,j] represents the edit distance of word1[0...i-1] and word2[0...j-1] 
        init: h[i,0] = i, h[0,i] = i, i = 0 means edit distance of empty string '' to another word, then the ops needed equals the length of the other word
        DP requirement:
            if word1[i-1] == word2[j-1]: h[i,j] = h[i-1,j-1], since we don't need edit anything if the last char of each word is the same
            else: h[i,j] = 1 + min(h[i-1,j], h[i,j-1], h[i-1,j-1]),
                h[i,j-1]: insert the last char of word2 to the tail of word1. The edit distance is the same as 1 + edit word1[1...i-1] and word2[1...j-2]
                h[i-1,j]: delete the last char of word1. The edit distance is the same as 1 + edit word1[1...i-2] and word2[1...j-1]
                h[i-1,j-1]: replace the last char of word1 to the last char of word2. The edit distance is the same as 1 + edit word1[1...i-2] and word2[1...j-2]
                
'''
def editDist(w1, w2):
    h = {}
    n1 = len(w1)
    n2 = len(w2)
    for i in range(n1 + 1):
        ''' be careful with the index '''
        h[i, 0] = i
    for j in range(n2 + 1):
        h[0, j] = j

    for i in range(1, n1 + 1):
        for j in range(1, n2 + 1):
            ''' be careful with the index '''
            if w1[i - 1] == w2[j - 1]:
                h[i, j] = h[i - 1, j - 1]
            else:
                h[i, j] = 1 + min(h[i, j-1], h[i-1, j], h[i-1, j-1])
    return h[n1, n2]

''' memoization '''
def solution2(w1, w2):
    return _mem(w1, w2, len(w1), len(w2), {})

def _mem(w1, w2, k, l, h):
    if k == 0: return l
    if l == 0: return k
    if (k, l) in h: return h[k, l]
    if w1[k - 1] == w2[l - 1]:
        h[k, l] = _mem(w1, w2, k - 1, l - 1, h)
    else:
        h[k, l] = 1 + min(_mem(w1, w2, k - 1, l, h), _mem(w1, w2, k, l - 1, h), _mem(w1, w2, k - 1, l - 1, h))
    return h[k, l]
    
    
    

w1 = 'cat'
w2 = 'hat'
print editDist(w1, w2)
print solution2(w1, w2)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    