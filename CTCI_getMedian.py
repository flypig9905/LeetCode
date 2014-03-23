'''
CTCI P54, N3
Created on Nov 19, 2013

@author: Songfan
'''
from binaryHeap import MaxBinaryHeap, MinBinaryHeap
def getMedian(aList):
    minHeap = MinBinaryHeap()
    maxHeap = MaxBinaryHeap()
    for e in aList:
        minHeapLen = minHeap.getSize()
        maxHeapLen = maxHeap.getSize()
        if maxHeapLen == minHeapLen:
            minHeap.insert(e)
        elif maxHeapLen < minHeapLen:
            currMedian = minHeap.peakRoot()
            if e <= currMedian:
                maxHeap.insert(e)
            else:
                maxHeap.insert(currMedian)
                minHeap.popRoot()
                minHeap.insert(e)
        else:
            currMedian = maxHeap.peakRoot()
            if e >= currMedian:
                minHeap.insert(e)
            else:
                minHeap.insert(currMedian)
                maxHeap.popRoot()
                maxHeap.insert(e)
    if minHeap.getSize() > maxHeap.getSize():
        return minHeap.peakRoot()
    elif minHeap.getSize() < maxHeap.getSize():
        return maxHeap.peakRoot()
    else:
        return (minHeap.peakRoot()+maxHeap.peakRoot()+0.0)/2
    
aList = [1,5,3,8,9,6]
print getMedian(aList)
aList = [1]
print getMedian(aList)
aList = [1,2,2,4]
print getMedian(aList)
aList = [1,3,3,3,5]
print getMedian(aList)
aList = [3,4,1,2]
print getMedian(aList)
