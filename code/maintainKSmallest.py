'''
maintain a string that contains k smallest integer from 2 int streams

Created on Mar 18, 2014

@author: Songfan
'''

'''
use max heap,
1. compare the 4 current element from each stream, pop the smallest, namely tmp
2. compare tmp to the root of max heap
'''
from binaryHeap import MaxBinaryHeap

def kthSmall(k, s1, s2):
    hp = MaxBinaryHeap()
    while s1!=[] and s2!=[]:
        if s1[0] > s2[0]:
            e = s2.pop(0)
        else:
            e = s1.pop(0)
        
        addElementToHeap(hp, k, e)
    
    for e in s1:
        addElementToHeap(hp, k, e)
    for e in s2:
        addElementToHeap(hp, k, e)
    
    print hp.heapList

def addElementToHeap(hp, k, e):
    # insert to heap
    if hp.getSize() < k:
        hp.insert(e)
    else:
        if hp.peakRoot() > e:
            # heap is full, pop the max and insert the current
            hp.popRoot()
            hp.insert(e) 
            
            
            
s1 = [1,3,5,2,4,6,8,5,3,2]
s2 = [5,23,8,9,8,1,44,7,88]
kthSmall(4, s1, s2)