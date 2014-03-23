'''

algorithm: for every element i in A, find the longest subseq that end with i-1, 
    check if if A[i] is ok to add to the previous subseq and also check if this will make it the longest

Created on Jan 4, 2014

@author: Songfan
'''


def longestMonoSubseq(A):
    return _lms(A, {}, len(A))

def _lms(A, h, n):
    N = len(A)
    assert(n <= N), 'input error'
    if N == 0: return []
    if n == 0 or N == 1: return [A[0]]
    if n in h: return h[n]
    for i in range(N):
        # for every element in A
        longest = [A[0]]
        for j in range(i):
            # for every element before A[i]
            tmp = _lms(A[:i], h, j)
            tmpCopy = tmp[:]    # make a deepcopy
            if A[j] <= A[i]:
                tmpCopy.append(A[i])
                if len(tmpCopy) >= len(longest):
                    longest = tmpCopy
        # assign the longest to map
        h[i] = longest
    
    # find the list with max length
    V = h.keys()
    maxKey = 0
    for v in V:
        if len(h[v]) > len(h[maxKey]):
            maxKey = v
    return h[maxKey]

def longestMonoSubseqDP(A):
    return _lmsDP(A, len(A))

def _lmsDP(A, n):
    h = {}
    for i in range(n):
        h[i] = [A[0]]
        for j in range(i):
            if A[j] <= A[i] and 1 + len(h[j]) > len(h[i]):
                tmp = h[j]
                tmpCopy = tmp[:]
                tmpCopy.append(A[i])
                h[i] = tmpCopy
    K = h.keys()
    maxKey = K[0]
    for k in K:
        if len(h[k]) > len(h[maxKey]):
            maxKey = k
    return h[k]

A = [1,2,4,4,3,4,6]
print 'memoization, recursive: ', longestMonoSubseq(A)    
print 'DP: ', longestMonoSubseqDP(A)

A = [6,5,3,2,7,8,1,10]
print 'memoization, recursive: ', longestMonoSubseq(A)    
print 'DP: ', longestMonoSubseqDP(A)