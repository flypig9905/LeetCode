'''

Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.

Created on Jan 30, 2014

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
        res = str(node.val) + '(' + self._display(node.left) + ',' + self._display(node.right) + ')'
        return res

''' dfs '''
def hasPathSum(root, num):
    if root == None: return False
    if root.left is None and root.right is None:
        if num == root.val: return True
        else: return False

    checkLeft = hasPathSum(root.left, num - root.val)
    checkRight = hasPathSum(root.right, num - root.val)
    return checkLeft or checkRight

    

n1  = TreeNode(1)
n2  = TreeNode(2)
n7  = TreeNode(7)
n13 = TreeNode(13)
n4  = TreeNode(4, None, n1)
n11 = TreeNode(11, n7, n2)
n8  = TreeNode(8, n13, n4)
n4  = TreeNode(4, n11, None)
n5  = TreeNode(5, n4, n8)
print BinaryTree(n5)
    
print hasPathSum(n5, 22), 'should be True'
print hasPathSum(n5, 26), 'should be True'
print hasPathSum(n5, 21), 'should be False'