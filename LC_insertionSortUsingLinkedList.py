'''
Created on Dec 12, 2013

@author: Songfan
'''
from linkedList import LinkedList

def insertionSort(head):
    if not head or not head.next: return head
    head2 = head
    curr1 = head.next
    head2.next = None
    while(curr1):
        curr2 = head2
        while(curr2):
            if curr1.value<curr2.value:
                head2 = curr1
                curr1 = curr1.next
                head2.next = curr2
                curr2 = None
            elif curr2.next and curr1.value<curr2.next.value:
                tmp = curr2.next
                curr2.next = curr1
                curr1 = curr1.next
                curr2.next.next = tmp
                curr2 = None
            elif not curr2.next:
                curr2.next = curr1
                curr1 = curr1.next
                curr2.next.next = None
                curr2 = None
            else:
                curr2 = curr2.next
    return head2


aList = LinkedList()
aList.add(9)
print aList.displayLinkedListFromNode(insertionSort(aList.head))
aList.add(4)
print aList.displayLinkedListFromNode(insertionSort(aList.head))
aList.add(8)
aList.add(3)
aList.add(7)
aList.add(6)
print aList
print aList.displayLinkedListFromNode(insertionSort(aList.head))

                