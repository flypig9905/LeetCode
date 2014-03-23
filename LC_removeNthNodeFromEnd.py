'''

Given a linked list, remove the nth node from the end of list and return its head.

For example,

   Given linked list: 1->2->3->4->5, and n = 2.

   After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:
Given n will always be valid.
Try to do this in one pass.

Created on Jan 14, 2014

@author: Songfan
'''

''' thought: two pointer, faster one is N position beyong the slower one, move both pointer until 
    faster reach the end, then remove the element the slower one points at '''

class ListNode:
    def __init__(self, val = None, next = None):
        self.val = val
        self.next = next
        
    def __str__(self):
        return str(self.val)
    
class LinkedList:
    def __init__(self, head = None):
        self.head = head
        
    def __str__(self):
        return self._display(self.head)
    
    def _display(self, node):
        if node is None: return
        res = []
        while node:
            res.append(str(node.val))
            node = node.next
        return '->'.join(res)
    
def removeFromEnd(head, n):
    p1 = head
    p2 = p1
    for _ in range(n):
        p2 = p2.next
    
    if p2 is None:  
        ''' this means we are trying to remove the first element '''
        return p1.next
    
    while p2.next:
        ''' should check p2.next but not p2 '''
        p1 = p1.next
        p2 = p2.next
        
    p1.next = p1.next.next
    return head

''' unittest LinkedList '''
n5 = ListNode(5)
n4 = ListNode(4, n5)
n3 = ListNode(3, n4)
n2 = ListNode(2, n3)
n1 = ListNode(1, n2)
print LinkedList(n1), 'should be 1->2->3->4->5'


''' unittest remove from end '''
n = removeFromEnd(n1, 1)
print LinkedList(n), 'shoule be 1->2->3->4'

n = removeFromEnd(n1, 4)
print LinkedList(n), 'should be 2->3->4'

n = removeFromEnd(n1, 2)
print LinkedList(n), 'should be 2->4'

