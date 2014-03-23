'''

Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Created on Jan 12, 2014

@author: Songfan
'''

''' algorithm: reuse merge 2 sorted list, O(n1+n2+...+nk) time. O(1) space '''

from LC_mergeTwoSortedList import mergeList, ListNode, LinkedList


def mergeKList(lists):
    if len(lists) == 0: return lists
    p = lists[0]
    for i in range(1,len(lists)):
        p = mergeList(p, lists[i])
    return p

''' unittest '''
n1 = ListNode(2)
n2 = ListNode(4)
n3 = ListNode(5)
n1.next = n2
n2.next = n3
A = LinkedList(n1)
print 'A:',A 

n4 = ListNode(3)
n5 = ListNode(4)
n6 = ListNode(8)
n4.next = n5
n5.next = n6
B = LinkedList(n4)
print 'B:',B

n7 = ListNode(1)
n8 = ListNode(6)
n9 = ListNode(7)
n10 = ListNode(9)
n7.next = n8
n8.next = n9
n9.next = n10
C = LinkedList(n7)
print 'merge A, B, C:',LinkedList(mergeKList([n1,n4,n7]))