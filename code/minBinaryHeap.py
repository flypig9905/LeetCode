'''
Created on Nov 7, 2013

@author: Songfan
'''

# use list structure to implement Minimum Binary Heap

class MinBinaryHeap:
    def __init__(self):
        self.heapList = [0]
        self.size = 0
        
    def insert(self, item):
        self.heapList.append(item)
        self.size += 1
        self.siftUp(self.size)
    
    def siftUp(self, size): # used for delete item from heap
        while(size//2>0):
            if self.heapList[size] < self.heapList[size//2]:
                tmp = self.heapList[size]
                self.heapList[size] = self.heapList[size//2]
                self.heapList[size//2] = tmp
            size = size//2
            
    def delMin(self):   
        if self.size == 0:
            return False
        minItem = self.heapList[1]
        self.heapList[1] = self.heapList[self.size]
        self.heapList.pop()
        self.size -= 1
        self.siftDown(1)
        return minItem
    
    def siftDown(self, i):  # used for building heap
        while(i<=self.size//2):
            minChildIdx = self.minChild(i)
            if self.heapList[i] > self.heapList[minChildIdx]:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[minChildIdx]
                self.heapList[minChildIdx] = tmp
            i = minChildIdx
        
    def minChild(self, i):
        if self.size == i*2:
            return i*2
        else:
            if self.heapList[i*2]>self.heapList[i*2+1]:
                return 2*i+1
            else:
                return 2*i
    
    def buildMinBinaryHeap(self, aList):
        self.heapList = aList
        self.heapList.insert(0, 0)
        self.size = len(self.heapList) - 1
        i = self.size //2
        while(i>0):
            self.siftDown(i)
            i -= 1
        
        
        
    def printHeap(self):
        print [i for i in self.heapList]
            
aMinBinaryHeap = MinBinaryHeap()
aMinBinaryHeap.insert(33)
aMinBinaryHeap.delMin()
aMinBinaryHeap.printHeap()
aMinBinaryHeap.insert(9)
aMinBinaryHeap.insert(21)
aMinBinaryHeap.insert(14)
aMinBinaryHeap.insert(18)
aMinBinaryHeap.insert(19)
aMinBinaryHeap.insert(11)
aMinBinaryHeap.insert(5)
aMinBinaryHeap.printHeap()
print aMinBinaryHeap.delMin()
aMinBinaryHeap.printHeap()
h = MinBinaryHeap()
h.buildMinBinaryHeap([9,6,5,2,3])
h.printHeap()