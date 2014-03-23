'''

DFS and BFS on binary search tree

Created on Jan 4, 2014

@author: Songfan
'''
from binarySearchTree import BinarySearchTree
from stack import Stack
from queue import Queue

def dfsIterative(node):
    visitedNode = []
    if node is None: return visitedNode
    s = Stack()
    s.push(node)
    while not s.isEmpty():
        tmp = s.pop()
        visitedNode.append(tmp.value)
        if tmp.left is not None:
            s.push(tmp.left)
        if tmp.right is not None:
            s.push(tmp.right)
    return visitedNode

def dfsRecursive(node):
    visitedNode = []
    return _dfsRecur(node, visitedNode)

def _dfsRecur(node, visitedNode):
    if node is None: return
    visitedNode.append(node.value)
    _dfsRecur(node.left, visitedNode)
    _dfsRecur(node.right, visitedNode)
    return visitedNode
        
def bfsIterative(node):
    if node is None: return []
    visitedNode = []
    q = Queue()
    q.enqueue(node)
    while(not q.isEmpty()):
        tmp = q.dequeue()
        visitedNode.append(tmp.value)
        if tmp.left and tmp.left.value not in visitedNode:
            q.enqueue(tmp.left)
        if tmp.right and tmp.right.value not in visitedNode:
            q.enqueue(tmp.right)
    return visitedNode
        
        
        
    
    

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