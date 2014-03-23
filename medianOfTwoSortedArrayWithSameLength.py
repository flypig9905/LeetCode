'''
Created on Mar 13, 2014

@author: Songfan
'''

'''
Divide and conquer, compare the median of each array
'''

def med(A, B):
    na = len(A)
    nb = len(B)
    if na == 0 and nb == 0: return
    return findMed(A, 0, na-1, B, 0, nb-1)

def findMed(A, aFront, aRear, B, bFront, bRear):
    if aFront == aRear:
        return float(A[aFront] + B[bFront]) / 2.0
    aMid = (aFront + aRear + 1) // 2
    bMid = (bFront + bRear + 1) // 2
    if A[aMid] == B[bMid]: return A[aFront]
    elif A[aMid] < B[bMid]:
        return findMed(A, aMid, aRear, B, bFront, bMid)
    else:
        return findMed(A, aFront, aMid, B, bMid, bRear)
    
A = [1,3,6,7,9]
B = [2,4,5,8,9]
print med(A, B)