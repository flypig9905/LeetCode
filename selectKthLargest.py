'''
Created on Mar 13, 2014

@author: Songfan
'''

'''
linear time selection
'''

def getByRank(A, rank):
    A.sort()
    return A[rank-1]

def selectKth(A, k):
    n = len(A)
    if n <= 5:
        return getByRank(A, k)
    # find median of medians
    medians = [getByRank(A[i:i+5], 3) for i in range(0, n-4, 5)]
    med = selectKth(medians, (len(medians)+1)//2)
    
    # partition
    L, R = [], []
    for a in A:
        if a < med: L.append(a)
        else: R.append(a)
    # recursive call
    if k <= len(L):
        return selectKth(L, k)
    else:
        return selectKth(R, k - len(L))
        
A = [21, 19, 20, 4, 5, 10, 14, 22, 23, 24, 11, 12, 16, 17, 18, 13, 15, 3, 1, 2, 6, 7, 9, 8]
rank = 15
print selectKth(A, rank)