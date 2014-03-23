'''

Given a 2D board containing 'X' and 'O', capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region .

For example,
X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X

Created on Jan 30, 2014

@author: Songfan
'''

''' dfs + memoization: for every 'O', check to see if it is surrounded '''

def solution(board):
    return _surroundRegion(board, {})

def _surroundRegion(board, h):
    for r in range(len(board)):
        for c in range(len(board[0])):
            if board[r][c] == 'O' and \
                    isSurrounded(board, r, c, h, ''):
                board[r][c] = 'X'
    return board
    
def isSurrounded(board, i, j, h, fromDirection):
    if board[i][j] == 'X':
        h[i,j] = True
        return True
    if i <= 0 or i >= len(board) - 1 or j <= 0 or j >= len(board[0]) - 1:
        return False
    if (i, j) in h:
        return h[i, j]
    
    
    ''' fromDirection is to prevent double checking '''
    left = True
    right = True
    up = True 
    down = True
    
    if fromDirection != 'left': 
        ''' for the left item, the recursive call is from right '''
        left = isSurrounded(board, i, j - 1, h, 'right')
    if fromDirection != 'right': 
        right = isSurrounded(board, i, j - 1, h, 'left')
    if fromDirection != 'up': 
        up = isSurrounded(board, i - 1, j, h, 'down')
    if fromDirection != 'down': 
        down = isSurrounded(board, i + 1, j, h, 'up')
        
    h[i, j] = left and right and up and down
    return  h[i, j]
    
    
board = [['X','X','X','X'],['X','O','O','X'],['X','X','O','X'],['X','O','X','X']]
b = solution(board)
print b
