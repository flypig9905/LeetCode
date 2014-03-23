'''

Given a set of distinct integers, S, return all possible subsets.

Note:
Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
For example,
If S = [1,2,3], a solution is:

[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

Created on Jan 12, 2014

@author: Songfan
'''

''' thought: recursion or DP'''

def subsetsRecur(A):
    # assume correct input
    return _subsetsRecur(A, len(A) - 1, {})

def _subsetsRecur(A, k, h):
    n = len(A)
    if n == 0: return []
    if n == 1: return [[],A]
    if k in h: return h[k]
    prevLists = _subsetsRecur(A[:k], k - 1, h)
    lastElem = A[k]
    tmpLists = prevLists[:]
    for L in prevLists:
        LCopy = L[:]
        LCopy.append(lastElem)
        if LCopy not in tmpLists:
            tmpLists.append(LCopy)
    h[k] = tmpLists
    return tmpLists

def subsetsDP(A):
    h = {}
    h[-1] = [[]]
    for i in range(len(A)):
        e = A[i]
        tmpLists = h[i-1]
        tmpListsCopy = tmpLists[:]
        for L in tmpLists:
            LCopy = L[:]
            LCopy.append(e)
            tmpListsCopy.append(LCopy)
        h[i] = tmpListsCopy
    return tmpListsCopy

A = [1, 2, 3]
res = subsetsRecur(A)
print 'recursive solution'
for i in res:
    print i

print 'DP solution'
res = subsetsDP(A)
for i in res:
    print i
    
    