'''

Given a collection of intervals, merge all overlapping intervals.

For example,
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18].

Created on Jan 1, 2014

@author: Songfan
'''

''' algorithm: sort based on the first element of the tuple, then merge '''
class Interval:
    def __init__(self, start = 0, end = 0):
        self.start = start
        self.end = end

    def __str__(self):
        return '[' + str(self.start) + ',' + str(self.end) + ']'

def mergeInterval(intervals):
    assert(isinstance(intervals, list)),'input error'
    n = len(intervals)
    if n == 0: return []
    interSorted = sorted(intervals, key = lambda x: x.start)
    curInter = interSorted[0]
    result = []
    for i in range(1,n):
        assert(isinstance(interSorted[i], Interval)),'input should be object of Interval class'
        if interSorted[i].start > curInter.end:
            result.append(curInter)
            curInter = interSorted[i]
        else:
            curInter = Interval(curInter.start, max(curInter.end, interSorted[i].end))
    if curInter not in result:
        result.append(curInter)
    
    return result
    
    
    
    
    
    
    
    
''' unittest Interval '''
# pass
#i = Interval(1,4)
#print i

''' unittest mergeInterval '''
intervals = [Interval(2,6),Interval(1,3),Interval(8,18),Interval(10,21)]
m = mergeInterval(intervals)
for e in m:
    print e

