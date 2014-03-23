'''
Created on Nov 10, 2013

@author: Songfan
'''
PATTERNS = [1, 11, 111, 1111, 11111]
DEALS = [1, .95, .9, .8, .75]
DEALNUM = len(DEALS)
UNIT_PRICE = 8

def calcBookPrice(bookChoice):
    t = calcVolPattern(bookChoice)
    DPMemory = {}
    for i in range(1,100000):
        minPrice = calcTotalBookNum(i)*UNIT_PRICE
        currentPattern = calcVolPattern(i)
        for j in range(0,DEALNUM):
            pattern = PATTERNS[j]
            if currentPattern % pattern == 0:
                comboNum = currentPattern//pattern
                minPrice = DEALS[j]*comboNum*(j+1)*UNIT_PRICE
                DPMemory[currentPattern] = minPrice
            elif currentPattern>pattern and DPMemory.has_key(currentPattern-pattern):
                if minPrice > DPMemory[currentPattern-pattern]+DEALS[j]*(j+1)*UNIT_PRICE:
                    minPrice = DPMemory[currentPattern-pattern]+DEALS[j]*(j+1)*UNIT_PRICE
        DPMemory[i] = minPrice
    return DPMemory[t]

def calcTotalBookNum(bookCombination):
    bookNum = 0
    for i in str(bookCombination):
        bookNum += int(i)
    return bookNum

def calcVolPattern(aBookChoice):
    assert (aBookChoice>0 and aBookChoice<100000), "Bad input book combination"
    a = [i for i in str(aBookChoice)]
    return int(''.join(sorted(a)))


print calcBookPrice(20415)
    
