'''
Created on Nov 6, 2013

@author: Songfan

Note: Just realize this is one variation of the classical knapsack problem, OMG!!!

'''
from queue import Queue
##### recursive call + caching
# def calcMinCoinNumFortotalValue(coinValueList,totalValue,knownMinCoinNumFortotalValue):
#     minCoinNum = totalValue
#     if totalValue in coinValueList:     # check base case
#         knownMinCoinNumFortotalValue[totalValue] = 1
#         return 1
#     elif knownMinCoinNumFortotalValue.has_key(totalValue) and knownMinCoinNumFortotalValue[totalValue] > 0:     # caching, check calculated result dictionary
#         return knownMinCoinNumFortotalValue[totalValue]
#     else:
#         for i in [c for c in coinValueList if c <= totalValue]:     # good grammar to follow
#             coinNum = 1 + calcMinCoinNumFortotalValue(coinValueList, totalValue-i, knownMinCoinNumFortotalValue)    # recursive call
#             if coinNum < minCoinNum:
#                 minCoinNum = coinNum
#                 knownMinCoinNumFortotalValue[totalValue] = minCoinNum
#     return minCoinNum
# 
# print(calcMinCoinNumFortotalValue([1,5,10,25],26,{}))
#####

def calcMinCoinNumForValue(coinValueList, totalValue):
    knownCoinNumForValue = {}
    knownCoinChoice = {}
    cnt = 0
    for i in range(1,totalValue+1):
        minCoinNum = i
        minCoinChoice = ""
        for j in coinValueList:
            if i==j:
                minCoinNum = 1
                minCoinChoice = str(j)
            elif i>j and knownCoinNumForValue.has_key(i-j):
                if minCoinNum > knownCoinNumForValue[i-j] + 1:
                    cnt += 1
                    minCoinNum = knownCoinNumForValue[i-j] + 1
                    minCoinChoice = knownCoinChoice[i-j] + " " + str(j)
        knownCoinNumForValue[i] = minCoinNum
        knownCoinChoice[i] = minCoinChoice
    print cnt
    return knownCoinChoice[totalValue]


def calcMinCoinNumForValue2(coinValueList, totalValue):
    knownCoinNumForValue = {}
    knownCoinChoice = {}
    knownCoinChoice[0] = ''
    q = Queue()
    q.enqueue((0,0))
    q.enqueue('endLevel')   # flag indicating end of level
    level = 1
    cnt = 0
    while(not q.isEmpty()):
        e = q.dequeue()
        if e== 'endLevel':
            level+=1
            q.enqueue('endLevel')
        else:
            currVal,valAdded = e
            for vi in coinValueList:
                if vi>=valAdded:
                    nextVal = currVal+vi
                    if nextVal==totalValue:
                        print str(vi)+' '+knownCoinChoice.get(currVal,'') # return empty string '' if knownCoinChoice[currVal] is undefined
                        print cnt
                        return level
                    elif nextVal>totalValue:
                        break
                    else:
                        cnt += 1
                        q.enqueue((nextVal,vi))
                        knownCoinNumForValue[nextVal]=level
                        if not knownCoinChoice.has_key(nextVal):
                            knownCoinChoice[nextVal] = str(vi)+' '+knownCoinChoice.get(currVal,'')


aList = [1,5,10,21,25]
print(calcMinCoinNumForValue(aList,630))   
aList = [1,5,10,21,25]
print(calcMinCoinNumForValue2(aList,630))   






