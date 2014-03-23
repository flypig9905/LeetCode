'''
determine if a bst is valid

Created on Mar 13, 2014

@author: Songfan
'''

import sys

class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
    def __str__(self):
        return str(self.val)
        
class BinaryTree:
    def __init__(self, root=None):
        self.root = root
        
    def __str__(self):
        return self._display(self.root)
    
    def _display(self, node):
        if node is None: return '*'
        return str(node.val) + '(' + self._display(node.left) + ',' \
            + self._display(node.right) + ')'

def validBST(root):
    if root is None: return True
    
    if root.left is None: leftVal = -sys.maxint
    else: leftVal = root.left.val
    
    if root.right is None: rightVal = sys.maxint
    else: rightVal = root.right.val
    
    return root.val > leftVal and root.val < rightVal and \
        validBST(root.left) and validBST(root.right)
        
n0 = TreeNode(0)
n2 = TreeNode(2)
n5 = TreeNode(5)
n1 = TreeNode(1, n0, n2)
n4 = TreeNode(4, None, n5)
n3 = TreeNode(3, n1, n4)
print BinaryTree(n3)
print validBST(n3),'should be True'
n4.left = TreeNode(5)
print validBST(n3),'should be False'
