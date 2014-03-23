'''

Clone an undirected graph. Each node in the graph contains a label and a list of its neighbors.


OJ's undirected graph serialization:
Nodes are labeled uniquely.

We use # as a separator for each node, and , as a separator for node label and each neighbor of the node.
As an example, consider the serialized graph {0,1,2#1,2#2,2}.

The graph has a total of three nodes, and therefore contains three parts as separated by #.

First node is labeled as 0. Connect node 0 to both nodes 1 and 2.
Second node is labeled as 1. Connect node 1 to node 2.
Third node is labeled as 2. Connect node 2 to node 2 (itself), thus forming a self-cycle.
Visually, the graph looks like the following:

       1
      / \
     /   \
    0 --- 2
         / \
         \_/

Created on Feb 15, 2014

@author: Songfan
'''

''' bfs
    To check if a node has been copied or not, use hashtable (original node -> copied node)
'''
from queue import Queue

# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
        
    def __str__(self):
        neighbor = [str(e.label) for e in self.neighbors]
        return 'label: ' + str(self.label) + ', neighbor: ' + ','.join(neighbor)

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    nodeCopy = {}
    def cloneGraph(self, node):
        if node is None: return node
        q = Queue()
        q.enqueue(node)
        self.nodeCopy[node] = UndirectedGraphNode(node.label)
        
        while not q.isEmpty():
            oldNode = q.dequeue()
            tmp = self.nodeCopy[oldNode]
            for nb in oldNode.neighbors:
                if nb not in self.nodeCopy:
                    ''' define new neighbor node if not previous defined (unvisited) '''
                    self.nodeCopy[nb] = UndirectedGraphNode(nb.label)
                    q.enqueue(nb)
                tmp.neighbors.append(self.nodeCopy[nb])
                self.nodeCopy[oldNode] = tmp
        return self.nodeCopy[node]
                
ss = Solution()
n0 = UndirectedGraphNode(0)
n1 = UndirectedGraphNode(1)
n2 = UndirectedGraphNode(2)
n0.neighbors = [n1]
n1.neighbors = [n0, n2]
n2.neighbors = [n1, n2]     
res = ss.cloneGraph(n0)
for k in ss.nodeCopy:
    print ss.nodeCopy[k]
        
        
        
        