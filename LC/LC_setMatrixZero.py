'''
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.

Created on Jan 2, 2014

@author: Songfan
'''

''' O(mn): iterate and find the position of 0 stored in tuples, then iterate tuples and set each element to be 0 
    O(m+n): iterate row and col, use two array to store 0s to represent that row or col should be set to 0
    O(1): use the first row and col to represent the rows and cols that need to be set to 0 '''
    
def setMatrixZero(M):
    m = len(M)
    if m == 0: return None
    n = len(M[0])
    if n == 0: return None
    
    # iterate the first row and first col, use two flags to indicate if they need to be set to 0, then we set them in the end
    setColOneZero = False
    for i in range(m):
        if M[i][0] == 0:
            setColOneZero = True
            break
    
    setRowOneZero = False
    for i in range(n):
        if M[0][i] == 0:
            setRowOneZero = True
            break
        
    # iterate the submatrix (aside from the first row and col), if came across a 0, store it in first row or col
    for i in range(1, m):
        for j in range(1, n):
            if M[i][j] == 0:
                M[i][0] = 0
                M[0][j] = 0
                
    # iterate submatrix and set zeros based on first row and first col
    for i in range(1, m):
        for j in range(1, n):
            if M[i][0] == 0 or M[0][j] == 0:
                M[i][j] = 0
                
    # set the first row and col to 0 if needed
    if setColOneZero:
        for i in range(m):
            M[i][0] = 0
    if setRowOneZero:
        for i in range(n):
            M[0][i] = 0
                
    return M
    
    
    


''' 1 0 2 3 4 5
    2 2 1 0 1 2
    3 1 2 3 4 5
    1 2 0 1 1 3 
    
    m = 4, n = 6
    '''
    
M = [[1,0,2,3,4,5],[2,2,1,0,1,2],[3,1,2,3,4,5],[1,2,0,1,1,3]]
M0 = setMatrixZero(M)
for i in M:
    print ', '.join([str(j) for j in i])
