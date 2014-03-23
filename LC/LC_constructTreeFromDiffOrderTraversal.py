'''

Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

Created on Jan 29, 2014

@author: Songfan
'''

''' recursion '''

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
    
    def _display(self, root):
        if root is None: return '*'
        result = str(root.val) + '(' + self._display(root.left) + ',' + self._display(root.right) + ')'
        return result

''' caveat: find root, partition, divide and conquar '''
def constructTreeFromInAndPost(InOrder, PostOrder):
    if len(InOrder) == 0 or len(PostOrder) == 0: return None
    
    # the root is the last item in post order list, find it in inorder list for partition
    currRootVal = PostOrder[-1]
    pivotIn = InOrder.index(currRootVal)
    InOrderLeft = InOrder[:pivotIn]
    InOrderRight = InOrder[pivotIn+1:]
    leftSize = pivotIn
    
    ''' partition post order list based on leftSize '''
    PostOrderLeft = PostOrder[:leftSize]
    PostOrderRight = PostOrder[leftSize:-1]
    
    # construct the tree recursively
    currRoot = TreeNode(currRootVal)
    currRoot.left = constructTreeFromInAndPost(InOrderLeft, PostOrderLeft)
    currRoot.right = constructTreeFromInAndPost(InOrderRight, PostOrderRight)
    
    return currRoot
    
    
def constructTreeFromInAndPre(InOrder, PreOrder):
    if len(InOrder) == 0 or len(PreOrder) == 0: return None
    
    # the root is the last item in post order list, find it in inorder list for partition
    currRootVal = PreOrder[0]
    pivotIn = InOrder.index(currRootVal)
    InOrderLeft = InOrder[:pivotIn]
    InOrderRight = InOrder[pivotIn+1:]
    leftSize = pivotIn
    
    ''' partition post order list based on leftSize '''
    PreOrderLeft = PreOrder[1:leftSize+1]
    PreOrderRight = PreOrder[leftSize+1:]
    
    # construct the tree recursively
    currRoot = TreeNode(currRootVal)
    currRoot.left = constructTreeFromInAndPre(InOrderLeft, PreOrderLeft)
    currRoot.right = constructTreeFromInAndPre(InOrderRight, PreOrderRight)
    
    return currRoot


''' unittest BinayTree '''
n4 = TreeNode(4)
n5 = TreeNode(5)
n6 = TreeNode(6)
n2 = TreeNode(2, None, n4)
n3 = TreeNode(3, n5, n6)
n1 = TreeNode(1, n2, n3)
print BinaryTree(n1)        

''' unittest constructTreeFromInAndPost '''
InOrder = [2,4,1,5,3,6]
PostOrder = [4,2,5,6,3,1]        
n = constructTreeFromInAndPost(InOrder, PostOrder)
print BinaryTree(n)


''' unittest constructTreeFromInAndPost '''
InOrder = [2,4,1,5,3,6]
PreOrder = [1,2,4,3,5,6]
n = constructTreeFromInAndPre(InOrder, PreOrder)
print BinaryTree(n)
