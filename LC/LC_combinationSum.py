'''
        Created on Feb 2, 2014
        
        @author: Songfan
        '''
        '''

Given a set of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

The same repeated number may be chosen from C unlimited number of times.

Note:
All numbers (including target) will be positive integers.
Elements in a combination (a1, a2, ... , ak) must be in non-descending order. (ie, a1 <= a2 <= ... <= ak).
The solution set must not contain duplicate combinations.
For example, given candidate set 2,3,6,7 and target 7, 
A solution set is: 
[7] 
[2, 2, 3] 

Created on Jan 26, 2014

@author: Songfan
'''
import copy
''' thought: DP '''
def solution1(C, t):  
    h = {}
    for k in range(1,t+1):
        if k in C:
            ''' items that is the solution themselves, ex: [7] in this case '''
            h[k] = [[k]]
        for c in C:
            if k - c in h:
                ''' check the previous item to see if them can achieve current k by addint any element in C'''
                tmp = copy.deepcopy(h[k-c])
                res = h.get(k,[])
                for t in tmp:
                    if c >= t[-1]:
                        ''' make sure ascending order '''
                        t.append(c)
                        res.append(t)
                h[k] = res
    return h[k]          
            
''' dfs '''
def solution2(C, t):
    result = []
    _dfs(C, t, [], result, 0)
    return result

def _dfs(C, t, intermediate, result, currVal):
    ''' intermediate: track the current solution
        result: store the final result
        currVal: make sure ascending order '''
    if t == 0: 
        ''' we have found a solution '''
        tmp = intermediate[:]
        result.append(tmp)
        return
    for c in C:
        if t < c: return
        if c >= currVal:
            ''' the number appended to intermediate solution has to be >= the current largest '''
            intermediate.append(c)
            _dfs(C, t - c, intermediate, result, c)
            ''' remember to pop back '''
            intermediate.pop()


''' thought: recursion + memoization '''
 
def solution3(C, t):
    if len(C) == 0: return
    return _comboSum(C, t, {})
 
def _comboSum(C, t, h):
    if t <= 0: return
    if t in h: return h[t]
    res = []
    if t in C:
        ''' this means [t] is a solution '''
        res.append([t])
    for c in C:
        prev = _comboSum(C, t - c, h)
        if prev:
            prevCopy = copy.deepcopy(prev)
            for item in prevCopy:
                if c >= item[-1]:
                    ''' ascending ordert '''
                    item.append(c)
                    res.append(item)
    h[t] = res
    return res
    
C = [2,3,6,7]
t = 7
print solution1(C,t)
print solution2(C,t)
print solution3(C,t)