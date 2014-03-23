'''
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and set.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
set(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

Answer: Queue(doubly linked list implementation) + Hashtable

Created on Dec 12, 2013

@author: Songfan
'''
from doublyLinkedList import DoublyLinkedList

class Queue:
    def __init__(self):
        self._list = DoublyLinkedList()
        self._size = 0
        
    def getSize(self):
        return len(self._list)
        
    def enqueue(self,item):
        self._list.insertFront(item)
        
    def dequeue(self):
        return self._list.removeEnd()
    
    def __str__(self):
        return self._list.displayForward()

class LRUCache:
    def __init__(self, capacity=10):
        self._capacity = capacity
        self._q = Queue()
        self._h = {}
        
    def set(self,key,value):
        if self._q.getSize() >= self._capacity:
            coldest = self._q.dequeue()
            self._h.pop(coldest)
        self._q.enqueue(key)
        self._h[key] = value
        
    def get(self, key):
        if self._h.has_key(key):
            self._q._list.moveFront(key)    # make this key the hottest
            return self._h[key]
        else:
            return -1

''' test for Queue ''' 
#q = Queue()
#q.enqueue(2)
#q.enqueue(1)    
#q.enqueue(3)
#print q
#q.dequeue()
#print q
#print q.getSize()

''' test for LRU Cache '''
lru = LRUCache(4)
lru.set(1, 'one')
lru.set(3, 'three')
lru.set(2, 'two')
lru.set(4, 'four')
print lru._q
print lru.get(3)
lru.set(5, 'five')
print lru._q