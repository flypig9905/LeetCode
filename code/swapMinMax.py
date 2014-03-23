'''
CTCI P58, N4
Created on Nov 19, 2013

@author: Songfan
'''
def swapMinMax(aList):
    if aList and len(aList)>0:
        minIndex = 0
        maxIndex = 0
        try:
            for i in range(1,len(aList)):
                assert (type(aList[i]) is int), "Input Error: this should be a int array"
                if aList[i]>aList[maxIndex]:
                    maxIndex = i
                elif aList[i]<aList[minIndex]:
                    minIndex = i
            tmp = aList[minIndex]
            aList[minIndex] = aList[maxIndex]
            aList[maxIndex] = tmp
        except AssertionError, e:
            print e.args[0]

aList = [1,3,'i',7,9]
swapMinMax(aList)
print aList