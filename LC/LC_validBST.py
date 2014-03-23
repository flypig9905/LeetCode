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
    if not root: return True
    if root.left:
        leftVal = root.left.val
    else:
        ''' caveat: set up upper and lower bound for left and right value '''
        leftVal = -sys.maxint
    if root.right:
        rightVal = root.right.val
    else:
        rightVal = sys.maxint
    return root.val > leftVal and root.val < rightVal and isValidBST(root.left) and isValidBST(root.right)
    
    
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

