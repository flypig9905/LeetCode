'''

Given a number represented as an array of digits, plus one to the number.

Created on Feb 3, 2014

@author: Songfan
'''

def solution(A):
    n = len(A)
    if n == 0: return A
    A.insert(0, 0)  # dummy position
    carry = 1
    i = n
    while i >= 0:
        tmp = A[i] + carry
        A[i] = tmp % 10
        carry = tmp // 10
        i -= 1
        
    if A[0] == 0: A.pop(0)
    return A

A = [1,2,3]
print solution(A), 'should be [1,2,4]'

A = [1]
print solution(A), 'should be [2]'

A = [9,9]
print solution(A), 'should be [1,0,0]'    