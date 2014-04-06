'''
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

confused what "{1,#,2,3}" means? 
OJ's Binary Tree Serialization:
The serialization of a binary tree follows a level order traversal, where '#' signifies a path terminator where no node exists below.

Here's an example:
   1
  / \
 2   3
    /
   4
    \
     5
The above binary tree is serialized as "{1,2,3,#,#,4,#,#,5}".

Created on Jan 2, 2014

@author: Songfan
'''

''' algorithm: recursive solution '''
import sys

class TreeNode:
    def __init__(self, val = None):
        self.val = val
        self.left = None
        self.right = None
        
    def __str__(self):
        return str(self.val)
    

def isValidBST(root):
    def helper(node, lo, hi):
        if node is None: return True
        if lo < node.val and node.val < hi:
            return helper(node.left, lo, node.val) and \
                helper(node.right, node.val, hi)
        else:
            return False
    return helper(root, -2**32, 2**32)
    
    
n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)
n5 = TreeNode(5)
n3.left = n1
n1.right = n2
n3.right = n4
n4.right = n5

print isValidBST(n1)

