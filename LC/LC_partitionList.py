'''

Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

For example,
Given 1->4->3->2->5->2 and x = 3,
return 1->2->2->4->3->5.

Created on Jan 28, 2014

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
    



''' three pointer algorithm: 
    1. vars
        leftDummy node pointed to the head of left part; rightDummy node pointed to the head of right part
        leftCurr node pointed to the current node of left part; rightCurr node pointed to the current node of right part
        curr is the running pointer
    2. procedure
        leftDummy and rightDummy are init to be floating ListNode, cur from head
        for every node that curr points at:
            if curr.val < t: increment leftCurr
            else: increment rightCurr
        set leftCurr.next to rightDummy.next
        set rightCurr.next to None
        return leftDummy

'''
class Solution:
    # @param head, a ListNode
    # @param x, an integer
    # @return a ListNode
    def partition(self, node, t):
        if node is None or node.next is None: return node
        leftDummy = ListNode(-1)
        rightDummy = ListNode(-1)
        leftCurr = leftDummy
        rightCurr = rightDummy
        curr = node
        while curr:
            if curr.val < t:
                leftCurr.next = curr
                leftCurr = curr
            else:
                rightCurr.next = curr
                rightCurr = curr
            curr = curr.next
        leftCurr.next = rightDummy.next
        rightCurr.next = None
        return leftDummy.next
    
''' unittest '''
n5 = ListNode(1)
n4 = ListNode(4, n5)
n3 = ListNode(2, n4)
n2 = ListNode(2, n3)
n1 = ListNode(3, n2)
print LinkedList(n1), 'should be 3->2->2->4->1'
ss = Solution()
n = ss.partition(n1, 3)
print LinkedList(n), 'should be 2->2->1->3->4'