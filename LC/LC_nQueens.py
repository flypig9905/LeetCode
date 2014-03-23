'''

Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

For example,
There exist two distinct solutions to the 4-queens puzzle:

[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]

Created on Jan 26, 2014

@author: Songfan
'''

'''algorithm: dfs 
    vector of current state of quees: A[row] = col
    isValid method:
        def isValid(self, r, c):
            for j in range(self.N):
                # for every item in A, check if it is valid w.r.t. (r,c)
                if self.A[j] == c or abs(c - self.A[j]) == abs(r - j):
                    return False
            return True
    core dfs 
    def nQueens(self, r):
        for i in range(self.N):
            if self.isValid(r, i):
                self.A[r] = i
                if r == self.N - 1: 
                    self.saveResult()
                else:
                    self.nQueens(r + 1)
                # backtracking: return to the previous state
                self.A[r] = sys.maxint
        

'''
import sys
import copy

class Solution:
    def __init__(self, N = 0):
        self.N = N
        self.A = [sys.maxint]*self.N
        self.result = []
        self.nQueens(0) # solve nQueens

    def isValid(self, r, c):
        for j in range(self.N):
            ''' for every item in A, check if it is valid w.r.t. (r,c) '''
            if self.A[j] == c or abs(c - self.A[j]) == abs(r - j):
                return False
        return True
        
    def saveResult(self):
        res = []
        for i in range(self.N):
            tmp = list('.'*self.N)
            tmp[self.A[i]] = 'Q'
            res.append(''.join(tmp))
        self.result.append(res)
        
    def nQueens(self, r):
        for i in range(self.N):
            if self.isValid(r, i):
                self.A[r] = i
                if r == self.N - 1: 
                    self.saveResult()
                else:
                    self.nQueens(r + 1)
                ''' backtracking: return to the previous state '''
                self.A[r] = sys.maxint
    
    def displayResult(self):
        for item in self.result:
            print 'solution:'
            for r in item:
                print r
                
q = Solution(4)
q.displayResult()