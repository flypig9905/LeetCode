'''
Insert Interval

Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:
Given intervals [1,3],[6,9], insert and merge [2,5] in as [1,5],[6,9].

Example 2:
Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] in as [1,2],[3,10],[12,16].

This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].

Created on Jan 1, 2014

@author: Songfan
'''

''' algorithm: linear scan and combine interval '''

class Interval:
    def __init__(self, start = 0, end = 0):
        self.start = start
        self.end = end

    def __str__(self):
        return '[' + str(self.start) + ',' + str(self.end) + ']'


'''
O(logN), binary search
- search upper bound and lower bound
- compared upper bound and lower bound to see if there should be any interval merge
'''
def solutionBS(A, b):
    n = len(A)
    if n == 0: return [b]
    upperIdx = search(A, b, 'upper')
    lowerIdx = search(A, b, 'lower')
    print upperIdx, lowerIdx
    


def search(A, b, bound):
    n = len(A)
    if bound == 'upper':
        return bs([a.start for a in A], b.start, 0, n-1)
    elif bound == 'lower':
        return bs([a.end for a in A], b.end, 0, n-1)

def bs(M, m, front, rear):
    n = len(M)
    if front > rear: return
    mid = (front+rear) // 2
    if mid < 0: return mid # reach head
    if mid >= n: return n # reach tail
    if m >= M[mid] and m <= M[mid+1]: return mid # between two interval
    if M[mid] > m:
        return bs(M, m, front, mid)
    elif M[mid] < m:
        return bs(M, m, mid+1, rear)

    
A = [Interval(1,2),Interval(3,5),Interval(6,7),Interval(8,10),Interval(12,16)]
b = Interval(4,9)
print solutionBS(A, b)
a = 1
    
    
    
''' 
O(N), linear scan
'''
def insertInterval(A, b):
    # assume correct input
    if not b.start or not b.end: return A
    result = []
    n = len(A)
    for i in range(n):
        if A[i].end < b.start:
            result.append(A[i])
        elif A[i].start > b.end:
            result.append(b)
            result.append(A[i])
        else:
            b = Interval(min(A[i].start, b.start), max(A[i].end, b.end))
            if i == n-1:
                result.append(b)
    return result
            

''' unittest '''
A = [Interval(1,3),Interval(6,9)]
b = Interval(2,5)
B = insertInterval(A, b)
for e in B:
    print e
print '###'
    
A = [Interval(1,3),Interval(3,5),Interval(6,7),Interval(8,10),Interval(12,16)]
b = Interval(4,13)
B = insertInterval(A, b)
for e in B:
    print e


