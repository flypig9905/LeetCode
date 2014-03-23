'''
CTCI 11-3 find an element from a rotated sorted array

Created on Dec 7, 2013

@author: Songfan
'''
""" not correct, need to check with answer
def _findHelper(A,v,first,last):
    while(first<last):
        mid = (first+last)//2
        if A[mid]==v:
            return mid
        elif (A[first]<v and A[last]<v) or (A[first]>v and A[last]>v):
            result1 = _findHelper(A,v,first,mid)
            result2 = _findHelper(A,v,mid,last)
            if result1: return result1
            if result2: return result2
        elif A[first]<v:
            last = mid
        elif A[last]>v:
            first = mid+1
        else:
            return False
    return False
    
    

def findFromRotatedArray(A,v):
    assert(isinstance(A,list)),'error'
    return _findHelper(A,v,0,len(A)-1)

# A = [15,16,19,20,25,1,3,4,5,7,10,13,14]
# v = 5
# print findFromRotatedArray(A,v)

A = [2,2,2,3,4,1,2]
v = 1
print findFromRotatedArray(A,v)