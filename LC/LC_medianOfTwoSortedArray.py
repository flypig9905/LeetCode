'''
There are two sorted arrays A and B of size m and n respectively. Find the median of the two sorted arrays. 
The overall run time complexity should be O(log (m+n)).

Created on Dec 29, 2013

@author: Songfan
'''

''' (1). O(m+n) time, O(m+n) space Algorithm: merge sorted arrays, count the index '''

''' (2). if m=n, we cam use median comparing algorithm '''


''' (3). O(log(m+n)) time, O(1) space: median find '''
''' ref: http://www.geeksforgeeks.org/median-of-two-sorted-arrays/ '''
''' ref: http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-046j-introduction-to-algorithms-sma-5503-fall-2005/assignments/ps9sol.pdf '''
import math

# def findMedian(A, B):
#     # assume correct input
#     l = len(A)
#     m = len(B)
#     n = m + l
#     h = math.ceil(n/2)
#     if 
#     return medianSearch(A, B, max(1, h - m), min(l, h))
# 
# def medianSearch(A, B, left, right):
#     if left > right:
#         return medianSearch(A, B, left, right)
#     if m == 0:
#         return B[k-1]
#     if (k==1)
#     
#         
# a1 = [1,2,3]
# a2 = [5,6,7,9]
# findMedian(a2, Ba1)