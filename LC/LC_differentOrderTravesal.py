'''
Binary Tree Postorder Traversal

Given a binary tree, return the postorder traversal of its nodes' values.

note: for easy adding purpose, use binary search tree

Created on Dec 13, 2013

@author: Songfan
'''
from binarySearchTree import BinarySearchTree
from stack import Stack
# recursive solution
def postOrderTravesal(root):
    if not root: return
    if root.left:
        postOrderTravesal(root.left)
    if root.right:
        postOrderTravesal(root.right)
    print root.value
    
''' iterative solution 
We use a prev variable to keep track of the previously-traversed node. Lets assume curr is the current 
node thats on top of the stack. When prev is currs parent, we are traversing down the tree. 
In this case, we try to traverse to currs left child if available (ie, push left child to the stack). 
If it is not available, we look at currs right child. If both left and right child do not exist (ie, curr is a leaf node), 
we print currs value and pop it off the stack.

If prev is curr left child, we are traversing up the tree from the left. We look at curr right child. 
If it is available, then traverse down the right child (ie, push right child to the stack), otherwise print curr value and pop it off the stack.

If prev is curr right child, we are traversing up the tree from the right. In this case, we print curr value and pop it off the stack.
'''
    
def postOrderTravesalIter(root):
    if not root: return
    s = Stack();
    s.push(root);
    prev = None
    while (not s.isEmpty()):
        curr = s.peek()
    # we are traversing down the tree
        if (not prev or prev.left == curr or prev.right == curr):
            if (curr.left):
                s.push(curr.left)
            elif (curr.right):
                s.push(curr.right)
            else:
                print curr.value
                s.pop()
            
        # we are traversing up the tree from the left
        elif (curr.left == prev):
            if (curr.right):
                s.push(curr.right)
            else:
                print curr.value
                s.pop()
    
        # we are traversing up the tree from the right
        elif (curr.right == prev):
            print curr.value
            s.pop()
        
        prev = curr  # record previously traversed node


def preOrderTravesalIter(root):
    ''' follow the same logic as postOrder '''
    if not root: return
    s = Stack()
    s.push(root)
    prev = None
    while(not s.isEmpty()):
        curr = s.peek()
        if not prev or curr==prev.left or curr==prev.right:
            print curr.value
            if curr.left:
                s.push(curr.left)
            elif curr.right:
                s.push(curr.right)
            else:
                s.pop()
        
        elif curr.left==prev:
            if curr.right:
                s.push(curr.right)
            else:
                s.pop()
                
        elif curr.right==prev:
            s.pop()
        prev = curr
        

def preOrderTravesalIter2(root):
    ''' a much easier way, use a stack, push right first and then push left '''
    if not root: return
    s = Stack()
    s.push(root)
    while(not s.isEmpty()):
        curr = s.pop()
        print curr.value
        if curr.right:
            s.push(curr.right)
        if curr.left:
            s.push(curr.left)
    
bst = BinarySearchTree()
bst.put(6)
bst.put(3)
bst.put(4)
bst.put(7)
bst.put(9)
bst.put(2)
print bst
# postOrderTravesal(bst.root)
postOrderTravesalIter(bst.root)
print '========'
preOrderTravesalIter(bst.root)
print '========'
preOrderTravesalIter2(bst.root)