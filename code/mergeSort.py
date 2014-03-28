'''
Created on Nov 14, 2013

@author: Songfan
'''
''' a better implementation '''
def merge_sort(A):
    mid = len(A) // 2
    left, right = A[:mid], A[mid:]
    if len(left) > 1: left = merge_sort(left)   # recursive call
    if len(right) > 1: right = merge_sort(right)
    res = []
    while left and right:
        if left[-1] >= right[-1]:   # take larger element, and append it to res, elegent implementation
            res.append(left.pop())
        else:
            res.append(right.pop())
    res.reverse()   # remember to reverse this
    return (left or right) + res    # either left or right is empty list, use or to avoid complex code

''' so so implementation '''

def merge(s1,s2):
    assert(s1 and s2 and len(s1)>=0 and len(s2)>=0), "Bad Input"
    i = 0
    j = 0
    result = []
    while(i<len(s1) and j<len(s2)):
        if s1[i]<=s2[j]:
            result.append(s1[i])
            i+=1
        else:
            result.append(s2[j])
            j+=1
    if i!=len(s1):
        result += s1[i:]
    elif j!=len(s2):
        result += s2[j:]
    return result
            
    

def mergeSort(A):
    if len(A)<=1:
        return A
    else:
        mid = len(A)//2
        left = mergeSort(A[:mid])
        right = mergeSort(A[mid:])
        result = merge(left,right)
        return result
    
    
A = [1,5,7,2,5,9,8,1]
# aList = 'abcidkels'
print mergeSort(A)
print merge_sort(A)