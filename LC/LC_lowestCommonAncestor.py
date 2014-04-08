'''
Created on Apr 7, 2014

@author: Songfan
'''

def LCA(root, n1, n2):
    if root is None: return
    if root == n1 or root == n2: return root
    left = LCA(root.left, n1, n2)
    right = LCA(root.right, n1, n2)
    if left and right: 
        return root
    else:
        return left or right
    
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
    def __str__(self):
        return str(self.val)
        
n1 = TreeNode(3)
n2 = None
print n1 or n2
