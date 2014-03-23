'''
CTCI 11.6
the row and col of a matrix is sort in ascending order, find x

Created on Dec 7, 2013

@author: Songfan
'''
def findInMatrix(M,v):
    rowStart = 0
    colStart = 0
    rowEnd = len(M)-1
    colEnd = len(M[0])-1
    while(rowStart<=rowEnd and colStart<=colEnd):
        if M[rowStart][colStart]==v:
            return True 
        elif M[rowEnd][colStart]<v:
            colStart+=1
        elif M[rowStart][colEnd]<v:
            rowStart+=1
        elif M[rowStart][colEnd]>v:
            colEnd-=1
        elif M[rowEnd][colStart]>v:
            rowEnd-=1
    return False
    
M = [[15,20,40,85],[20,35,80,95],[30,55,95,105],[40,80,100,120]]
print findInMatrix(M,56)