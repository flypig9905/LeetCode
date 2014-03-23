'''
Created on Dec 12, 2013

@author: Songfan
'''
class DLLNode:
    # doubly linked list node
    def __init__(self, value=None, prev=None, next=None):
        self._value = value
        self._prev = prev
        self._next = next

    def __str__(self):
        return str(self._value)
    
    def hasNext(self):
        return self._next != None
    
    def getNext(self):
        return self._next
    
    def setNext(self, node):
        self._next = node
    
    def hasPrevious(self):
        return self._prev != None
    
    def getPrevious(self):
        return self._prev
    
    def setPrevious(self, node):
        self._prev = node
        
    def getPreviousAndNext(self):
        return self._prev, self._next
    
    def setPreviousAndNext(self, prevNode, nextNode):
        self._prev = prevNode
        self._next = nextNode
        
    def getValue(self):
        return self._value
    
    def setValue(self, value):
        self._value = value

class DoublyLinkedList:
    def __init__(self):
        self._first = DLLNode()
        self._last = DLLNode()
        self._first.setNext(self._last)
        self._last.setPrevious(self._first)
        self._length = 0
    
    def __len__(self):
        return self._length
    
    def insertFront(self, value):
        newNode = DLLNode(value,self._first,self._first._next)
        self._first._next._prev = newNode
        self._first._next = newNode
        self._length+=1
        
    def insertLast(self, value):
        newNode = DLLNode(value, self._last._prev, self._last)
        self._last._prev._next = newNode
        self._last._prev = newNode
        self._length+=1
        
    def displayForward(self):
        plist = []
        curr = self._first
        while curr._next._value:
            plist.append(str(curr._next._value))
            curr = curr._next
        return "LinkedList: %s" % '<->'.join(plist)
    
    def displayBackward(self):
        plist = []
        curr = self._last
        while curr._prev._value:
            plist.append(str(curr._prev._value))
            curr = curr._prev
        return "LinkedList: %s" % '<->'.join(plist)

    def removeEnd(self):
        if not self._length: 
            return None
        item = self._last._prev._value
        self._last._prev._prev.setNext(self._last)
        self._last.setPrevious(self._last._prev._prev)
        self._length-=1
        return item
    
    def moveFront(self, value):
        curr = self._first._next
        while(curr):
            if curr._value == value:
                break
            curr = curr._next
        if curr: # value in list
            # detach current node
            curr._prev.setNext(curr._next)
            curr._next.setPrevious(curr._prev)
            self.insertFront(curr._value)
            
    
#dll = DoublyLinkedList()
#dll.insertFront(3)
#dll.insertFront(1)
#dll.insertFront(2)
#dll.insertLast(5)
#dll.insertLast(7)
#print dll.displayForward() 
#print dll.displayBackward()   
#dll.removeEnd()
#print dll.displayForward()
#print len(dll)
#dll.moveFront(3)
#print dll.displayForward()