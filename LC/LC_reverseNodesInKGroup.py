'''

Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

You may not alter the values in the nodes, only nodes itself may be changed.

Only constant memory is allowed.

For example,
Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5

Created on Feb 1, 2014

@author: Songfan
'''

'''  
    first think about how to realize the following function, then, this question boils down to find valid first and last pointer
    
     Reverse a link list between pre and next exclusively
     an example:
     a linked list:
     0->1->2->3->4->5->6
     |           |   
     first       last
     after call first = reverse(first, last)
     
     0->3->2->1->4->5->6
              |  |
              f  l
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
        res = []
        curr = self.head
        while curr:
            res.append(str(curr.val))
            curr = curr.next
        return '->'.join(res)
    
def solution(head, k):
    if head is None: return head
    dummy = ListNode(-1, head)
    first = dummy
    last = head
    while last:
        ''' move the last pointer to the end of group '''
        cnt = k
        while cnt > 0:
            if last: last = last.next
            else: break
            cnt -= 1
            
        ''' this means last is valid '''
        if cnt == 0:
            ''' reverse the list between last and first one by one '''
            curr = first.next
            while curr.next != last:
                tmp = curr.next
                curr.next = tmp.next
                tmp.next = first.next
                first.next = tmp
            ''' assign 'first' to the previous of 'last', so that first.next = last, for next iteration '''
            first = curr
    return dummy.next



''' unittest '''
n6 = ListNode(6)
n5 = ListNode(5, n6)
n4 = ListNode(4, n5)
n3 = ListNode(3, n4)
n2 = ListNode(2, n3)
n1 = ListNode(1, n2)
print LinkedList(n1)
        
n = solution(n1, 3)
print LinkedList(n), 'should be 3->2->1->6->5->4'
        
# test case 2
n6 = ListNode(6)
n5 = ListNode(5, n6)
n4 = ListNode(4, n5)
n3 = ListNode(3, n4)
n2 = ListNode(2, n3)
n1 = ListNode(1, n2)
        
n = solution(n1, 4)
print LinkedList(n), 'should be 4->3->2->1->5->6'

