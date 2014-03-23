'''
Created on Dec 30, 2013

@author: Songfan
'''
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        
    def __str__(self):
        return str(self.val)

class LinkedList:
    def __init__(self, head):
        self.head = head

    def __str__(self):
        currNode = self.head
        result = []
        while(currNode):
            result.append(str(currNode.val))
            currNode = currNode.next
        return '->'.join(result)
            

def mergeList(a, b):
    # check input
    if not a:
        return b
    elif not b:
        return a
    
    # init pointer for each list 
    c1 = a
    c2 = b
    
    ''' use a dummy variable to track the head '''
    dummy = ListNode(-1)
    c3 = dummy
    
    # merge
    while(c1 and c2):   # if both node is not None, we are not finished
        if c1.val <= c2.val:
            c3.next = c1
            c1 = c1.next
        else:
            c3.next = c2
            c2 = c2.next
        c3 = c3.next
    
    # add the remaining list to current node
    if c1:
        c3.next = c1
    elif c2:
        c3.next = c2
        
    return dummy.next
    
    

''' unittest ListNode'''
n = ListNode(3)
print n
 
''' unittest LinkedList '''
n1 = ListNode(2)
n2 = ListNode(4)
n3 = ListNode(5)
n1.next = n2
n2.next = n3
A = LinkedList(n1)
print A 
 
''' unittest mergeList '''
n4 = ListNode(3)
n5 = ListNode(4)
n6 = ListNode(8)
n4.next = n5
n5.next = n6
B = LinkedList(n4)
print B
C = LinkedList(mergeList(n1,n4))
print C