'''

Given a collection of numbers, return all possible permutations.

For example,
[1,2,3] have the following permutations:
[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], and [3,2,1].

able to handle dups

Created on Jan 12, 2014

@author: Songfan
'''

''' 
    recursion + memoization
    recursively add the last element to the every possible position of the previous list 
    O(N!) time worst case, O(N!) space
    
'''



def permutations(A):
    assert(isinstance(A,list)),'input error'
    return _permutations(A, {}, len(A) - 1)

def _permutations(A, h, m):
    n = len(A)
    if n == 0: return []
    if n == 1: return [A]
    if m in h: return h[m]
    prevPerms = _permutations(A[:m], h, m - 1)
    lastElem = A[m]
    currPerms = []
    for perm in prevPerms:
        for i in range(len(perm)+1):
            ''' add the element to possible location '''
            ''' caveat: since it is list not string, we cannot use +, instead, use extend which requires deep copy of the tmp variable '''
            tmp = perm[:i][:]
            tmp.extend([lastElem])
            tmp.extend(perm[i:])
            if tmp not in currPerms:
                currPerms.append(tmp)
    h[m] = currPerms
    return currPerms

''' unittest '''
A = [1,2,1]
print permutations(A)