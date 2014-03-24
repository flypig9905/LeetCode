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

