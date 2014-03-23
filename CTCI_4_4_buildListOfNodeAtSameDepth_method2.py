'''
CTCI 4-4
Given a binary search tree, design an alghrithm to create a linked list of all the nodes at each depth

Algorithm: breath first search and record the level of each node

Created on Nov 28, 2013

@author: Songfan
'''
from queue import Queue
from buildListOfNodeAtSameDepth_4_4 import LinkedList, BST

''' BFS: using a queue '''

class BST2(BST):
    def buildNodeList(self):
        result = {}
        if self.root:
            q = Queue()
            visitedNode = []
            q.enqueue(self.root)
            q.enqueue('EndLevelFlag')
            level = 0
            while(not q.isEmpty()):
                tmp = q.dequeue()
                if tmp == 'EndLevelFlag':
                    # finish building the current level
                    level += 1
                else:
                    # add node to Linked List
                    visitedNode.append(tmp)
                    if level in result.keys():
                        result[level].append(tmp)
                    else:
                        aList = LinkedList()
                        aList.append(tmp.value)
                        result[level] = aList
                    if tmp.left: q.enqueue(tmp.left)
                    if tmp.right: q.enqueue(tmp.right)
                    # add dummy item to represent the end of level
                    q.enqueue('EndLevelFlag')
        return result

t = BST()
print t
t.insert(5)
t.insert(1)
t.insert(7)
t.insert(2)
t.insert(9)
t.insert(8)
print t
print t.root.getDepth()
print t.root.left.getDepth()
h = t.buildNodeList()
for k in h.keys():
    print h[k]