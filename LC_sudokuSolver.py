'''

Write a program to solve a Sudoku puzzle by filling the empty cells.

Empty cells are indicated by the character '.'.

You may assume that there will be only one unique solution.

Created on Feb 1, 2014

@author: Songfan
'''

''' dfs '''

Nums = ['1','2','3','4','5','6','7','8','9']

def sudokuSolver(board):
    ''' stopping condition, find the position of last dot '''

    for i in range(9):
        for j in range(9):
            if board[i][j] == '.':
                for n in Nums:
                    board[i][j] = n
                    ''' memorize this !!! '''
                    if validSudoku(board, i, j) and sudokuSolver(board):
                        return board
                    board[i][j] = '.'
                return False    # this means we have tried every combination for board[i][j] and non of them works, this means this sudoku is invalid
    return True

def validSudoku(board, r, c):
    ''' check validity for a specific position is easier compared with checking validity of entire board '''
    
    ''' check dups for rows '''
    for i in range(9):
        if i != c and board[r][i] == board[r][c]:
            return False
        
    ''' check dups for cols '''
    for i in range(9):
        if i != r and board[i][c] == board[r][c]:
            return False
        
    ''' check dups for block '''
    m = r // 3
    n = c // 3
    for i in range(3):
        for j in range(3):
            if (m*3 + i != r or n*3 + j != c) and board[m*3+i][n*3+j] == board[r][c]: # not (m+i==r and n+j==c)
                return False
    return True
    
    
    
    
    
    
    
    
board = [['5','3','.','.','7','.','.','.','.'],
         ['6','.','.','1','9','5','.','.','.'],
         ['.','9','8','.','.','.','.','6','.'],
         ['8','.','.','.','6','.','.','.','3'],
         ['4','.','.','8','.','3','.','.','1'],
         ['7','.','.','.','2','.','.','.','6'],
         ['.','6','.','.','.','.','2','8','.'],
         ['.','.','.','4','1','9','.','.','5'],
         ['.','.','.','.','8','.','.','7','9']]

b = sudokuSolver(board)
for i in b:
    print i