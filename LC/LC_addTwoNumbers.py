'''

You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. 
Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8

Created on Jan 5, 2014

@author: Songfan
'''

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

    def __str__(self):
        return str(self.val)

def addTwoNumbers(n1, n2):
    if n1 is None: return n2
    if n2 is None: return n1
    c1 = n1
    c2 = n2
    c3 = None
    carry = False
    while(c1 or c2):
        ''' caveat: c1 or c2, not care if one point reach the end, this will simplify the procedure ''' 
        if c1: v1 = c1.val
        else: v1 = 0
        if c2: v2 = c2.val
        else: v2 = 0
        
        # compute value for current digit and carry over
        if carry: tmpVal = v1 + v2 + 1
        else: tmpVal = v1 + v2
        tmpNode = ListNode(tmpVal % 10)
        if tmpVal >= 10: carry = True
        else: carry = False
        
        # if c3 is not init, this mean the head is not yet set
        if c3 is None:
            resHead = tmpNode
            c3 = resHead
        else:
            c3.next = tmpNode
            c3 = c3.next
        
        # update running pointer
        if c1: c1 = c1.next
        if c2: c2 = c2.next
    if c1 is None and c2 is None and carry:
        ''' this means we have to create a new Node represents a new digit '''
        c3.next = ListNode(1)
    
    return resHead

def displayList(n):
    result = []
    while(n):
        result.append(str(n.val))
        n = n.next
    print '->'.join(result)

''' unittest '''
n1 = ListNode(2)
n2 = ListNode(4)
n3 = ListNode(3)
n1.next = n2
n2.next = n3

n4 = ListNode(5)
n5 = ListNode(6)
n6 = ListNode(4)
n7 = ListNode(1)
n4.next = n5
n5.next = n6
n6.next = n7 

n = addTwoNumbers(n1, n4)
displayList(n)
print 'should be 7->0->8->1'
print

''' unittest '''
n1 = ListNode(9)
n2 = ListNode(9)
n1.next = n2

n4 = ListNode(9)
n5 = ListNode(9)
n6 = ListNode(9)
n4.next = n5
n5.next = n6

n = addTwoNumbers(n1, n4)
displayList(n)
print 'should be 8->9->0->1'
print