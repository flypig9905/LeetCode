'''
CTCI p86 4-2, N8
Given a sorted (increasing order) array with unique integer elements, write a algorithm to create a binary search tree with minimum height


Created on Nov 25, 2013

@author: Songfan
'''
class TreeNode:
    def __init__(self,value):
        self.left = None
        self.right = None
        self.value = value
    
    def __str__(self):
        return str(self.value)
    
class BST:
    def __init__(self):
        self.root = None
        
    def buildBSTFromSortedArray(self, A):
        self.root = self._BSTFromSortedArray(A)
        
    def _BSTFromSortedArray(self,A):
        if len(A)==0:
            return
        elif len(A)==1:
            return TreeNode(A[0])
        else:
            mid = len(A)//2
            n = TreeNode(A[mid])
            n.left = self._BSTFromSortedArray(A[:mid])
            n.right = self._BSTFromSortedArray(A[mid+1:])
            return n
        
        
    def insert(self, value):
        self.root = self._insert(self.root, value)
        
            
    def _insert(self, node, value):
        if not node:
            return TreeNode(value)
        elif value < node.value:
            node.left = self._insert(node.left, value)
        else:
            node.right =  self._insert(node.right, value)
        return node
            
        
        
    def __str__(self):
        return self._getStr(self.root)
        
    def _getStr(self, node):
        if not node:
            return "*"
        else:
            while(node):
                return str(node.value) + " (" + self._getStr(node.left) + "," + self._getStr(node.right) + ") "
            
            
t = BST()
print t
t.insert(5)
t.insert(9)
t.insert(3)
t.insert(12)
print t

aList = [1,2,3,4,5,6]
b = BST()
b.buildBSTFromSortedArray(aList)
print b            
        
    