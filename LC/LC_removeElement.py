'''
Given an array and a value, remove all instances of that value in place and return the new length.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Created on Jan 12, 2014

@author: Songfan
'''

''' thought: two pointer strategy, one is the running pointer, the other is the pointer that track the end 
of the modified list '''

def removeElement(A, e):
    n = len(A)
    if n == 0: return A, 0
    tail = 0
    for i in range(n):
        if A[i] !=  e:
            A[tail] = A[i]
            tail += 1
    return A[:tail], tail

''' unittest '''
A =[]
e = 5
print removeElement(A, e), ', should be ([], 0)'
            
A =[5]
e = 5
print removeElement(A, e), ', should be ([], 0)'

A =[1,5]
e = 5
print removeElement(A, e), ', should be ([1], 1)'

A =[5,1,5,2,5]
e = 5
print removeElement(A, e), ', should be ([1,2], 2)'