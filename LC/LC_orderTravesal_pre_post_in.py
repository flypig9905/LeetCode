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
def postOrderRecur(root):
    if not root: return
    postOrderRecur(root.left)
    postOrderRecur(root.right)
    print root.value
    
    
def postOrderIter(root):
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
    if root is None: return
    s = Stack()
    s.push(root)
    prev = None
    while not s.isEmpty():
        curr = s.peek()
        # traverse down
        if prev is None or prev.left == curr or prev.right == curr:
            if curr.left: s.push(curr.left)
            if curr.right: s.push(curr.right)
        # traverse up from left
        elif prev == curr.left:
            if curr.right: s.push(curr.right)
        # traverse up from right
        else:
            print curr.value
            s.pop()
        prev = curr


def postOrderIter2(root):
    ''' 
    post order iterative: two stack solution
    two stacks: s1 and s2
    push root to s1
    while s1:
        tmp = pop from s1
        push tmp it to s2
        push tmp.left to s1
        push tmp.right to s2
    when s1 is empty, s2 has all the nodes in post order
    '''
    if root is None: return
    s1, s2 = Stack(), Stack()
    s1.push(root)
    while not s1.isEmpty():
        tmp = s1.pop()
        s2.push(tmp)
        if tmp.left: s1.push(tmp.left)
        if tmp.right: s1.push(tmp.right)
    # retrieve node from s2
    res = []
    while not s2.isEmpty():
        res.append(s2.pop().value)
    print res

def inOrderIter(root):
    if root is None: return
    s, finished, curr, res = Stack(), False, root, []
    while not finished:
        if curr:
            s.push(curr)
            curr = curr.left
        else:
            if s.isEmpty(): finished = True
            else:
                curr = s.pop()
                res.append(curr.value)
                curr = curr.right
    print res


def inOrderRecur(root):
    res = []
    _inOrder(root, res)
    res = ' '.join(res)
    print res

def _inOrder(root, res):
    if root is None: return root
    _inOrder(root.left, res)
    res.append(str(root.value))
    _inOrder(root.right, res)


def preOrderIter(root):
    ''' a much easier way, use a stack, push right first and then push left '''
    if not root: return
    s = Stack()
    s.push(root)
    while not s.isEmpty():
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
print '==== post recur ===='
postOrderRecur(bst.root)
print '==== post iter===='
postOrderIter(bst.root)
print '==== post iter 2===='
postOrderIter2(bst.root)
print '==== pre iter===='
preOrderIter(bst.root)
print '==== in recur===='
inOrderRecur(bst.root)
print '==== in iter===='
inOrderIter(bst.root)