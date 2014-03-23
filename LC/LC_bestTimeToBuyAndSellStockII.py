'''

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like 
(ie, buy one and sell one share of the stock multiple times). 
However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

Created on Feb 9, 2014

@author: Songfan
'''

''' buy low and sell high, take every possible profit,
    algorithm: convert the list to diff list, and add positive diff '''
    
def solution(P):
    n = len(P)
    if n <= 1: return 0
    
    profit = 0
    for i in range(1,n):
        diff = P[i] - P[i-1]
        if diff > 0: profit += diff
    
    return profit

P = [1,3,2,3,4,1,3,2,4]
print solution(P), 'should be 8'