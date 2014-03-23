'''

Given a binary tree, return the zigzag level order traversal of its nodes' values. 
(ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree {3,9,20,#,#,15,7},
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]

Created on Jan 28, 2014

@author: Songfan
'''

''' bfs + flip odd level order '''
from binarySearchTree import BinarySearchTree
from queue import Queue

def zigzagLevel(root):
    if root is None: return root
    q = Queue()
    q.enqueue(root)
    level = 0
    q.enqueue('end')
    currLevel = []
    res = []
    while not q.isEmpty():
        tmp = q.dequeue()
        if tmp == 'end':
            if level % 2: # flip odd level
                currLevel = [r for r in currLevel[::-1]]
            level += 1
            res.append(currLevel)
            currLevel = []
            if q.isEmpty(): break  # no more element
            else: q.enqueue('end')
        else:
            currLevel.append(tmp.value)
            if tmp.left:
                q.enqueue(tmp.left)
            if tmp.right:
                q.enqueue(tmp.right)
    for r in res:
        print r

''' unittest '''
bst = BinarySearchTree()
bst.put(6)
bst.put(3)
bst.put(4)
bst.put(7)
bst.put(9)
bst.put(2)
print bst
zigzagLevel(bst.root)