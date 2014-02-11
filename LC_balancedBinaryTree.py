'''
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



''' recursion, dfs, check balance for both left and right '''

def solution(node):
    return checkBalance(node) >= 0

def checkBalance(node):
    if node is None: return 0
    leftHeight = checkBalance(node.left)
    rightHeight = checkBalance(node.right)
    
    # pruning
    if leftHeight < 0 or rightHeight < 0 or abs(leftHeight - rightHeight) > 1:
        return -1
    
    return 1 + max(leftHeight, rightHeight)
    
    
n1 = TreeNode(3)
n2 = TreeNode(4)
n3 = TreeNode(4)
n4 = TreeNode(3)
n5 = TreeNode(2, n1, n2)
n6 = TreeNode(2, n3, n4)
n7 = TreeNode(1, n5, n6)
print BinaryTree(n7)
print solution(n7), 'should be True'


n11 = TreeNode(1)
n12 = TreeNode(2, n11)
n13 = TreeNode(3, None, n12)
n14 = TreeNode(4)
n15 = TreeNode(5, n13, n14)
print BinaryTree(n15)
print solution(n15), 'should be False'
