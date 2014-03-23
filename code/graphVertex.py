'''
Created on Nov 8, 2013

@author: Songfan
'''
class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}
        
    def addNeighbor(self, toVertex, weight=0):
        self.connectedTo[toVertex] = weight
        
    def __str__(self):
        return str(self.id) + ' is connected to ' + str([x.id for x in self.connectedTo])
    
    def getId(self):
        return self.id
    
    def getConnections(self):
        return self.connectedTo.keys()
    
    def getWeight(self, toVertex):
        return self.connectedTo[toVertex]
    
# v1 = Vertex('A')
# v2 = Vertex('B')
# v3 = Vertex('C')
#  
# v1.addNeighbor(v2)
# v1.addNeighbor(v3)
# 
# print v1
# print [x.id for x in v1.getConnections()]