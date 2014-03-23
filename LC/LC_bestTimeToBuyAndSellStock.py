'''

Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Created on Feb 9, 2014

@author: Songfan
'''

''' O(n) time, O(1) space, greedy algorithm, track the current min and max profit '''

def solution(P):
    n = len(P)
    if n <= 1: return 0
    
    currMin = P[0]
    maxProfit = 0
    
    for i in range(1, n):
        maxProfit = max(maxProfit, P[i] - currMin)
        currMin = min(P[i], currMin)
        
    return maxProfit

P = [2,1,3,4,5,2]
print solution(P), 'should be 4'