'''

Reverse a linked list from position m to n. Do it in-place and in one-pass.

For example:
Given 1->2->3->4->5->NULL, m = 2 and n = 4,

return 1->4->3->2->5->NULL.

Note:
Given m, n satisfy the following condition:
1 <= m <= n <= length of list.

Created on Feb 4, 2014

@author: Songfan
'''
class ListNode:
    def __init__(self, val = None, next = None):
        self.val = val
        self. next = next
        
    def __str__(self):
        return str(self.val)
    
class LinkedList:
    def __init__(self, head = None):
        self.head = head
    
    def __str__(self):
        res = []
        curr = self.head
        while curr:
            res.append(str(curr.val))
            curr = curr.next
        return '->'.join(res)
    
def solution(head, m, n):
    if head is None: return head
    dummy = ListNode(-1, head)
    cnt = 1
    start = dummy
    while cnt < m:
        start = start.next
        cnt += 1
    curr = start.next
    
    ''' curr pointer in position, start swap one by one '''
    while cnt < n:
        
        tmp = start.next
        start.next = curr.next
        curr.next = curr.next.next
        start.next.next = tmp
         
        cnt += 1
    
    return dummy.next
        
    
    
    

    

''' unittest '''
   
n5 = ListNode(5)
n4 = ListNode(4, n5)
n3 = ListNode(3, n4)
n2 = ListNode(2, n3)
n1 = ListNode(1, n2)
print LinkedList(n1)        
print LinkedList(solution(n1, 2, 4))
        
    