'''

Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

For example,
S = "ADOBECODEBANC"
T = "ABC"
Minimum window is "BANC".

Note:
If there is no such window in S that covers all characters in T, return the emtpy string "".

If there are multiple such windows, you are guaranteed that there will always be only one unique minimum window in S.

Created on Feb 4, 2014

@author: Songfan
'''
''' two hashtable: has found, need to find
   +two pointer:   one front, one back
    needNum: track if all the chars need are found. 
    
    algorithm: Move back ptr and record hasFound and needNum. If char needed are all found, we increase front while maintaining the status that all chars are found. Store the length 
    to the global var minWindow.
   
'''

def solution(S, T):
    m = len(T)
    n = len(S)
    if m > n or n == 0: return ''
    
    needToFind = {}
    needNum = 0
    hasFound = {}
    for s in T:
        needToFind[s] = needToFind.get(s, 0) + 1
        needNum += 1
    
    front = 0
    back = 0
    minWindow = n
    minWindowChars = T
    while back < n:
        s = S[back]
        if s not in needToFind:
            ''' skip chars that are not in T '''
            back += 1
            continue
        
        hasFound[s] = hasFound.get(s, 0) + 1
        if hasFound[s] <= needToFind[s]:
            needNum -= 1
        
        if needNum == 0:
            ''' means we have get all the chars in T, check to see if we can increase the front pointer '''
            # ignore chars not need to find
            while S[front] not in needToFind or \
                    S[front] in hasFound and S[front] in needToFind and hasFound[S[front]] > needToFind[S[front]]:
                
                if S[front] in hasFound and S[front] in needToFind and hasFound[S[front]] > needToFind[S[front]]:
                    hasFound[S[front]] -= 1
                front += 1
            
            ''' record current min '''
            if minWindow > back - front + 1:
                minWindowChars = S[front:back+1]
                minWindow = back - front + 1
            
        back += 1
    if needNum > 0:
        return ''
    else:
        return minWindowChars
        
S = "ADOBECODEBANC"
T = "ABC"
print solution(S, T)
             
    
    
    
    
    
    