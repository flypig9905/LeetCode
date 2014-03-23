'''
Created on Mar 13, 2014

@author: Songfan
'''
'''
two pointer, similar to union
'''

def intersect(A, B):
    na, nb = len(A), len(B)
    if na == 0 or nb == 0: return []
    pa, pb, result = 0, 0, []
    while pa < na and pb < nb:
        if A[pa] == B[pb]:
            result.append(A[pa])
            pa += 1
            pb += 1
        elif A[pa] < B[pb]: pa += 1
        else: pb += 1
        
    return result

A = [1,3,4,5,7]
B = [2,3,5,6]
print intersect(A,B)