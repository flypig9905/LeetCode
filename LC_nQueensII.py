'''
Created on Jan 26, 2014

@author: Songfan
'''

import sys
import copy

class Solution:
    def __init__(self, N = 0):
        self.N = N
        self.A = [sys.maxint]*self.N
        self.result = 0
        self.nQueens(0) # solve nQueens

    def isValid(self, r, c):
        for j in range(self.N):
            ''' for every item in A, check if it is valid w.r.t. (r,c) '''
            if self.A[j] == c or abs(c - self.A[j]) == abs(r - j):
                return False
        return True
        
        
    def nQueens(self, r):
        for i in range(self.N):
            if self.isValid(r, i):
                self.A[r] = i
                if r == self.N - 1: 
                    self.result += 1
                else:
                    self.nQueens(r + 1)
                ''' backtracking: return to the previous state '''
                self.A[r] = sys.maxint
    
    def displayResult(self):
        print self.result
                
q = Solution(4)
q.displayResult()