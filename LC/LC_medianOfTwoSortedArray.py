'''
There are two sorted arrays A and B of size m and n respectively. Find the median of the two sorted arrays. 
The overall run time complexity should be O(log (m+n)).

Created on Dec 29, 2013

@author: Songfan
'''

''' (1). O(m+n) time, O(m+n) space Algorithm: merge sorted arrays, count the index '''

''' (2). if m=n, we cam use median comparing algorithm '''


''' (3). O(log(m+n)) time, O(1) space: median find; a variation of find k-th largest of two sorted array
len(A) = m, len(B) = n
partition A and B to A1, A2, B1, B2
if m//2+n//2+1 > k and A[m//2]>B[n//2], drop A2
if m//2+n//2+1 > k and A[m//2]<B[n//2], drop B2
if m//2+n//2+1 < k and A[m//2]>B[n//2], drop B1
if m//2+n//2+1 < k and A[m//2]<B[n//2], drop A1
'''

def find_median(A, B):
    m = len(A)
    n = len(B)
    k = (m+n) // 2
    if (m+n)%2 == 1:
        return find_med(A, 0, m-1, B, 0, n-1, k)
    else:
        return float(find_med(A, 0, m-1, B, 0, n-1, k) + find_med(A, 0, m-1, B, 0, n-1, k+1)) / 2.0

def find_med(A, st_a, ed_a, B, st_b, ed_b, k):
    if st_a >= ed_a: return B[k-1]
    if st_b >= ed_b: return A[k-1]
    if k <= 1: return min(A[st_a], B[st_b])
    md_a = (st_a+ed_a) // 2
    md_b = (st_b+ed_b) // 2
    if A[md_a] > B[md_b]:
        if md_a + md_b > k:
            return find_med(A, st_a, md_a, B, st_b, ed_b, k)   # drop A2
        else:
            return find_med(A, st_a, ed_a, B, md_b, ed_b, k-ed_b+st_b)   # drop B1
    else:
        if md_a + md_b > k:
            return find_med(A, st_a, ed_a, B, st_b, md_b, k)   # drop B2
        else:
            return find_med(A, md_a, ed_a, B, st_b, ed_b, k-ed_a+st_a)   # drop A1
            


 
a1 = [1,2,3]
a2 = [5,6,7,9]
print find_median(a1, a2)