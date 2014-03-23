'''

Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

    For example, given array S = {-1 2 1 -4}, and target = 1.

    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

Created on Feb 12, 2014

@author: Songfan
'''

''' method 1: sort, 2 ptrs meet in the middle. Caveat: for loop on the front ptr p1, let middle ptr p2 and rear ptr p3 meet in the middle '''
import sys

def solution(num, target):
    n = len(num)
    if n <= 2: return -1
    
    num = sorted(num)
    closest = 0
    minGap = sys.maxint
    for p1 in range(n - 2):
        p2 = p1 + 1
        p3 = n - 1
        while p2 < p3:
            sum3 = num[p1] + num[p2] + num[p3]
            gap = abs(sum3 - target)
            
            if gap < minGap:
                closest = sum3
                minGap = gap
            
            if sum3 == target: return closest
            elif sum3 < target: p2 += 1
            else: p3 -= 1
            
    return closest
                
                
num = [-1, 2, 1, -4]
print solution(num, 1)            
                
                
                
                
                
                
                
                
                
            
        