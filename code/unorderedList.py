'''
Created on Nov 4, 2013

@author: Songfan
'''
from node import Node
class UnorderedList:
    def __init__(self):
        self.head = None
        
    def isEmpty(self):
        return self.head == None
    
    def add(self, item):
        tmp = Node(item)
        tmp.setNext(self.head)
        self.head = tmp
    
    def size(self):
        count = 0
        current = self.head
        while(not current==None):
            count+=1
            current = current.getNext()
        return count
    
    def printList(self):
        current = self.head
        output  = []
        while (current):
            output.append(current.getData())
            current = current.getNext()
        print output
    
    def search(self, item):
        current = self.head
        while(not current == None):
            if current.getData()==item:
                return True
            else:
                current = current.getNext()
        return False

    def remove(self, item):
        current = self.head
        if current and current.getData() == item:
            self.head = current.getNext()
            return
        previous = current
        current = current.getNext()
        while(current):
            if current.getData()==item:
                previous.setNext(current.getNext())
                current.setNext(None)
                return 
            else:
                previous = current
                current = current.getNext()
                

u = UnorderedList()
u.add(31)
u.remove(30)
u.printList()
u.add(32)
u.add(33)
u.printList()
# print u.search(31)
# print u.search(34)
u.remove(32)
u.printList()
u.remove(31)
u.printList()
u.add(1)
u.add(2)
u.remove(2)
u.printList()
u.add(3)
u.add(4)
u.add(5)
u.add(6)
u.remove(5)
u.printList()