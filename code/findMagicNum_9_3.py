'''
CTCI P109 9-3

Magic index in an array is defined as index such that A[i]=i. Given a sorted array of distinct integers, find magic index if exists in array A

Created on Dec 2, 2013

@author: Songfan
'''

def _findMagicNumUnique(A,idx,result):
    if len(A)==0: return
    mid = len(A)//2
    if A[mid]<=idx[mid]:
        if A[mid]==idx[mid] and idx[mid] not in result:
            result.append(idx[mid])
        _findMagicNumUnique(A[mid+1:],idx[mid+1:],result)
    if A[mid]>=idx[mid]:
        if A[mid]==idx[mid] and idx[mid] not in result:
            result.append(idx[mid])
        _findMagicNumUnique(A[:mid],idx[:mid],result)

def findMagicNumUnique(A):
    assert(isinstance(A,list)),'input error: input should be an array'
    result = []
    _findMagicNumUnique(A,range(len(A)),result)
    return result

def _findMagicNumUnique(A,idx,result):


def findMagicNum(A):
    assert(isinstance(A,list)),'input error: input should be an array'
    result = []
    _findMagicNum(A,range(len(A)),result)
    return result



A = [-3,-1,0,1,3,5,6,8]
print findMagicNumUnique(A)
A = [-40,-20,-1,1,2,3,5,7,9,12,13]
print findMagicNumUnique(A)      