'''

Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

For example,
If n = 4 and k = 2, a solution is:

[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

Created on Jan 12, 2014

@author: Songfan
'''
''' dfs '''
class Solution:
    # @return a list of lists of integers
    def combine(self, n, k):
        res = []
        self.dfs(n, k, 1, [], res)
        return res
    
    def dfs(self, n, k, startNum, intermediate, res):
        if k == 0: 
            res.append(intermediate[:])
            return
        for i in range(startNum, n+1):
            intermediate += [i]
            self.dfs(n, k-1, i+1, intermediate, res)
            intermediate.pop()


''' recur + memo'''
def combinations(n, k):
    assert(n >= k),'input error'
    return _combo(n, k, {})

def _combo(n, k, h):
    if k == 0: return []
    if k == 1: 
        res = []
        for i in range(1, n + 1):
            res.append([i])
        return res
    if k in h: return h[k]
    prevList = _combo(n, k - 1, h)
    res = []
    for L in prevList:
        maxElem = L[-1]
        for i in range(maxElem + 1, n + 1):
            tmp = L[:]
            tmp.append(i)
            if tmp not in res:
                res.append(tmp)
    h[k] = res
    return res


''' DP solution '''
def combinationsDP(n, k):
    assert(n >= k),'input error'
    h = {}
    if k == 0: return []
    res = []
    for i in range(1, n + 1):
        res.append([i])
    h[1] = res
    for i in range(2,k+1):
        prevList = h[i-1]
        res = []
        for L in prevList:
            maxElem = L[-1]
            for j in range(maxElem + 1, n + 1):
                tmp = L[:]
                tmp.append(j)
                if tmp not in res:
                    res.append(tmp)
        h[i] = res
    return h[k]
    

ss = Solution()
print ss.combine(4,2)
print combinations(4,2)
print combinationsDP(4,2)