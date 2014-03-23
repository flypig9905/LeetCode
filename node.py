'''
Created on Nov 4, 2013

@author: Songfan
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
    def getData(self):
        return self.data
    
    def getNext(self):
        return self.next
    
    def setData(self, data):
        self.data = data
    
    def setNext(self, node):
        self.next = node