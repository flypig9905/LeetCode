'''

Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Created on Jan 24, 2014

@author: Songfan
'''

''' algorithm:
    if current item == target item: return
    elif first item < current item:
        if first item < target item < current item: search left
        else: search right
    else:
        if current item < target item < last item: search right
        else: search left
'''
def findItem(A, e):
    n = len(A)
    if n == 0: return -1
    left = 0
    right = n - 1
    while left <= right:
        mid = (left + right) // 2
        if A[mid] == e: return mid
        ''' caveat: compare A[left] to A[mid] '''
        if A[left] <= A[mid]: 
            if A[left] <= e and e < A[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if A[mid] < e and e <= A[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1
    
A = [4, 5, 6, 7, 0, 1, 2]         
e = 3
print findItem(A, e), 'should be -1'

e = 5
print findItem(A, e), 'should be 1'

e = 1
print findItem(A, e), 'should be 5'

e = 4
print findItem(A, e), 'should be 0'

e = 2
print findItem(A, e), 'should be 6'




# 
# ''' thought: there is no duplicates, we can safely use binary search, 
#     if current item == target item: return
#     elif current item < target item: 
#         if left item > target item, target is not in left, search right
#         elif right item < target item, target is not in right, search left
#         else: should search both sides
#     else (current item > target item): 
#         if left item > target item, target is not in left, search right
#         if right item > target item, target is not in right, search left
#         else: should search both sides
# '''


# 
# def findIn(A, e):
#     # assume correct input
#     return _find(A, e, 0, len(A) - 1)
# 
# def _find(A, e, left, right):
#     n = len(A)
#     if n == 0 or left > right: return -1
#     mid = (left + right) // 2
#     if A[mid] == e: return mid
#     elif A[mid] < e:
#         if A[left] > e: return _find(A, e, mid + 1, right)
#         elif A[right] < e: return _find(A, e, left, mid - 1)
#         else: return max(_find(A, e, left, mid - 1), _find(A, e,mid + 1, right))
#     else:
#         if A[left] > e: return _find(A, e, mid + 1, right)
#         elif A[right] > e: return _find(A, e, left, mid - 1)
#         else: return max(_find(A, e, left, mid - 1), _find(A, e,mid + 1, right))
#             
#             
#             
#             
# print 'method 2, my implementation, not very efficient'
# e = 3
# print findIn(A, e), 'should be -1'
# 
# e = 5
# print findIn(A, e), 'should be 1'
# 
# e = 1
# print findIn(A, e), 'should be 5'
# 
# e = 4
# print findIn(A, e), 'should be 0'
# 
# e = 2
# print findIn(A, e), 'should be 6'
#             
#             
#             
#             
#             
            