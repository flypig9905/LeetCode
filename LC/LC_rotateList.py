'''

Given a list, rotate the list to the right by k places, where k is non-negative.

For example:
Given 1->2->3->4->5->NULL and k = 2,
return 4->5->1->2->3->NULL.

Created on Feb 3, 2014

@author: Songfan
'''

''' caution: k could be larger than list length, k %= n
    1. find length, get tail
    2. running pointer move next for k steps
    3. break and link tail to head
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
    ''' find tail and get length '''
    curr = head
    n = 0
    while curr:
        n += 1
        tail = curr
        curr = curr.next
        
    ''' link tail to head and running pointer k steps '''
    k %= n
    tail.next = head
    curr = tail # start form the previous node of head
    while k > 0:
        curr = curr.next
        k -= 1
    newHead = curr.next
    curr.next = None
    return newHead

''' unittest '''
n5 = ListNode(5)
n4 = ListNode(4, n5)
n3 = ListNode(3, n4)
n2 = ListNode(2, n3)
n1 = ListNode(1, n2)
print LinkedList(n1), 'should be 1->2->3->4->5'
print LinkedList(solution(n1, 15)), 'should be 1->2->3->4->5'
print LinkedList(solution(n1, 2)), 'should be 3->4->5->1->2'