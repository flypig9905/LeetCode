'''

Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:
Elements in a quadruplet (a,b,c,d) must be in non-descending order. (ie, a <= b <= c <= d)
The solution set must not contain duplicate quadruplets.
    For example, given array S = {1 0 -1 0 -2 2}, and target = 0.

    A solution set is:
    (-1,  0, 0, 1)
    (-2, -1, 1, 2)
    (-2,  0, 0, 2)

Created on Jan 31, 2014

@author: Songfan
'''

''' if use the same method as 3sum, that is O(N^3), we can use similar method as 2sum, calculate the sum of every pair, store their indecis in a map, 
( with the sum as their key) then, run through the map and check if negative key exists, if exist, sort the order of the list, O(N^2logN) '''

def solution(A):
    n = len(A)
    if n <= 4: return False
    h = {}
    for i in range(n):
        for j in range(i + 1, n):
            tmpSum = A[i] + A[j]
            tmpCombo = h.get(tmpSum, [])
            tmpCombo.append((i,j))
            h[tmpSum] = tmpCombo
    
    res = []
    for k in h:
        if -k in h:
            if k == 0:
                n = len(h[0])
                for i in range(n):
                    for j in range(i + 1, n):
                        idx = [h[0][i][0],h[0][i][1],h[0][j][0],h[0][j][1]]
                        ''' this means the duplicate number have been pick '''
                        if len(set(idx)) < 4: continue
                        r = [A[m] for m in idx]
                        r = sorted(r)
                        if r not in res: res.append(r)
            else:
                n1 = len(h[k])
                n2 = len(h[-k])
                for i in range(n1):
                    for j in range(n2):
                        idx = [h[k][i][0],h[k][i][1],h[-k][j][0],h[-k][j][1]]
                        if len(set(idx)) < 4: continue
                        r = [A[m] for m in idx]
                        r = sorted(r)
                        if r not in res: res.append(r)

    return res
            
A = [1, 0, -1, 0, -2, 2]
print solution(A)
            
            