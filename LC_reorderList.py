'''

Given a singly linked list L: L0->L1->...->Ln-1->Ln,
reorder it to: L0->Ln->L1->Ln-1->L2->Ln-2->...

You must do this in-place without altering the nodes' values.

For example,
Given {1,2,3,4}, reorder it to {1,4,2,3}.

Created on Feb 15, 2014

@author: Songfan
'''
'''
separate list from the middle, reverse the second part, and combine

1. Find the middle node (use the slow/fast pointers)
2  Reverse the second part of the linked list (from middle->next to tail)
3  Combine
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
    def __str__(self):
        return str(self.val)

class Solution:
    # @param head, a ListNode
    # @return nothing
    def reorderList(self, head):
        if head is None or head.next is None or head.next.next is None:
            # no ops needed for less than 2 nodes
            return head
        
        # find middle
        faster = head
        slow = head
        while faster.next and faster.next.next:
            slow = slow.next
            faster = faster.next.next
        mid = slow
        
        # reverse mid to tail
        mid.next = self.reverse(mid.next)
        
        # combine
        front = head
        rear = mid.next
        mid.next = None
        head = self.combine(front, rear)
            
        return head
        
    def reverse(self, head):
        if head is None or head.next is None: return head
        dummy = ListNode(-1)
        dummy.next = head
        curr = head
        while curr.next:
            tmp = dummy.next
            dummy.next = curr.next
            curr.next = dummy.next.next
            dummy.next.next = tmp
        return dummy.next
            
    
    def combine(self, node1, node2):
        ret = node1
        cur1 = node1
        cur2 = node2
        while cur2:
            tmp = cur1.next
            cur1.next = cur2
            cur2 = cur2.next
            cur1.next.next = tmp
            cur1 = tmp    
        return ret
        
        
        
    
n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)
n6 = ListNode(6)
n7 = ListNode(7)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6
n6.next = n7


ss = Solution()
n = ss.reorderList(n1)
curr = n
while curr:
    print curr.val
    curr = curr.next
        
        
        
        