'''
Linear time selection

select the k-th largest

Created on Apr 5, 2014

@author: Songfan
'''
import timeit

# def by_med(A):
#     A.sort()
#     return A[len(A)//2]
# 
# def partition(A):
#     n = len(A)
#     if n < 5:
#         pi = by_med(A)
#     else:
#         ''' median of median as pivot '''
#         meds = [by_med(A[i:i+5]) for i in range(0,n-4,5)]
#         pi = by_med(meds)
#     A.remove(pi)
#     lo = [x for x in A if x <= pi]
#     hi = [x for x in A if x > pi]
#     return pi, lo, hi

def partition(A):
    ''' first element as pivot '''
    pi, seq = A[0], A[1:]
    lo = [x for x in seq if x <= pi]
    hi = [x for x in seq if x > pi]
    return pi, lo, hi

def select(A, k):
    pi, lo, hi = partition(A)
    n = len(lo)
    if k == n: return pi
    elif k < n: return select(lo, k)
    else: return select(hi, k-n-1)
    
''' unittest '''
A = [3,2,5,4,1,6,7]
st = timeit.default_timer()
print select(A, 1), 'should be 1'
print 'time: ', timeit.default_timer() - st

st = timeit.default_timer()
print select(A, 3), 'should be 3'
print 'time: ', timeit.default_timer() - st
    
    