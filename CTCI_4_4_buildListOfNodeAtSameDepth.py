'''
CTCI 4-4
Given a binary search tree, design an alghrithm to create a linked list of all the nodes at each depth

Algorithm: include a depth class variable in TreeNode class, and change the insert method of BST class. Do a depth first search and add the node to the 

Created on Nov 28, 2013
@author: Songfan
'''
from stack import Stack

class TreeNodeWithDepth:
    def __init__(self, value, depth=-1):
        self.value = value
        self.depth = depth
        self.left = None
        self.right = None
        
    def setDepth(self, depth):
        assert(depth>=0),"depth is non negative"
        self.depth = depth
    
    def getDepth(self):
        return self.depth

class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        
    def __str__(self):
        return str(self.value)
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def append(self, value):
        if not self.head:
            self.head = LinkedListNode(value)
        else:
            node = self.head
            while(node.next):
                node = node.next
            node.next = LinkedListNode(value)
            
    def __str__(self):
        result = "LinkedList: "
        if self.head: 
            node = self.head
            result += str(node.value)
            while(node.next):
                node = node.next
                result += '->'+str(node.value)
        return result

class BST:
    def __init__(self):
        self.root = None
        
    def insert(self, value):
        self.root = self._insert(value, self.root, 0)
        
    def _insert(self, value, node, depth):
        if not node:
            n = TreeNodeWithDepth(value, depth)
            return n
        elif value < node.value:
            node.left = self._insert(value, node.left, depth+1)
        else:
            node.right = self._insert(value, node.right, depth+1)
        return node
    
    def buildNodeList(self):
        result = self._buildNodeList(self.root)
        return result
    
    def _buildNodeList(self, node):
        assert(isinstance(node, TreeNodeWithDepth)),"input should be a node."
        result = {}
        s = Stack()
        visitedNode = []
        s.push(node)
        while(not s.isEmpty()):
            currNode = s.pop()
            if currNode not in visitedNode:
                visitedNode.append(node)
                d = currNode.getDepth()
                if d not in result.keys():
                    tmp = LinkedList()
                    tmp.append(currNode.value)
                    result[d] = tmp
                else:
                    result[d].append(currNode.value)
            if currNode.right: s.push(currNode.right)
            if currNode.left: s.push(currNode.left)
        return result
    
    def __str__(self):
        return self._str(self.root)
    
    def _str(self, node):
        if not node: return "*"
        while(node):
            return str(node.value) + ' (' + self._str(node.left) + ',' + self._str(node.right) + ') '
        
# # test Linked List
# aList = LinkedList()
# print aList
# aList.append(3)
# aList.append(2)
# aList.append(4)
# print aList
# 
# # test bst
# t = BST()
# print t
# t.insert(5)
# t.insert(1)
# t.insert(7)
# t.insert(2)
# t.insert(9)
# t.insert(8)
# print t
# print t.root.getDepth()
# print t.root.left.getDepth()
# h = t.buildNodeList()
# for k in h.keys():
#     print h[k]