'''

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

Created on Feb 9, 2014

@author: Songfan
'''

''' two non-overlap transactions: divide and conquer
    O(N^2) time: for every i, compute max profit from P[:i] and P[i:]
    O(N) time, O(N) space: 
        forward scan, compute the max profit that end with each time
        backward scan, compute the max profit backwards, and check total profit
'''

def solution(P):
    n = len(P)
    if n <= 1: return 0
    
    ''' forward scan '''
    maxProfitForward = [0]
    minPrice = P[0]
    maxProfit = 0
    for i in range(1, n):
        maxProfit = max(maxProfit, P[i] - minPrice)
        maxProfitForward.append(maxProfit)
        
    ''' backward scan and compute max profit '''
    maxPrice = P[n-1]
    maxProfit = 0
    maxProfitTotal = 0
    for i in range(n-2, -1, -1):
        maxProfit = max(maxProfit, maxPrice - P[i])
        maxProfitTotal = max(maxProfitTotal, maxProfit + maxProfitForward[i])
    
    return maxProfitTotal

P = [1,3,2,3,4,1,3,2,4]
print solution(P), 'should be 6'

        
        
        
        
        
        
        
    
    
     

