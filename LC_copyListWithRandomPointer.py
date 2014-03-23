'''

A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.

Created on Feb 15, 2014

@author: Songfan
'''
''' 1. duplicate each node
    2. copy each rand ptr
    3. separate the linked list
'''

# Definition for singly-linked list with a random pointer.
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None
        
    def __str__(self):
        return str(self.label)

class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        if head is None: return head
        
        # first pass, copy node
        curr = head
        while curr:
            newNode = RandomListNode(curr.label)
            newNode.next = curr.next
            curr.next = newNode
            curr = newNode.next
        
        # second pass, copy random ptr
        curr = head
        while curr:
            ''' curr.random can be None '''
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next
            
        # seperate list
        curr = head
        newHead = head.next
        while curr:
            tmp = curr.next
            ''' tmp can be None, which means the end of list '''
            if tmp:
                curr.next = tmp.next
            curr = tmp
        
        return newHead
    

n1 = RandomListNode(1)
n2 = RandomListNode(2)
n3 = RandomListNode(3)
n4 = RandomListNode(4)
n5 = RandomListNode(5)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n1.random = n4
n3.random = n5
n4.random = n2

ss = Solution()
newHead = ss.copyRandomList(n1)  
curr = newHead
while curr:
    print curr.label
    curr = curr.next
            
            
            
        
        
        
        
        
        
        
        
        
        
        
        