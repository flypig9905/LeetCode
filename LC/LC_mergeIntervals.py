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

def merge_interval(intervals):
    n = len(intervals)
    if n == 0: return []
    inter_sort = sorted(intervals, key = lambda x: x.start)
    curr_inter = inter_sort[0]
    result = []
    for i in range(1,n):
        if inter_sort[i].start > curr_inter.end:
            result.append(curr_inter)
            curr_inter = inter_sort[i]
        else:
            curr_inter = Interval(curr_inter.start, max(curr_inter.end, inter_sort[i].end))
    if curr_inter not in result:
        result.append(curr_inter)
    
    return result
    
    
    
    
    
    
    
    
''' unittest Interval '''
# pass
#i = Interval(1,4)
#print i

''' unittest merge_interval '''
intervals = [Interval(2,6),Interval(1,3),Interval(8,18),Interval(10,21)]
m = merge_interval(intervals)
for e in m:
    print e

