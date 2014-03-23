'''
Created on Nov 21, 2013

@author: Songfan
'''

class Node:
    def __init__(self,value=None):
        self.value = value
        self.next = None
        
    def __str__(self):
        return str(self.value)

class LinkedList:
    def __init__(self, head = None):
        self.head = head
        
    def add(self, value):
        n = Node(value)
        if self.head == None:
            self.head = n
        else:
            currNode = self.head
            while(not currNode.next == None):
                currNode = currNode.next
            currNode.next = n
            
    def remove(self, value):
        if self.head == None:
            return
        if self.head.value == value:
            self.head = self.head.next
        else:
            currNode = self.head
            while(currNode.next):
                if currNode.next.value == value:
                    currNode.next = currNode.next.next
                    break
                currNode = currNode.next    
                
    def mergeSort(self, node):
        if(not node or node.next == None):
            return node
        else:
            # runner strategy to find the middle node of the list
            slower = node
            faster = node.next
            while(faster.next and faster.next.next):
                slower = slower.next
                faster = faster.next.next
            # break the linked list from the middle
            tmp = slower.next
            slower.next = None
            slower = tmp
            return self.merge(self.mergeSort(node), self.mergeSort(slower))
    
    def merge(self, a, b):
        c = Node()
        head = c
        # set the next pointer in sorted order
        while(a!=None and b!=None):
            if(a.value <= b.value):
                c.next = a
                c = a
                a = a.next
            else:
                c.next = b
                c = b
                b = b.next
        if (a==None):
            c.next = b
        else:
            c.next = a
        return head.next
    
    def removeDup(self):
        currNode = self.mergeSort(self.head)
        while(currNode and currNode.next):
            if currNode.value == currNode.next.value:
                currNode.next = currNode.next.next  # assign the next pointer of current Node to the one next to the next
            else:
                currNode = currNode.next    # move current Node pointer to the next element
            
        
    
    def __str__(self):
        if self.head is None:
            return 'linked list:'
        s = [str(self.head.value)]
        currNode = self.head.next
        while(not currNode == None):
            s.append(str(currNode.value))
            currNode = currNode.next
        return 'linked list: ' + '->'.join(s)
    
    def displayLinkedListFromNode(self,node):
        if not node:
            return 'linked list: '
        s = [str(node.value)]
        curr = node.next
        while(curr):
            s.append(str(curr.value))
            curr = curr.next
        return 'linked list: '+'->'.join(s)


# aList = LinkedList()
# aList.remove(2)
# aList.removeDup()
# print aList
# aList.add(2)
# aList.add(4)
# aList.add(7)
# aList.add(2)
# aList.add(6)
# aList.add(7)
# aList.mergeSort(aList.head)
# print aList
# aList.removeDup()
# print aList