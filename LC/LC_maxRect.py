'''

Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing all ones and return its area.

Created on Feb 8, 2014

@author: Songfan
'''

''' O(N^2): compute the 2d histogram and convert the problem to largest rect in hist

consider this matrix: 
11000
11000
00111
00111
00111

the histogram is:
11000
22000
00111
00222
00333

then, run largest rect in hist for each row
 '''
from stack import Stack

def solution(M):
    r = len(M)
    if r == 0: return
    c = len(M[0])
    if c == 0: return
    
    ''' construct hist '''
    hist = {}
    for i in range(r):
        for j in range(c):
            if M[i][j] == 0:
                hist[i,j] = 0
            else:
                if i == 0:
                    hist[i,j] = 1
                else:
                    hist[i,j] = hist[i-1,j] + 1
    
    maxRect = 0
    for i in range(r):
        ''' reconstruct hist from hashtable '''
        h = []
        for j in range(c):
            h.append(hist[i,j])
            
        maxRect = max(maxRectInHist(h), maxRect)
    
    return maxRect
    
def maxRectInHist(A):
    n = len(A)
    ''' add dummy element '''
    A.append(-1)
    s = Stack()
    i = 0
    maxRect = 0
    
    while i <= n:
        if s.isEmpty() or A[i] > A[s.peek()]:
            s.push(i)
            i += 1
        else:
            tmp = s.pop()
            if s.isEmpty():
                rect = A[tmp] * i
            else:
                rect = A[tmp] * (i - s.peek() - 1)
            maxRect = max(maxRect, rect)
    return maxRect


M = [[1,1,0,0,0],[1,1,0,0,0],[0,0,1,1,1],[0,0,1,1,1],[0,0,1,1,1]]
print solution(M), 'should be 9'
    
    
    
    


