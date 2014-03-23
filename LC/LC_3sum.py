'''
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:
Elements in a triplet (a,b,c) must be in non-descending order. (ie, a <= b <= c)
The solution set must not contain duplicate triplets.
    For example, given array S = {-1 0 1 2 -1 -4},

    A solution set is:
    (-1, 0, 1)
    (-1, -1, 2)


Created on Dec 30, 2013

@author: Songfan
'''


''' algorithm O(N^2): first sort the array, then have two pointers moving from the head and tail of list '''
def sum3(A):
    A = sorted(A)
    n = len(A)
    result = []
    for i in range(n - 1):
        j = i + 1
        k = n - 1
        while j < k:
            curSum = A[i] + A[j] + A[k]
            if curSum == 0:
                ''' alert: need to seperate the if statement and update both j and k '''
                if (A[i],A[j],A[k]) not in result:
                    result.append((A[i], A[j], A[k]))                    
                j += 1
                k -= 1
            elif curSum < 0:
                j += 1
            elif curSum > 0:
                k -= 1
     
    return result

''' two hash table, one stores index of sum of 1 element (which is themselves), one stores indices of sum of 2 element
    then, for every key k in h1, find if -k in h2 
    
    O(N^2logN)
    
    '''
def solution2(A):
    n = len(A)
    if n < 3: return None
    h1 = {}
    h2 = {}
    for i in range(n):
        # store element in h1
        tmp = h1.get(A[i], [])
        tmp.append(i)
        h1[A[i]] = tmp
        
        # store pairs in h2
        for j in range(i + 1, n):
            tmp = h2.get(A[i] + A[j], [])
            tmp.append((i,j))
            h2[A[i] + A[j]] = tmp
    
    res = []
    for k in h1:
        if -k in h2:
            for i in h1[k]:
                for j in h2[-k]:
                    idx = [i, j[0], j[1]]
                    if len(set(idx)) < 3: continue
                    r = [A[m] for m in idx]
                    r = sorted(r)
                    if r not in res: res.append(r)
    return res


A = [-1, 0, 1, 2, -1, -4]
print sum3(A)
print solution2(A)
