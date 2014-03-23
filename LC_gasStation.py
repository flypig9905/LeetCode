'''
Gas Station

There are N gas stations along a circular route, where the amount of gas at station i is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1). You begin the journey with an empty tank at one of the gas stations.

Return the starting gas station's index if you can travel around the circuit once, otherwise return -1.

Note:
The solution is guaranteed to be unique.

Created on Dec 29, 2013

@author: Songfan
'''

def canFinishLoop(gas, cost):
    # assume correct input
    # compute difference
    sLen = len(gas)
    diff = []
    gasSum = 0
    for i in range(sLen):
        d = gas[i]-cost[i]
        diff.append(d)
        gasSum += d
    if gasSum < 0:  # if sum of all gas station is less than total, cannot complete the loop
        return -1
    
    # for each station as a starting point, check the possibility of every move, 
    # if cumulated sum is less than zero, it means this station is not suitable as a starting point
    ''' efficiency caveat: if start from i and cumsum is negative at j, start point should move to j+1 '''
    for i in range(sLen):
        if diff[i] < 0: # cost - gas is negative means this point should not be picked as starter
            continue
        # rotation the difference list to form a new list for computation
        # list rotation is O(1) complexity using linked list, but O(n) for array
        newDiff = diff[i:] + diff[:i]
        
        curSum = 0
        cnt = 0
        for d in newDiff:
            curSum += d
            cnt += 1
            if curSum < 0:  # cumulated sum should not be negative
                break   # break to execute outer for loop
        if cnt == sLen:
            return i

gas = [2, 3, 2, 4, 5]
cost = [1, 4, 6, 2, 3]
print canFinishLoop(gas, cost)



# use a graph to represent Gas station and cost 
# no need to do all this, but it is a good exercise
# class GasStation():
#     def __init__(self, key, gas):
#         self.id = key
#         self.gas = gas
#         self.connectedTo = {}
#     
#     def setGas(self, gas):
#         self.gas = gas
#         
#     def getGas(self):
#         return self.gas
#     
#     def __str__(self):
#         return 'gas station (' + str(self.id) + ') has gas (' + str(self.gas) + ')'
#     
#     def addConnection(self, toStation, weight):
#         # link each other
#         self.connectedTo[toStation] = weight
#         toStation.connectedTo[self] = weight
#     
#     def getConnections(self):
#         return self.connectedTo.keys()
# 
# 
# class GasStationNetwork():
#     def __init__(self):
#         self.stations = []
#         
#     def addStation(self, station):
#         if station not in self.stations:
#             self.stations.append(station)
#         
#     def addMultipleStation(self, stations):
#         for s in stations:
#             self.addStation(s)
# 
#     def __str__(self):
#         res = 'Network has stations:'
#         for s in self.stations:
#             res += ' ' + str(s.id)
#         return res
# 
#     def route(self):
#         if 
# 
# # Gas = {'a':2, 'b':3, 'c':2, 'd':4, 'e':5}
# # Cost = {'ab':1, 'bc':4, 'cd':6, 'de':2, 'ae':3}
# g1 = GasStation('a', 2)
# g2 = GasStation('b', 3)
# g3 = GasStation('c', 2)
# g4 = GasStation('d', 4)
# g5 = GasStation('e', 5)
# 
# g1.addConnection(g2, 1)
# g2.addConnection(g3, 4)
# g3.addConnection(g4, 6)
# g4.addConnection(g5, 2)
# g5.addConnection(g1, 3)
# 
# for g in g2.getConnections():
#     print g
#     
# ''' gas station network '''
# gsn = GasStationNetwork()
# gsn.addStation(g1)
# print gsn
# gsn.addMultipleStation([g2,g3,g4,g5])
# print gsn