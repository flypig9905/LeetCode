'''
Created on Dec 11, 2013

@author: Songfan
'''
from linkedList import LinkedList

def getTail(head):
    curr = head
    while(curr.next):
        curr = curr.next
    return curr

def partition(head, pivot):
    newHead = None
    newTail = pivot
    curr = head
    prev = None
    while(curr!=pivot):
        # check two base case, whether or not the newHead has been assigned
        if not newHead:
            # then check if the curr value is less than pivot
            if curr.value<=pivot.value:
                newHead = curr
                prev = curr
                curr = curr.next
            else:
                newTail.next = curr
                newTail = curr
                curr = curr.next
                newTail.next = None
        elif curr.value > pivot.value:
            prev.next = curr.next
            newTail.next = curr
            newTail = curr
            curr = curr.next
            newTail.next = None
        else:
            prev = prev.next
            curr = curr.next
    if not newHead:
        newHead = pivot
    return newHead,newTail

def quicksortHelper(head,pivot):
    if not head or head==pivot: # base case is extremely important, the case when head=pivot need to be handle here
        return head
    newHead,newTail = partition(head,pivot)
    if newHead!=pivot:
        #find tail of the first half, called tmp
        tmp = newHead
        while(tmp.next!=pivot):
            tmp = tmp.next
        tmp.next = None # need to break the link for the first half
        newHead = quicksortHelper(newHead,tmp)
        tmp = getTail(newHead)  # the tail of the first half should be re-fetch
        tmp.next = pivot
        
    if newTail!=pivot:
        pivot.next = quicksortHelper(pivot.next,newTail)
        
    return newHead

def quickSort(head):
    if head:
        tail = getTail(head)
        return quicksortHelper(head,tail)
    
    



aList = LinkedList()
aList.add(9)
aList.add(4)
aList.add(8)
aList.add(3)
aList.add(7)
aList.add(6)
print aList
print aList.displayLinkedListFromNode(aList.head.next)
print aList.displayLinkedListFromNode(quickSort(aList.head))