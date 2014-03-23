'''

Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

For example,
Given 1->2->3->3->4->4->5, return 1->2->5.
Given 1->1->1->2->3, return 2->3.

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


''' recursion '''
class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, node):
        return self._removeDup(node)

    def _removeDup(self, node):
        if node is None or node.next is None: return node
        if node.val == node.next.val:
            ''' move to the next non-dup node '''
            while node.next and node.next.val == node.val:
                node = node.next
            return self._removeDup(node.next)
        else:
            node.next = self._removeDup(node.next)
            return node


''' iteration (incomplete): very hard to implement, don't try this!!! '''
# def solution1(node):
#     if node is None or node.next is None: return node
#     dummy = ListNode(-1)
#     ''' pointer track previous non-dup position '''
#     p1 = dummy  
#     p2 = node   # running pointer
#     while p2 and p2.next:
#         if p2.val == p2.next.val:
#             ''' move p to the next non-dup node, set p1 to this position, update p2 '''
#             while p2.next and p2.next.val == p2.val:
#                 p2 = p2.next
#             p1 = p2
#             p2 = p2.next
#             p1.next = None
#         else:
#             p1.next = p2
#             if dummy.next is None:
#                 dummy.next = p2
#             p1 = p2
#             p2 = p2.next
#             p1.next = None
#     return dummy.next


    

''' unittest '''
n8 = ListNode(5)
n7 = ListNode(5, n8)
n6 = ListNode(4, n7)
n5 = ListNode(3, n6)
n4 = ListNode(3, n5)
n3 = ListNode(2, n4)
n2 = ListNode(1, n3)
n1 = ListNode(1, n2)
print LinkedList(n1), 'should be 1->1->2->3->3->4->5->5'

ss = Solution()
print LinkedList(ss.deleteDuplicates(n1)), 'should be 2->4'

