'''

Two elements of a binary search tree (BST) are swapped by mistake.

Recover the tree without changing its structure.

Note:
A solution using O(n) space is pretty straight forward. Could you devise a constant space solution?

Created on Feb 10, 2014

@author: Songfan
'''

''' O(N) space: in order traversal, this should result in increasing list for bst. Based on this observation, use pointer to record the element that should be swaped during traversal, 
    This is O(N) space because the recursive call will store the current state in a stack.
    
    O(1) space: use Morris inorder traversal, not very suitable for an interview question 
    
    The O(N) solution is provided here
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
        return str(node.val) + '(' + self._display(node.left) + ',' + self._display(node.right) + ')'
        
        

def solution(node):
    prev = None
    res = inorder(node, prev, [None, None])
    if res[0] and res[1]:
        res[0].val, res[1].val = res[1].val, res[0].val
    return node
 
def inorder(node, prev, res):
    if node is None: return
    ''' traverse to the left most element '''
    inorder(node.left, prev, res)
    if prev and prev.val > node.val:
        ''' violate the increasing order '''
        res[1] = node
        if res[0] is None:
            ''' if two elements are next to each other, this is way to capture element n1 and n2,
                if two elements are apart from each other, we only need to change n2 '''
            res[0] = prev
    prev = node
    inorder(node.right, prev, res)
    return res

''' unittest '''
n1 = TreeNode(1)
n3 = TreeNode(3)
n2 = TreeNode(2)
n7 = TreeNode(7)
n5 = TreeNode(5, n1, n3)
n6 = TreeNode(6, n2, n7)
n4 = TreeNode(4, n5, n6)
print BinaryTree(n4)

print BinaryTree(solution(n4))