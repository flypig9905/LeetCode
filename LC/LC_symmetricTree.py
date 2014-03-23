'''

Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following is not:
    1
   / \
  2   2
   \   \
   3    3

Created on Feb 10, 2014

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


''' recursion '''
def solution(node):
    if node is None: return
    return checkSymm(node.left, node.right)

def checkSymm(n1, n2):
    if n1 is None and n2 is None: return True
    return n1.val == n2.val and \
        checkSymm(n1.left, n2.right) and \
        checkSymm(n1.right, n2.left)

''' iterative: BFS, check the symmetric requirement is meet for every level '''

n1 = TreeNode(3)
n2 = TreeNode(4)
n3 = TreeNode(4)
n4 = TreeNode(3)
n5 = TreeNode(2, n1, n2)
n6 = TreeNode(2, n3, n4)
n7 = TreeNode(1, n5, n6)
print BinaryTree(n7)
print solution(n7), 'should be True'