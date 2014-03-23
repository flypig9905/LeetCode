'''
CTCI P77 2-4
partition a linked list around x

Created on Nov 21, 2013

@author: Songfan
'''
from linkedList import LinkedList

# def linkedListPartition(aList, x):
#     assert(isinstance(x, int)),'we assuem x in an integer!'
#     if aList.head:
#         currPtr = aList.head
#         while(currPtr):
#             if currPtr.value<x:
#                 if not 'small' in vars():
#                     small = currPtr
#                     smallRunner = small
#                 else:
#                     smallRunner.next = currPtr
#                     smallRunner = currPtr
#             else:
#                 if not 'big' in vars():
#                     big = currPtr
#                     bigRunner = big
#                 else:
#                     bigRunner.next = currPtr
#                     bigRunner = currPtr
#             currPtr = currPtr.next
#         
#         smallList = LinkedList()
#         bigList = LinkedList()
#         if 'small' in vars():
#             smallList.head = small
#             smallRunner.next = None
#         if 'big' in vars():
#             bigList.head = big
#             bigRunner.next = None
#         return(smallList, bigList)
#     else:
#         return(None, None)
 
 
# #----------------test-----------------
# x = 5    
# aList = LinkedList()
# smallList,bigList = linkedListPartition(aList,x)
# print smallList
# print bigList
# 
# aList = LinkedList()
# aList.add(2)
# smallList,bigList = linkedListPartition(aList,x)
# print smallList
# print bigList
# 
# aList = LinkedList()
# aList.add(1)
# aList.add(2)
# aList.add(3)
# smallList,bigList = linkedListPartition(aList,x)
# print smallList
# print bigList
# 
# aList = LinkedList()
# aList.add(6)
# aList.add(7)
# aList.add(8)
# smallList,bigList = linkedListPartition(aList,x)
# print smallList
# print bigList
# 
# aList = LinkedList()
# aList.add(1)
# aList.add(6)
# aList.add(3)
# aList.add(5)
# aList.add(8)
# aList.add(2)
# smallList,bigList = linkedListPartition(aList,x)
# print smallList
# print bigList

def partition(linkedlist, x):
    if linkedlist.head != None:
        p1 = linkedlist.head
        p2 = linkedlist.head.next
        while p2 != None:
            """ beautiful solution!!!"""
            # two runner pointer p1 and p2, where p2 = p1.next, if p1.value > p2.value, assign p2 to head, so head always point to smaller part!
            if p2.value < x:
                p1.next = p2.next
                p2.next = linkedlist.head
                linkedlist.head = p2
                p2 = p1.next
            else:
                p1 = p1.next
                p2 = p1.next



#----------------test-----------------
aList = LinkedList()
aList.add(6)
aList.add(6)
aList.add(3)
aList.add(7)
aList.add(6)
aList.add(1)
aList.add(9)
aList.add(8)
aList.add(2)
x = 5

print aList, " , x=5"   
partition(aList, x)
print aList