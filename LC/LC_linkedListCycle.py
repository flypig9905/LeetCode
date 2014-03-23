'''

Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?

Created on Feb 16, 2014

@author: Songfan
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        faster = head
        slower = head
        while faster and faster.next:
            faster = faster.next.next
            slower = slower.next
            if faster == slower:
                return True
        return False