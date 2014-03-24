'''

Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

Each number in C may only be used once in the combination.

Note:
All numbers (including target) will be positive integers.
Elements in a combination (a1, a2, ... , ak) must be in non-descending order. (ie, a1 <= a2 <= ... <= ak).
The solution set must not contain duplicate combinations.
For example, given candidate set 10,1,2,7,6,1,5 and target 8, 
A solution set is: 
[1, 7] 
[1, 2, 5] 
[2, 6] 
[1, 1, 6] 

Created on Feb 2, 2014

@author: Songfan
'''

''' sort + dfs '''
def solution(A, t):
    n = len(A)
    if n == 0: return []
    ''' sort the array and we can prune the search procedure '''
    A = sorted(A)
    ''' Awesome trick, bow down to myself:) : to track which element is used next '''
    nextIdx = 0 
    res = []
    _dfs(A, t, [], res, nextIdx)
    return res

def _dfs(pool, target, currRes, res, nextIdx):
    if target == 0:
        tmp = currRes[:]
        if tmp not in res: res.append(tmp)
        return
    n = len(pool)
    if nextIdx == n: return
    if target < pool[nextIdx]: return   # pruning
    
    for i in range(nextIdx, n):
        currRes.append(pool[i])
        ''' we are force to choose element from index i+1, therefore, non-decreasing order is forced '''
        _dfs(pool, target - pool[i], currRes, res, i + 1)
        currRes.pop()
    return
    
    
A = [10,1,2,7,6,1,5]
t = 8
print solution(A, t)