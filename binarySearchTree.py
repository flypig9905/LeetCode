'''
Created on Nov 7, 2013

@author: Songfan
'''
from treeNode import TreeNode
from queue import Queue
class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0
    
    def isEmpty(self):
        return self.root is None
    
    def getSize(self):
        return self.size
    
    def put(self, value):
        ''' assign to root '''
        self.root = self._put(self.root, value)
    
    def _put(self, currentNode, value):
        if currentNode is None:
            self.size += 1
            ''' create a new node here '''
            return TreeNode(value)
        if value < currentNode.value:
            ''' remember to assign to left child '''
            currentNode.left = self._put(currentNode.left, value)
        elif value > currentNode.value:
            currentNode.right = self._put(currentNode.right, value)
        else:
            currentNode.value = value
        return currentNode
    
    def get(self, value):
        return self._get(self.root, value)
        
    def _get(self, currentNode, value):
        if not currentNode:
            return None
        if value == currentNode.value:
            return currentNode.value
        elif value < currentNode.value:
            return self._get(currentNode.left, value)
        else:
            return self._get(currentNode.right, value)
            
    def __getitem__(self, value): # make the interface look like dictionary: a = bst[key]
        return self.get(value)
    
    def delMin(self):
        self.root = self._delMin(self.root)
    
    def _delMin(self, currentNode):
        if not currentNode.left:
            self.size -= 1
            return currentNode.right
        currentNode.left = self._delMin(currentNode.left)   # Diao Bao!!!!
        return currentNode
    
    def __str__(self):
        return self._getStr(self.root)
        
    def _getStr(self, node):
        if not node:
            return "*"
        else:
            while(node):
                return str(node.value) + " (" + self._getStr(node.left) + "," + self._getStr(node.right) + ") "
    
    # leetCode: find minimum depth of the tree
    def minDepth(self):
        return self._minDepth(self.root)
    
    def _minDepth(self,node):
        depth = 0
        if not node: return depth
        q = Queue()
        q.enqueue(node)
        while(q):
            n = q.dequeue()
            depth+=1
            if n.left: q.enqueue(n.left)
            else: return depth
            if n.right: q.enqueue(n.right)
            else: return depth
                
bst = BinarySearchTree()
 
# print bst.get(2)
bst.put(20)
bst.put(12)
bst.put(21)
bst.put(23)
print bst
print bst.minDepth()
# print bst.get(2)
# print bst.get(3)
a = bst[20]
print a
bst.delMin()
print bst
print bst.minDepth()