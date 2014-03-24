'''

Given a binary tree, flatten it to a linked list in-place.

For example,
Given

         1
        / \
       2   5
      / \   \
     3   4   6
The flattened tree should look like:
   1
    \
     2
      \
       3
        \
         4
          \
           5
            \
             6

Created on Jan 31, 2014

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
   
        
''' recursion: root.right = flatten(root.left, tail) with the tail pointing to flatten(root.right)) 
    O(N) time, O(logN) space ?
'''
   
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return nothing, do it in place
    def flatten(self, root):
        return self._flatten(root, None)
    
    def _flatten(self, root, tail):
        if root is None:
            ''' this means the current node does not have left child, simply return the tail pointer which represents the flatten version right child ''' 
            return tail
        
        root.right = self._flatten(root.left, self._flatten(root.right, tail))
        root.left = None
        return root 




n3 = TreeNode(3)
n4 = TreeNode(4)
n6 = TreeNode(6)
n2 = TreeNode(2, n3, n4)
n5 = TreeNode(5, None, n6)
n1 = TreeNode(1, n2, n5)
print BinaryTree(n1)
ss = Solution()
print BinaryTree(ss.flatten(n1))