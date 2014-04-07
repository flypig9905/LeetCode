'''

DFS and BFS on binary search tree

Created on Jan 4, 2014

@author: Songfan
'''
from binarySearchTree import BinarySearchTree
from stack import Stack
from queue import Queue

def dfsIterative(node):
    res = []
    if node is None: return res
    s = Stack()
    s.push(node)
    while not s.isEmpty():
        tmp = s.pop()
        res.append(tmp.value)
        if tmp.right is not None: s.push(tmp.right)
        if tmp.left is not None: s.push(tmp.left)
    return res

def dfsRecursive(node):
    return _dfsRecur(node, [])

def _dfsRecur(node, res):
    if node is None: return
    res.append(node.value)
    _dfsRecur(node.left, res)
    _dfsRecur(node.right, res)
    return res
        
def bfsIterative(node):
    if node is None: return []
    res = []
    q = Queue()
    q.enqueue(node)
    while not q.isEmpty():
        tmp = q.dequeue()
        res.append(tmp.value)
        if tmp.left: q.enqueue(tmp.left)
        if tmp.right: q.enqueue(tmp.right)
    return res
        
        
        
    
    

bst = BinarySearchTree()
bst.put(5)
bst.put(2)
bst.put(4)
bst.put(3)
bst.put(1)
bst.put(8)
bst.put(7)
bst.put(9)
print bst

print 'dfs iterative: ', dfsIterative(bst.root)
print 'dfs recursive: ', dfsRecursive(bst.root)
print 'bfs iterative: ', bfsIterative(bst.root)