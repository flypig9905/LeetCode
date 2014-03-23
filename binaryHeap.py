'''
Created on Nov 7, 2013

@author: Songfan
'''
import abc
# use list structure to implement Minimum Binary Heap
class BinaryHeap:
    def __init__(self):
        self.heapList = [0]
        self.size = 0
        
    def getSize(self):
        return self.size

    @abc.abstractmethod
    def siftUpCompare(self,upper,lower):
        """when sift a element up, compare the heap element from upper level to lower level"""
        return
    
    @abc.abstractmethod
    def siftDownCompare(self,upper,lower):
        """when sift a element up, compare the heap element from upper level to lower level"""
        return

    def insert(self, item):
        """Insert a item to binary heap"""
        self.heapList.append(item)
        self.size += 1
        self.siftUp(self.size)
    
    def peakRoot(self):
        assert (self.size > 0), "empty heap!"
        return self.heapList[1]
    
    def popRoot(self):   
        """remove the root element, it is either the minimum or the maximum if the heap is min-heap or max-heap"""
        if self.size == 0:
            return False
        rootItem = self.heapList[1]
        self.heapList[1] = self.heapList[self.size]
        self.heapList.pop()
        self.size -= 1
        self.siftDown(1)
        return rootItem
    
    def siftDown(self, i):  # used for building heap
        while(i<=self.size//2):
            childIdx = self.candidateChild(i)
            if self.siftDownCompare(self.heapList[i], self.heapList[childIdx]):
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[childIdx]
                self.heapList[childIdx] = tmp
            i = childIdx
    
    def candidateChild(self, i):
        """ get candidate child given parents index: minChild for min-heap, maxChild for max-heap"""
        if self.size == i*2:
            return i*2
        else:
            if self.siftDownCompare(self.heapList[i*2], self.heapList[i*2+1]):  # for simplicity, adopt same comparison result
                return 2*i+1
            else:
                return 2*i
    
    def buildBinaryHeap(self, aList):
        self.heapList = aList
        self.heapList.insert(0, 0)
        self.size = len(self.heapList) - 1
        i = self.size //2
        while(i>0):
            self.siftDown(i)
            i -= 1
    
    def siftUp(self, size): # used for add item and delete item from heap
        while(size//2>0):
            if self.siftUpCompare(self.heapList[size],self.heapList[size//2]):
                tmp = self.heapList[size]
                self.heapList[size] = self.heapList[size//2]
                self.heapList[size//2] = tmp
            size = size//2
            


    def printHeap(self):
        print [i for i in self.heapList]


""" min-heap """
class MinBinaryHeap(BinaryHeap):
        
    def siftUpCompare(self, upper, lower):
        return upper < lower
            

    def siftDownCompare(self, upper, lower):
        return upper > lower
        

    
""" max-heap """
class MaxBinaryHeap(BinaryHeap):
        
    def siftUpCompare(self, upper, lower):
        return upper > lower
            

    def siftDownCompare(self, upper, lower):
        return upper < lower

            
# aMinBinaryHeap = MinBinaryHeap()
# aMinBinaryHeap.insert(33)
# aMinBinaryHeap.popRoot()
# aMinBinaryHeap.printHeap()
# aMinBinaryHeap.insert(9)
# aMinBinaryHeap.insert(21)
# aMinBinaryHeap.insert(14)
# aMinBinaryHeap.insert(18)
# aMinBinaryHeap.insert(19)
# aMinBinaryHeap.insert(11)
# aMinBinaryHeap.insert(5)
# aMinBinaryHeap.printHeap()
# print aMinBinaryHeap.popRoot()
# aMinBinaryHeap.printHeap()
# h = MinBinaryHeap()
# h.buildBinaryHeap([9,6,5,2,3])
# h.printHeap()
# maxH = MaxBinaryHeap()
# maxH.buildBinaryHeap([9,6,5,2,3])
# maxH.printHeap()