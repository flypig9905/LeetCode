'''

Given a sorted linked list, delete all duplicates such that each element appear only once.

For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.

Created on Jan 27, 2014

@author: Songfan
'''
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
        cur = self.head
        res = []
        while cur:
            res.append(str(cur.val))
            cur = cur.next
        return '->'.join(res)


def solution(node):
    if node is None: return node
    p1 = node   # slow pointer
    p2 = node.next   # running pointer
    while p2:
        if p2.val == p1.val: 
            p2 = p2.next
        else:
            p1.next = p2
            p1 = p2
            p2 = p2.next
    ''' remember to take care this case: when p2 reaches the end, set the p1.next to None to remove the dups in the end '''
    p1.next = p2
    return node



''' unittest '''
n5 = ListNode(3)
n4 = ListNode(3, n5)
n3 = ListNode(2, n4)
n2 = ListNode(1, n3)
n1 = ListNode(1, n2)
print n5, 'should be 3'
L = LinkedList(n1)
print L, 'should be 1->1->2->3->3'

L1 = solution(n1)
print LinkedList(L1), 'should be 1->2->3'

