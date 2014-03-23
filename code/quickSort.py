'''
Created on Dec 6, 2013

@author: Songfan
'''
def _quickSort(A,left,right):
    pivotPos = partition(A,left,right)
    if(left<pivotPos):
        _quickSort(A,left,pivotPos)
    if(right>pivotPos):
        _quickSort(A,pivotPos+1,right)
    return A
    
    
def partition(A,left,right):    
    pivot = A[(left+right)//2]
    while(left<right):
        ''' swap two number when one is greater 
            than pivot and the other is less than pivot '''
        while(A[left]<pivot):
            left+=1
        while(A[right]>pivot):
            right-=1
        if(left<right):
            tmp = A[left]
            A[left] = A[right]
            A[right] = tmp
    ''' caveat: return the left position '''
    return left

def quickSort(A):
    assert(isinstance(A,list)),'Error'
    return _quickSort(A,0,len(A)-1)

A = [3,2,1,6,8,5]
print quickSort(A)