'''
Created on Nov 6, 2013

@author: Songfan
'''

# non-recursive implementation
def binarySearch(searchList, item):
    bottom = 0
    top = len(searchList)-1
    
    while bottom <= top:
        mid = (bottom+top)//2
        if searchList[mid]==item:
            return True
        else:
            if searchList[mid]<item:
                bottom = mid+1
            else:
                top = mid-1
    return False

def binarySerachRecursive(searchList, item):
    listLength = len(searchList)
    if listLength==0:
        return False
    else:
        mid = listLength//2
        if searchList[mid] == item:
            return True
        else:
            if searchList[mid] > item:
                return binarySerachRecursive(searchList[:mid], item)
            else:
                return binarySerachRecursive(searchList[mid+1:], item)
            
def bs(A,val):
    assert(isinstance(A,list)),'Input Error'
    aLen = len(A)
    if aLen == 0: return False
    mid = aLen // 2
    if val == A[mid]: return True
    elif val < A[mid]:
        return bs(A[:mid],val)
    else:
        return bs(A[mid+1:],val)
    


'''
exercise
'''
def bsIter(A, t):
    n = len(A)
    if n == 0: return False
    front, rear = 0, n-1
    while front <= rear:
        mid = (front+rear) // 2
        if A[mid] == t: 
            return True
        elif A[mid] < t: 
            front = mid+1
        else: 
            rear = mid-1
    return False

def bsRecur(A, t):
    n = len(A)
    return _bs(A, t, 0, n-1)

def _bs(A, t, front, rear):
    if front > rear: return False
    mid = (front+rear) // 2
    if A[mid] == t: 
        return True
    elif A[mid] < t:
        return _bs(A, t, mid+1, rear)
    else:
        return _bs(A, t, front, mid-1)
















A = []
item = 2
print binarySearch(A, item)
print binarySerachRecursive(A, item)
print bs(A,item)

A = [8]
item = 8
print binarySearch(A, item)
print binarySerachRecursive(A, item)
print bs(A,item)

A = [3]
item = 7
print binarySearch(A, item)
print binarySerachRecursive(A, item)
print bs(A,item)

A = [3,4,6,9]
item = 4
print binarySearch(A, item)
print binarySerachRecursive(A, item)
print bs(A,item)

A = [3,4,6,9,10]
item = 9
print binarySearch(A, item)
print binarySerachRecursive(A, item)
print bs(A,item)

A = [3,4,6,9,10]
item = 16
print binarySearch(A, item)
print binarySerachRecursive(A, item)
print bs(A,item)
print bsIter(A, item)
print bsRecur(A, item)

