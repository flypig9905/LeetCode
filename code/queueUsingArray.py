'''

implement a queue using array, when overflow, substitute the front item.

Created on Feb 8, 2014

@author: Songfan
'''

''' prealloc size, front and rear pointer, length
    enqueue: increment rear ptr
    dequeue: increment front ptr
    increment: need to rap around

 '''

class Queue:
    def __init__(self, capacity = 5):
        self.capacity = capacity
        self.data = [None] * self.capacity
        self.front = 0
        self.rear = -1
        self.size = 0
    
    def enqueue(self, e):
        ''' move front ptr first '''
        if self.size == self.capacity:
            self.front = self._increment(self.front)
            self.size -= 1
        self.rear = self._increment(self.rear)
        self.data[self.rear] = e
        self.size += 1
        
    def dequeue(self):
        assert(self.size > 0),'dequeue from an empty queue!'
        self.data[self.front] = None
        self.front = self._increment(self.front)
        self.size -= 1
            
    
    def _increment(self, ptr):
        ptr = (ptr + 1) % self.capacity # rap around
        ''' equivalent to the following code'''
#         if ptr != self.capacity - 1:
#             ptr += 1
#         else:   # rap around
#             ptr = 0
        
        return ptr
        
    ''' test passes '''    
    def __str__(self):
        if self.size == 0:
            return ''
        elif self.front < self.rear:
            res = [str(d) for d in self.data[self.front:self.rear+1]]
            return ','.join(res)
        elif self.front > self.rear:
            part1 = [str(d) for d in self.data[self.front:]]
            part2 = [str(d) for d in self.data[:self.rear+1]]
            part1.extend(part2)
            return ','.join(part1)
        else:   # only one item
            return str(self.data[self.front])
    
    
''' unittest Queue '''
''' enqueue passes '''
q = Queue(5)
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
print q, 'should be 1,2,3,4,5'
q.enqueue(6)
print q, 'should be 2,3,4,5,6'
q.enqueue(7)
q.enqueue(8)
q.enqueue(9)
q.enqueue(10)
print q, 'should be 6,7,8,9,10'

''' dequeue '''
q = Queue(5)
q.enqueue(1)
q.dequeue()
print q, 'should be '
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
q.dequeue()
print q, 'should be 2,3,4,5'