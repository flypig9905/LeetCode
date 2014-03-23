'''

Given n, generate all structurally unique BST's (binary search trees) that store values 1...n.

For example,
Given n = 3, your program should return all 5 unique BST's shown below.

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

version I only returns the number of unique BSTs

Created on Feb 8, 2014

@author: Songfan
'''

''' dfs '''
import timeit

class TreeNode:
    def __init__(self, val = None, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
        
    def __str__(self):
        return str(self.val)
    
    
class BinaryTree:
    def __init__(self, root = None):
        self.root = root
        
    def __str__(self):
        return self._display(self.root)
    
    def _display(self, node):
        if node is None:
            return '*'
        return str(node.val) + '(' + self._display(node.left) + ',' + self._display(node.right) + ')'


def uniqueBST(n):
    candidate = range(1,n+1)
    return buildBST(candidate)
 
def buildBST(candidate):
    n = len(candidate)
    if n == 0: return [None]
    if n == 0: return [TreeNode(candidate[0])]
    
    res = []
    for i in range(n):
        lefts = buildBST(candidate[:i])
        rights = buildBST(candidate[i+1:])
        for l in lefts:
            for r in rights:
                tmp = TreeNode(candidate[i])
                tmp.left = l
                tmp.right = r
                res.append(tmp)
    return res
                
    
def countUniqueBST(n):
    f = {}
    f[0] = 1
    f[1] = 1
    for i in range(2, n + 1):
        for k in range(1,i + 1):
            f[i] = f.get(i,0) + f[k-1] * f[i-k]
    return f[n]
    
    
    
    

''' unittest binary tree '''
n4 = TreeNode(4)
n2 = TreeNode(2)
n5 = TreeNode(5, n4)
n3 = TreeNode(3, n2, n5)
print BinaryTree(n3), 'should be 3(2(*,*),5(4(*,*),*))'


''' unittest count '''
print countUniqueBST(4)

''' unittest list all combination '''

start = timeit.default_timer()
bst = uniqueBST(4)
stop = timeit.default_timer()
print stop - start

for b in bst:
    print BinaryTree(b)        
        
        
        
        
        
        
        
        
        
        