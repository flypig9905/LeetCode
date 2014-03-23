'''

Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Here are few examples.
[1,3,5,6], 5 -> 2
[1,3,5,6], 2 -> 1
[1,3,5,6], 7 -> 4
[1,3,5,6], 0 -> 0

Created on Feb 1, 2014

@author: Songfan
'''

''' binary search, be careful with the equal sign in 'while first <= last' '''


def search(A, k):
    n = len(A)
    if n == 0: return 0
    first = 0
    last = n - 1
    while first <= last:
        mid = first + (last - first) / 2
        if A[mid] == k:
            return mid
        if A[mid] < k:
            first = mid + 1
        else:
            last = mid - 1
    return first
    
A = [1,3,5,6]
print search(A, 5), 'should be 2'
A = [1,3,5,6]
print search(A, 2), 'should be 1'
A = [1,3,5,6]
print search(A, 7), 'should be 4'
A = [1,3,5,6]
print search(A, 0), 'should be 0'
A = [1,3,4,5,6]
print search(A, 1), 'should be 0'






