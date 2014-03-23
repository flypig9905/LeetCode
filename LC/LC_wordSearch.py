'''

Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. 
The same letter cell may not be used more than once.

For example,
Given board =

[
  ["ABCE"],
  ["SFCS"],
  ["ADEE"]
]
word = "ABCCED", -> returns true,
word = "SEE", -> returns true,
word = "ABCB", -> returns false.

Created on Jan 13, 2014

@author: Songfan
'''

''' algorithm: dfs for every grid on board, store visited grid '''


def wordSearch(board, word):
    # assume correct input
    row = len(board)
    col = len(board[0])
    ''' python 2-dim list is tricky, use dictionary instead '''
    visited = {}
    for i in range(row):
        for j in range(col):
            visited[i,j] = False
    
    for i in range(row):
        for j in range(col):
            if _dfs(board, word, i, j, visited, 0): # 0 means the first char of word 
                return True
    return False

def _dfs(board, word, m, n, visited, charPosition):
    if charPosition >= len(word):   # we have finished search every char in word
        return True
    if m < 0 or n < 0 or m >= len(board) or n >= len(board[0]):   # out of boundary
        return False
    if visited[m,n] is True:   # we have visited this grid
        return False
    if board[m][n] != word[charPosition]: # end search if char doesn't match
        return False
    visited[m,n] = True
    res =   _dfs(board, word, m + 1, n, visited, charPosition + 1) or \
            _dfs(board, word, m - 1, n, visited, charPosition + 1) or \
            _dfs(board, word, m, n + 1, visited, charPosition + 1) or \
            _dfs(board, word, m, n - 1, visited, charPosition + 1)
    ''' caveat: set this grid visited to be False '''
    visited[m,n] = False
    return res

board = [
         'ABCE',
         'SFCS',
         'ADEE' 
         ]
word = 'ABCCED'
print wordSearch(board, word), 'should be True'

word = 'SEE'
print wordSearch(board, word), 'should be True'

word = 'ABCB'
print wordSearch(board, word), 'should be False'

