'''

Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
return
[
   [5,4,11,2],
   [5,8,4,5]
]

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
    
''' need to store every possible result, has two vars, one store the tmp solution, and one store the entire result '''
   
def pathSum(root, num):
    res = []
    currSolu = []
    _pathSum(root, num, currSolu, res)
    return res

def _pathSum(node, num, currSolu, res):
    if node.left is None and node.right is None and node.val == num:
        ''' stop condition '''
        currSolu.append(num)
        tmp = currSolu[:]
        res.append(tmp)
        return
    
    currSolu.append(node.val)
    if node.left:
        _pathSum(node.left, num - node.val, currSolu, res)
        currSolu.pop()
    if node.right:
        _pathSum(node.right, num - node.val, currSolu, res)
        currSolu.pop()
    return
    
    

n1  = TreeNode(1)
n2  = TreeNode(2)
n7  = TreeNode(7)
n13 = TreeNode(13)
n51 = TreeNode(5)
n4  = TreeNode(4, n51, n1)
n11 = TreeNode(11, n7, n2)
n8  = TreeNode(8, n13, n4)
n4  = TreeNode(4, n11, None)
n5  = TreeNode(5, n4, n8)
print BinaryTree(n5)

res = pathSum(n5, 22)
print res