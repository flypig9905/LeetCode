'''

Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.

For example,
Given height = [2,1,5,6,2,3],
return 10.

Created on Feb 1, 2014

@author: Songfan
'''

''' O(N): 
    maintain a increasing stack. 
    If stack is empty or element is greater than the top of stack, push the index of element to stack.
    else:
        A[curr] := current bar
        pop the top index out, compute the area of rectangle with this element as the smallest bar. We can guarantee the tall
        bars (taller than A[curr]) being poped out are not wasted because there will be no greater area formed by the these tall bars, 
        simply because the area is bounded by the A[curr]
'''

from stack import Stack

def solution(A):
    n = len(A)
    if n == 0: return 0
    s = Stack()
    A.append(-1)
    maxSum = 0
    i = 0
    while i <= n:
        if s.isEmpty() or A[i] > A[s.peek()]:
            s.push(i)
            i += 1
        else:
            tmp = s.pop()
            ''' Let the removed bar be hist[tmp]. Calculate area of rectangle with hist[tmp] as smallest bar '''
            if s.isEmpty():
                tmpArea = A[tmp] * i
            else:
                tmpArea = A[tmp] * (i - s.peek() - 1)   # s.peek() will tell how long the current rect spans
            maxSum = max(maxSum, tmpArea)
    return maxSum

A = [2,1,5,6,2,3]
print solution(A), 'should be 10'

A = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,1,5,6,2,3]
print solution(A)