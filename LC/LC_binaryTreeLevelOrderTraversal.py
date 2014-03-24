'''

Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree {3,9,20,#,#,15,7},
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
confused what "{1,#,2,3}" means? > read more on how binary tree is serialized on OJ.


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

Created on Jan 13, 2014

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


''' BFS + sentinal '''

''' recursion + hashtable '''
def levelOrderTraversal(root):
    h = {}
    _levelOrderTraversal(root, 1, h)
    # organize result
    i = 1
    res = []
    while i in h:
        res.append(h[i])
        i += 1
    return res

def _levelOrderTraversal(root, level, h):
    if root is None: return None
    h[level] = h.get(level, [])
    h[level].append(root.val)
    _levelOrderTraversal(root.left, level + 1, h)
    _levelOrderTraversal(root.right, level + 1, h)
    


n15 = TreeNode(15)
n7 = TreeNode(7)
n20 = TreeNode(20, n15, n7)
n9 = TreeNode(9)
n3 = TreeNode(3, n9, n20)
b = BinaryTree(n3)
print b

print levelOrderTraversal(n3)