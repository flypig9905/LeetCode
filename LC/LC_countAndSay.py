'''

The count-and-say sequence is the sequence of integers beginning as follows:
1, 11, 21, 1211, 111221, ...

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth sequence.

Note: The sequence of integers will be represented as a string.

Created on Feb 2, 2014

@author: Songfan
'''

def solution(N):
    if N < 1: return ''
    if N == 1: return '1'
    currSeq = '1'
    for _ in range(1, N):
        currSeq = cas(currSeq)
    return currSeq

def cas(seq):
    n = len(seq)
    prevChar = seq[0]
    cnt, idx, res = 0, 0, ''

    while idx <= n:
        if idx == n:
            res += str(cnt)+str(prevChar)
        elif prevChar == seq[idx]:
            cnt += 1
        else:
            res += str(cnt)+str(prevChar)
            cnt = 1
            prevChar = seq[idx]
        idx += 1
    return res
            
print solution(1), 'should be 1'
print solution(2), 'should be 11'
print solution(3), 'should be 21'
print solution(4), 'should be 1211'
print solution(5), 'should be 111221'
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
             
    