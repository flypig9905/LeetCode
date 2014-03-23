'''
Given two sorted integer arrays A and B, merge B into A as one sorted array.

Note:
You may assume that A has enough space to hold additional elements from B. The number of elements initialized in A and B are m and n respectively.

Created on Jan 2, 2014

@author: Songfan
'''

''' algorithm: two pointer each from the back of A and B, merge array from back to front '''

def mergeSortedArray(A, m, B, n):
    # assume correct input
    if m == 0: return B
    if n == 0: return A
    p1 = m - 1
    p2 = n - 1
    while(p1 >= 0 and p2 >= 0):
        ''' merge elements backwords from A and B '''
        if A[p1] >= B[p2]:
            ''' ALERT: back position should be p1+p2+1, since p1=m-1 p2=n-1 '''
            A[p1+p2+1] = A[p1]
            p1 -= 1
        else:
            A[p1+p2+1] = B[p2]
            p2 -= 1
    
    
    while(p2 >= 0):
        ''' if some element in B is not added to A, this means they are small elements and should be added now '''
        A[p2] = B[p2]
        p2 -= 1
    return A



A = [1,4,7,9,None,None,None,None]
B = [2,5,8]
m = 4
n = 3
Am = mergeSortedArray(A, m, B, n)
print [str(i) for i in Am]