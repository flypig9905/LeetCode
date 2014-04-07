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

class Solution:
    # @param root, a tree node
    # @return an integer
    def minDepth(self, root):
        if root is None: return 0
        if root.left is None and root.right is None: return 1
        
        if root.left is None:
            return self.minDepth(root.right) + 1
        elif root.right is None:
            return self.minDepth(root.left) + 1
        else:
            return min(self.minDepth(root.left), self.minDepth(root.right)) + 1


''' unittest '''
n1 = TreeNode(1)
n3 = TreeNode(3)
n4 = TreeNode(4)
n5 = TreeNode(5, n1)
n6 = TreeNode(6, n3, n4)
n7 = TreeNode(7, n5, n6)
print BinaryTree(n7)
ss = Solution()
print ss.minDepth(n7),'should be 3'   

n12 = TreeNode(2)
n11 = TreeNode(1, n12)
print ss.minDepth(n11), 'should be 2'