'''

Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

Created on Jan 29, 2014

@author: Songfan
'''

''' similar to binary search, add mid first, recursively add left and right '''


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
    
    def _display(self, root):
        if root is None: return '*'
        result = str(root.val) + '(' + self._display(root.left) + ',' + self._display(root.right) + ')'
        return result

def solution(A):
    return buildBST(A)

def buildBST(A):
    n = len(A)
    if n == 0: return None
    if n == 1: return TreeNode(A[0])
    
    mid = n // 2
    node = TreeNode(A[mid])
    node.left = buildBST(A[:mid])
    node.right = buildBST(A[mid+1:])
    
    return node

A = range(1,7)
n = buildBST(A)
print BinaryTree(n)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

