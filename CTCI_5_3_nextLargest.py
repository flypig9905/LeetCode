'''
CTCI P92 5.3

Given a positive integer, print the largest number that has the same number of 1 bits in binary representation

Created on Nov 29, 2013

@author: Songfan
'''

def firstZeroAfterOne(a):
    oneFlag = False
    pos = 0
    while(a):
        currBit = a&1
        pos += 1
        if currBit==0 and oneFlag:
            return pos
        elif currBit==1:
            oneFlag = True
        a >>= 1
        
    if oneFlag:
        return pos+1
    else:
        return False
        
def getOneNum(a, pos):
    cnt = 0
    b = a
    while(pos-1):
        currBit = b&1
        if currBit==1:
            cnt += 1
        #update
        pos -= 1
        b >>= 1
    return cnt

def createMask(pos,num):
    subFrom = 2**pos-1
    ones = 2**(pos-1)-1
    sub = (ones>>num)<<num
    return subFrom-sub

def tailZeros(a,pos):
    return a>>pos<<pos

def nextLargest(a):
    assert(isinstance(a,int)),'input error: input should be a integer'
    assert(a>0),'input error: impossible'
    
    pos1 = firstZeroAfterOne(a)
    
    oneNum = getOneNum(a,pos1)
    
    mask = createMask(pos1, oneNum-1)
    
    aModi = tailZeros(a, pos1)
    
    return aModi | mask


#unittest
a = 16  # 0001 0000    ->    0010 0000 (32)
print a,nextLargest(a)

a = 17  # 0001 0001    ->    0001 0010 (18)
print a,nextLargest(a)

a = 15  # 0000 1111    ->    0001 0111 (23)
print a,nextLargest(a)

# a = 0   # 0000 0000    error
# print nextLargest(a)



