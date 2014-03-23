'''

Given two binary trees, write a function to check if they are equal or not.

Two binary trees are considered equal if they are structurally identical and the nodes have the same value.

Created on Feb 11, 2014

@author: Songfan
'''

''' recursion '''
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

def solution(n1, n2):
    return checkEqual(n1, n2)

def checkEqual(n1, n2):
    if n1 is None and n2 is None: return True
    if n1 is None or n2 is None: return False
    
    return n1.val == n2.val and checkEqual(n1.left, n2.left) \
        and checkEqual(n1.right, n2.right)

''' unittest '''
n1 = TreeNode(3)
n2 = TreeNode(4)
n3 = TreeNode(5)
n4 = TreeNode(3)
n5 = TreeNode(2, n1, n2)
n6 = TreeNode(2, n3, n4)
n7 = TreeNode(1, n5, n6)
        
n11 = TreeNode(3)
n12 = TreeNode(4)
n13 = TreeNode(5)
n14 = TreeNode(3)
n15 = TreeNode(2, n11, n12)
n16 = TreeNode(2, n13, n14)
n17 = TreeNode(1, n15, n16)
    
print solution(n7, n17), 'should be True'

n18 = TreeNode(8)
n11.left = n18
print solution(n7, n17), 'should be False'
    
    
    
    