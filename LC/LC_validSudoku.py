'''

Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.

Created on Feb 1, 2014

@author: Songfan
'''

''' for loop: 1. check rows, 2. check cols, 3. check 3*3 blocks
    1 and 2 can be combined
'''

def validSudoku(board):
    ''' check rows '''

                    
    ''' check rows and cols'''
    for i in range(9):
        memRow = {}
        memCol = {}
        for j in range(9):
            if board[i][j] != '.':
                if board[i][j] in memRow:
                    return False
                else:
                    memRow[board[i][j]] = True
            if board[j][i] != '.':
                if board[j][i] in memCol:
                    return False
                else:
                    memCol[board[j][i]] = True
    
    ''' check 3 by 3 blocks '''
    for i in range(0,9,3):
        for j in range(0,9,3):
            memBlock = {}
            for m in range(3):
                for n in range(3):
                    if board[i+m][j+n] != '.':
                        if board[i+m][j+n] in memBlock:
                            return False
                        else:
                            memBlock[board[i+m][j+n]] = True
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

print validSudoku(board)