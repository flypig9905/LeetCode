'''

Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

For example,

    1
   / \
  2   3
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.

Return the sum = 12 + 13 = 25.

Created on Jan 14, 2014

@author: Songfan
'''

''' thought: dfs, add value to sum when leaf '''

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
        

def sumRoot2Leaf(root):
    return _dfs(root, 0)

def _dfs(root, numSum):
    if root is None: return 0
    if root.left is None and root.right is None:
        ''' add the leaf value '''
        numSum = numSum * 10 + root.val
        return numSum
    else:
        ''' recursive call, add 10 * sum to the current sum '''
        numSum = _dfs(root.left, numSum * 10 + root.val) + _dfs(root.right, numSum * 10 + root.val)
        return numSum
        
    
n4 = TreeNode(4)
n6 = TreeNode(6)
n2 = TreeNode(2)
n3 = TreeNode(3, n4, n6)
n1 = TreeNode(1, n2, n3)
b = BinaryTree(n1)
print b
print sumRoot2Leaf(n1), 'should be 282'