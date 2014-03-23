'''
Given a linked list, swap every two adjacent nodes and return its head.

For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.

Your algorithm should use only constant space. You may not modify the values in the list, 
only nodes itself can be changed.

Created on Jan 12, 2014

@author: Songfan
'''

''' thoughts: running pointer stragegy, change the direction of next pointer for each node '''

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
        res = []
        tmp = self.head
        while(tmp):
            res.append(str(tmp.val))
            tmp = tmp.next
        return '->'.join(res)

def swapNodeInPair(head):
    if head is None or head.next is None: return head
    # swap first two element for init
    ''' this can be improved by creating a dummy node '''
    tmp = head
    head = tmp.next
    tmp.next = head.next
    head.next = tmp
    curr = tmp
    while(curr.next and curr.next.next):
        tmp1 = curr.next
        tmp2 = tmp1.next
        tmp1.next = tmp2.next
        curr.next = tmp2
        tmp2.next = tmp1
        curr = tmp1
    return head

def swapNodeInPair2(head):
    if head is None or head.next is None: return head
    ''' create a dummy node prior to head '''
    dummy = ListNode(-1, head)
    curr = dummy
    while(curr.next and curr.next.next):
        tmp1 = curr.next
        tmp2 = tmp1.next
        tmp1.next = tmp2.next
        curr.next = tmp2
        tmp2.next = tmp1
        curr = tmp1
    return dummy.next

''' unittest '''
n5 = ListNode(5)
n4 = ListNode(4,n5)
n3 = ListNode(3,n4)
n2 = ListNode(2,n3)
n1 = ListNode(1,n2)

A = LinkedList(n1)
print A 

b = swapNodeInPair2(n1)
B = LinkedList(b)
print B

