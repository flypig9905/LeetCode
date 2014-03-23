'''
Created on Mar 13, 2014

@author: Songfan
'''

''' 
two pointer
'''

def union(A, B):
    na, nb = len(A), len(B)
    if na == 0: return B
    if nb == 0: return A
    pa, pb, result = 0, 0, []
    
    while pa < na and pb < nb:
        if A[pa] < B[pb]:
            result.append(A[pa])
            pa += 1
        elif A[pa] > B[pb]:
            result.append(B[pb])
            pb += 1
        else:
            result.append(A[pa])
            pa += 1
            pb += 1
            
    while pa < na:
        result.append(A[pa])
        pa += 1
    while pb < nb:
        result.append(B[pb])
        pb += 1
    return result

A = [1,3,4,5,7]
B = [2,3,5,6]
print union(A,B)