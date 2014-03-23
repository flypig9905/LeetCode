'''

Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree {3,9,20,#,#,15,7},
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7]
  [9,20],
  [3],
]

Created on Feb 11, 2014

@author: Songfan
'''
from queue import Queue

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
        return str(node.val) + ' ( ' + self._display(node.left) + ' , ' + self._display(node.right) + ' ) '

''' bfs. add dummy variable at the end of each level '''

def solution(root):
    if root is None: return []
    q = Queue()
    q.enqueue(root)
    q.enqueue('EndLevel')
    res = []
    tmpRes = []
    while not q.isEmpty():
        tmp = q.dequeue()
        if tmp == 'EndLevel':
            res.append(tmpRes)
            tmpRes = []
            if not q.isEmpty():
                # otherwise infinite loop
                q.enqueue('EndLevel')
        else:
            tmpRes.append(tmp.val)
            if tmp.left: q.enqueue(tmp.left)
            if tmp.right: q.enqueue(tmp.right)
            
    return res[::-1]

''' unittest '''
n1 = TreeNode(3)
n3 = TreeNode(5)
n4 = TreeNode(3)
n5 = TreeNode(2, n1)
n6 = TreeNode(2, n3, n4)
n7 = TreeNode(1, n5, n6)    
print BinaryTree(n7)

print solution(n7), 'should be [[3, 5, 3],[2, 2],[1]]'
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    