'''
Created on Dec 6, 2013

@author: Songfan
'''
from math import log

def getPassNum(A,base):
    # get the number of passes of sorting needed
    return int((log(max(A),base)+1))

def getBit(a,digit,base):
    # get the corresponding bucket index
#     return (a%(base**(digit+1)))//(base**digit)
    return (a // base ** digit) % base 


def sortBasedOnDigit(A,digit,base):
    # sort all number based on the current digit
    buckets = [[] for i in range(base)]
    for a in A:
        buckets[getBit(a,digit,base)].append(a)
    result = []
    for b in buckets:
        result.extend(b)
    return result
    

def radixSort(A,base):
    assert(isinstance(A,list)),'Input Error'
    passNum = getPassNum(A,base)
    for i in range(passNum):
        A = sortBasedOnDigit(A,i,base)
    return A

A = [994,28,19,1245]
print radixSort(A,10)