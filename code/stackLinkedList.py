'''
The Linked List implementation of stack
Created on Nov 21, 2013

@author: Songfan
'''
from linkedList import Node

class stack:
    def __init__(self):
        self.top = None
        
    def isEmpty(self):
        return self.top == None
        
    def push(self, item):
        n = Node(item)
        if self.top == None:
            self.top = n
        else:
            n.next = self.top
            self.top = n
        
    def pop(self):
        assert(not self.isEmpty()),"Unexpected behavior: pop from an emoty stack!"
        item = self.top.value
        self.top = self.top.next
        return item
    
    def peek(self):
        assert(not self.isEmpty()),"Unexpected behavior: peek from an emoty stack!"
        return self.top.value
    
    def size(self):
        if self.isEmpty():
            return 0
        currNode = self.top
        sz = 1
        while(currNode.next):
            sz+=1
            currNode = currNode.next
        return sz
        
    def __str__(self):
        if self.isEmpty():
            return "empty stack"
        else:
            currNode = self.top
            result = [str(currNode.value)]
            while(currNode.next):
                result.append(str(currNode.next.value))
                currNode = currNode.next
        return "stack from top: " + "->".join(result)
        
s = stack()
print s
print s.size()
s.push(2)
s.push(3)
s.push(5)
print s
s.pop()
print s
print s.size()