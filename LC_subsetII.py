'''

Given a collection of integers that might contain duplicates, S, return all possible subsets.

Note:
Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
For example,
If S = [1,2,2], a solution is:

[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]

Created on Feb 4, 2014

@author: Songfan
'''

''' similar algorithm as 'subsetI', recursion + memoization check duplication '''
def solution(S):
    return subset(S, {})

def subset(S, h):
    n = len(S)
    if n == 0: return [[]]
    sk = tuple(S)
    if sk in h: return h[sk]
    
    ''' pick the last element and recursion '''
    prevRes = subset(S[:-1], h)
    res = prevRes[:]
    for s in prevRes:
        tmp = s[:]
        tmp.append(S[-1])
        if tmp not in res:
            res.append(tmp)
    
    return res

S = [1,2,2]
print solution(S)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    


