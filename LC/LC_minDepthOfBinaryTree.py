'''

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Created on Feb 11, 2014

@author: Songfan
'''

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
        if node is None: return '*'
        return str(node.val) + '(' + self._display(node.left) + ',' + self._display(node.right) + ')'

def solution(node):
    return maxHeight(node)

def maxHeight(node):
    if node is None: return 0
    return min(maxHeight(node.left) + 1, maxHeight(node.right) + 1)


''' unittest '''
n1 = TreeNode(3)
n3 = TreeNode(5)
n4 = TreeNode(3)
n5 = TreeNode(2, n1)
n6 = TreeNode(2, n3, n4)
n7 = TreeNode(1, n5, n6)

print solution(n7),'should be 2'   