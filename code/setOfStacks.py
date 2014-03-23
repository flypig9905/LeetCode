'''
CTCI P80 3.3
implement a data structure that behave exactly like stack. This data structure contains sereval stacks, a new stack is created if the number of item in the 
previous stack exceeded the threshold

Created on Nov 21, 2013

@author: Songfan
'''
import unittest

class SetOfStacks():
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = [[]]
        
    def isEmpty(self):
        return self.data[0] == []
        
    def push(self, item):
        last = self.getLastStack()
        if len(last)<self.capacity:
            last.append(item)
        else:
            self.data.append([item])
        
    def getLastStack(self):
        return self.data[-1]
    
    def pop(self):
        last = self.getLastStack()
        assert(len(last)>0),"Unexpected behavior: poping from an empty stack!"
        item = last.pop()
        if len(last)==0:
            # delete last stack when empty
            del self.data[-1]
        return item
            
    def peek(self):
        last = self.getLastStack()
        assert(len(last)>0),"Unexpected behavior: peeking from an empty stack!"
        return last[-1]
    
    def popAt(self, index):
        stackLen = len(self.data)
        assert(index<stackLen),"We do not even have that many stack yet!"
        if index == stackLen-1:
            self.pop()
        else:
            self.data[index].pop()
            self.rollOver(index)
            
    def rollOver(self, index):
        stackLen = len(self.data)
        assert(index<stackLen),"We do not even have that many stack yet!"
        if len(self.data[index]) == self.capacity:
            return
        for i in range(index,stackLen):
            if i<stackLen-1:
                self.data[i].append(self.data[i+1].pop(0))
            elif i==stackLen-1:
                if len(self.data[i])==0:
                    del self.data[i]
                
    def __str__(self):
        result = ""
        for i in range(len(self.data)):
            s = [str(item) for item in self.data[i]]
            result += 'stack '+str(i)+': '+', '.join(s)+'; '
        return result

class testSetOfStacks(unittest.TestCase):
    def testEmpty(self):
        s = SetOfStacks(5)
        self.assertTrue(s.isEmpty)
        
    def testPush(self):
        s = SetOfStacks(5)
        for i in range(14):
            s.push(i)
        self.assertEqual(len(s.data), 3)
        
    
        
unittest.main()

# # unittest
# s = SetOfStacks(5)
# print s.isEmpty()   # empty stack
# # s.pop()             # pop: from empty stack
# 
# s.push(2)
# s.push(3)
# s.push(4)
# print s             # push: capacity not exceeded
# 
# s.push(7)
# s.push(8)
# s.push(9)
# s.push(3)
# print s             # push: capacity exceeded
# 
# item = s.pop()
# print s             # pop: normal case
# print item
# s.pop()
# print s             # pop: when last stack is empty after poping
# 
# item = s.peek()
# print item
# print s             # peek: normal case
# 
# s.push(3)
# s.push(7)
# s.push(9)
# print s
# s.popAt(1)          
# print s             # popAt: normal case, from the last stack
# s.popAt(0)
# print s             # popAt: normal case, not from the last stack
# s.popAt(0)
# print s             # popAt: last stack becomes empty
