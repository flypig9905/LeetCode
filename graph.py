'''
Created on Nov 8, 2013

@author: Songfan
'''
from graphVertex import Vertex
from queue import Queue
from stack import Stack

class Graph:
    def __init__(self):
        self.vertexList = {}
        self.vertexNum = 0
        
    def addVertex(self, key):
        self.vertexList[key] = Vertex(key)
        self.vertexNum += 1
        
    def getVertex(self, v):
        if v in self.vertexList:
            return self.vertexList[v]
        else:
            return None
        
    def __contains__(self, v):
        return v in self.vertexList
    
    def addEdge(self, fromV, toV, weight=0):
        if fromV not in self.vertexList:
            self.addVertex(fromV)
        if toV not in self.vertexList:
            self.addVertex(toV)
        self.vertexList[fromV].addNeighbor(self.vertexList[toV], weight)
        self.vertexList[toV].addNeighbor(self.vertexList[fromV], weight)
        
    def __str__(self):
        return [v for v in self.vertexList]
    
    def getVertices(self):
        return self.vertexList.keys()
    
    def __iter__(self):
        return iter(self.vertexList.values())
    
    def showConnections(self):
        for v in self.vertexList:
            print self.vertexList[v]

    def breadthFirstSearchTraverse(self, startVertex):  # use a queue to store the temporory vertex
        vertexQueue = Queue()
        if startVertex in self:
            vertexQueue.enqueue(startVertex)
        visitedVertex = []
        while(not vertexQueue.isEmpty()):
            currentVertex = vertexQueue.dequeue()
            visitedVertex.append(currentVertex)
            for neighborVertex in self.vertexList[currentVertex].getConnections():
                if neighborVertex.id not in visitedVertex:
                    vertexQueue.enqueue(neighborVertex.id) 
        return visitedVertex  
        
    def depthFirstSearchTraverse(self, startVertex): # use a stack to store the temporory vertex
        vertexStack = Stack()
        if startVertex in self:
            vertexStack.push(startVertex)
        visitedVertex = []
        while(not vertexStack.isEmpty()):
            currentVertex = vertexStack.pop()
            visitedVertex.append(currentVertex)
            for neighborVertex in self.vertexList[currentVertex].getConnections():
                if neighborVertex.id not in visitedVertex:
                    vertexStack.push(neighborVertex.id)
        return visitedVertex
        
    def depthFirstSearch(self, startVertex, key):
        vertexStack = Stack()
        if startVertex not in self.vertexList.keys():
            return False
        else:
            vertexStack.push(startVertex)
        visitedVertex = []
        while(not vertexStack.isEmpty()):
            currentVertex = vertexStack.pop()
            visitedVertex.append(currentVertex)
            if currentVertex == key:
                return True
            else:
                for neighborVertex in self.vertexList[currentVertex].getConnections():
                    if neighborVertex.id not in visitedVertex:
                        vertexStack.push(neighborVertex.id)
        return False

g = Graph()

g.addEdge('A','B',3)
g.addEdge('A','C',3)
g.addEdge('B','D',3)
g.addEdge('B','E',3)
g.addEdge('A','C',3)
g.addEdge('C','F',3)
g.addEdge('C','G',3)
g.addEdge('E','H',3)
g.addEdge('E','I',3)
g.addEdge('G','J',3)
g.addEdge('G','K',3)
print g.getVertices()
g.showConnections()
print g.breadthFirstSearchTraverse('A')
print g.depthFirstSearchTraverse('A')
print g.depthFirstSearch('A', 'Z')