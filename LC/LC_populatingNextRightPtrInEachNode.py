'''

Given a binary tree

    struct TreeLinkNode {
      TreeLinkNode *left;
      TreeLinkNode *right;
      TreeLinkNode *next;
    }
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Note:

You may only use constant extra space.
You may assume that it is a perfect binary tree (ie, all leaves are at the same level, and every parent has two children).
For example,
Given the following perfect binary tree,
         1
       /  \
      2    3
     / \  / \
    4  5  6  7
After calling your function, the tree should look like:
         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \  / \
    4->5->6->7 -> NULL

Created on Jan 30, 2014

@author: Songfan
'''
from queue import Queue

class TreeNode:
    def __init__(self, val = None, left = None, right = None, next = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
    
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

class LinkedList:
    def __init__(self, head = None):
        self.head = head
        
    def __str__(self):
        return self._display(self.head)
    
    def _display(self, head):
        res = []
        curr = head
        while curr:
            res.append(str(curr.val))
            curr = curr.next
        return '->'.join(res)
        
        
''' intuitively thought about bfs, but bfs is not O(1) space '''
''' solution: dfs + recursion, only works for perfect tree, where next sibling is very easy to find '''
def solution1(node):
    _populate(node)
    
def _populate(node):
    if node is None: return
    if node.left is None and node.right is None: return
    
    if node.next:
        nextSib = node.next.left
    else:
        nextSib = None
    node.left.next = node.right
    node.right.next = nextSib
    _populate(node.left)
    _populate(node.right)

''' version II: not perfect binary tree 
    recursion: curr track the current level, prev track the next level (starting from dummy), 
        since current level has to get all connected, we can use 'while curr' for iteration,
        after done with the current level, recursively call next level, which is dummy.next

'''
def solution2(node):
    _connect(node)
    
def _connect(node):
    if node is None: return
    dummy = TreeNode(-1)
    curr = node
    prev = dummy
    while curr:
        if curr.left:
            prev.next = curr.left
            prev = prev.next
        if curr.right:
            prev.next = curr.right
            prev = prev.next
        curr = curr.next
    _connect(dummy.next)
    

''' unittest version I, perfect binary tree '''
n4 = TreeNode(4)
n5 = TreeNode(5)
n6 = TreeNode(6)
n7 = TreeNode(7)
n2 = TreeNode(2, n4, n5)
n3 = TreeNode(3, n6, n7)
n1 = TreeNode(1, n2, n3)
print BinaryTree(n1)

solution1(n1)
print LinkedList(n1)
print LinkedList(n2)
print LinkedList(n4)

''' unittest version II, non-perfect binary tree '''
n4 = TreeNode(4)
n5 = TreeNode(5)
n7 = TreeNode(7)
n2 = TreeNode(2, n4, n5)
n3 = TreeNode(3, None, n7)
n1 = TreeNode(1, n2, n3)
print BinaryTree(n1)

solution2(n1)
print LinkedList(n1)
print LinkedList(n2)
print LinkedList(n4)
