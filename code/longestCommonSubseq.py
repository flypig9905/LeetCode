'''

find a longest common subsequence of A and B

A = [1,3,2,6,4,9]
B = [2,5,4,7,9]

LCS(A,B) = [2,4,9]

algorithm:
if A[i] = B[j]:
    LCS(A,B,i,j) = LCS(A,B,i-1,j-1)+1
else:
    LCS(A,B,i,j) = max(LCS(A,B,i-1,j), LCS(A,B,i,j-1))

Created on Jan 4, 2014

@author: Songfan
'''

def LCS(A,B):
    return _LCS(A, B, len(A)-1, len(B)-1, {})

def _LCS(A, B, m, n, h):
    ''' recursive call method is call memoization method, DP is built from bottom up '''
    
    if m < 0 or n < 0: return []    # if A or B is [], there cannot be any Common subsequence
    if (m,n) in h: return h[(m,n)]
    if A[m] == B[n]:
        tmp = _LCS(A, B, m-1, n-1, h)
        tmpCopy = tmp[:]
        tmpCopy.append(A[m])
    else:
        tmp1 = _LCS(A, B, m-1, n, h)
        tmp2 = _LCS(A, B, m, n-1, h)
        if len(tmp1) > len(tmp2):
            tmpCopy = tmp1[:]
        else:
            tmpCopy = tmp2[:]
    h[(m,n)] = tmpCopy
    return h[(m,n)]

def lcsDP(A,B):
    return _lcsDP(A, B, len(A)-1, len(B)-1)

def _lcsDP(A, B, m, n):
    h = {}
    for i in range(-1,m+1): # -1 is for init
        for j in range(-1,n+1):
            if i < 0 or j < 0:
                ''' for initialization, think of the matrix picture '''
                h[(i,j)] = []
            elif A[i] == B[j]:
                tmp = h[(i-1,j-1)]
                tmpCopy = tmp[:]
                tmpCopy.append(A[i])
                h[(i,j)] = tmpCopy
            else:
                tmp1 = h[(i-1,j)]
                tmp2 = h[(i,j-1)]
                if len(tmp1) > len(tmp2):
                    h[(i,j)] = tmp1
                else:
                    h[(i,j)] = tmp2
    return h[m,n]
                    

A = [1,3,2,6,4,9]
B = [1,2,5,6,7,9]
# A = [1,2]
# B = [1]
print 'memoization, recursive: ', LCS(A,B)
print 'DP: ', lcsDP(A,B)