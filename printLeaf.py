'''
print the leaf of a binary tree

Created on Mar 23, 2014

@author: Songfan
'''

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
        return str(node.val) + '(' + self._display(node.left) + ',' + self._display(node.right) + ')'

def printLeaf(node):
    if node is None: return []
    if node.left is None and node.right is None: return [node.val]
    return printLeaf(node.left) + printLeaf(node.right)


''' unittest '''
n2 = TreeNode(2)
n4 = TreeNode(4)
n5 = TreeNode(5)
n3 = TreeNode(3, n4, n5)
n1 = TreeNode(1, n2, n3)
print BinaryTree(n1)
print printLeaf(n1)