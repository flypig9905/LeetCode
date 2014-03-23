'''
Created on Nov 14, 2013

@author: Songfan
'''

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