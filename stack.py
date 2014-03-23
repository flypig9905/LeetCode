# Bradley N. Miller, David L. Ranum
# Introduction to Data Structures and Algorithms in Python
# Copyright 2005
# 
#stack.py

class Stack:
    def __init__(self):
        self.data = []

    def isEmpty(self):
        return self.data == []

    def push(self, item):
        self.data.append(item)

    def pop(self):
        assert (self.size()>0), "Cannot pop from a empty stack!"
        return self.data.pop()

    def peek(self):
        assert (self.size()>0), "Cannot peek from a empty stack!"
        return self.data[-1]

    def size(self):
        return len(self.data)

    def __str__(self):
        result = []
        for i in self.data:
            result.append(str(i))
        return 'stack from the bottom: '+', '.join(result)
 
# s = Stack()
# print s
# s.push(2)
# s.push(3)
# print s
# print s.peek()