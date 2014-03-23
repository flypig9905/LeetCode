'''
Created on Nov 4, 2013

@author: Songfan
'''
from queue import Queue
q = Queue()
q.enqueue('cat')
q.enqueue(2)
print q.size()
print q.dequeue()
print q.peek()