'''
Created on Nov 4, 2013

@author: Songfan
'''
class Queue:
    def __init__(self):
        self.data = []
    
    def isEmpty(self):
        return len(self.data) == 0
    
    def enqueue(self,e):
        self.data.insert(0, e)
        
    def dequeue(self):
        return self.data.pop()
    
    def peek(self):
        return self.data[-1]
    
    def size(self):
        return len(self.data)
    
    def __str__(self):
        return str([i for i in self.data])
    
    def __contains__(self, other):
        return other in self.data
    