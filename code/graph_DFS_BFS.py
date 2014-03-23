'''

DFS: could be iterative and recursive
BFS: normally iterative

For Graph, when implementing DFS or BFS, track visited list

Trade-off between iterative method and recursive method:
(http://stackoverflow.com/questions/15688019/recursion-versus-iteration)

Recursion is usually MUCH SLOWER because all function calls must be stored in a stack to allow the return back to the caller functions. 
In many cases, memory has to be allocated and copied to implement scope isolation.

(Some optimizations, like tail call optimization, make recursions faster but aren't always possible, and aren't implemented in all languages.)

The main reasons to use recursion are:

that it's more intuitive in many cases when it mimics our approach of the problem
that some data structures like trees are easier to explore using recursion (or would need stacks in any case)

Of course every recursion can be modeled as a kind of loop : that's what the CPU will ultimately do. And the recursion itself, 
more directly, means putting the function calls and scopes in a stack. But changing your recursive algorithm to a looping one 
might need a lot of work and make your code less maintainable : as for every optimization, it should only be attempted when 
some profiling or evidence showed it to be necessary.

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
        while not vertexQueue.isEmpty():
            currentVertex = vertexQueue.dequeue()
            visitedVertex.append(currentVertex)
            for neighborVertex in self.vertexList[currentVertex].getConnections():
                if neighborVertex.id not in visitedVertex:
                    vertexQueue.enqueue(neighborVertex.id) 
        return visitedVertex  
        
    def depthFirstSearchTraverse(self, startVertex): # use a stack to store the temporory vertex
        ''' dfs iterative '''
        vertexStack = Stack()
        if startVertex in self:
            vertexStack.push(startVertex)
        visitedVertex = []
        while not vertexStack.isEmpty():
            currentVertex = vertexStack.pop()
            visitedVertex.append(currentVertex)
            for neighborVertex in self.vertexList[currentVertex].getConnections():
                if neighborVertex.id not in visitedVertex:  # need to check if 
                    vertexStack.push(neighborVertex.id)
        return visitedVertex
        
    def dfsTraverseRecursive(self, startVertex):
        ''' depth first search traversal, recursive '''
        if startVertex not in self.getVertices():
            return False
        visitedVertex = []
        self._dfs(startVertex, visitedVertex)
        return visitedVertex
    
    def _dfs(self, startVertex, visitedVertex):
        visitedVertex.append(startVertex)
        for v in self.vertexList[startVertex].getConnections():
            if v.id not in visitedVertex:
                self._dfs(v.id, visitedVertex)
        
    def depthFirstSearch(self, startVertex, key):
        ''' search for a specific key '''
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
print 'bfs iterative: ', g.breadthFirstSearchTraverse('A')
print 'dfs iterative: ', g.depthFirstSearchTraverse('A')
print 'dfs recursive: ', g.dfsTraverseRecursive('A')
print g.depthFirstSearch('A', 'A')