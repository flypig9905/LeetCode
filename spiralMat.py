'''
given a number N, return N*N spiral Matrix

Created on Mar 13, 2014

@author: Songfan
'''

'''
from outter circle inwards
'''
def spiral(N):
    if N < 0: return
    M = [[0 for _ in range(N)] for _ in range(N)]
    n = 1
    circleNum = N // 2
    for i in range(circleNum):
        sideLen = N-1-2*i
        
        # upper
        r = i
        for c in range(i,i+sideLen):
            M[r][c] = n
            n += 1
        
        # right
        c = N-1-i
        for r in range(i,i+sideLen):
            M[r][c] = n
            n += 1
        
        # bottom
        r = N-1-i
        for c in range(N-1-i,N-1-i-sideLen,-1):
            M[r][c] = n
            n += 1
        
        # left
        c = i
        for r in range(N-1-i,N-1-i-sideLen,-1):
            M[r][c] = n
            n += 1
    if N % 2:
        M[N//2][N//2] = n
    return M

M = spiral(5)
for m in M:
    print m