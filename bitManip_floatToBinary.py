'''
Created on Nov 7, 2013

@author: Songfan
'''
def posIntToBinary(x):
    output = []
    if x == 0:
        return '00000000'
    while(x != 0):
        output.append(str(x&0x01))
        x >>= 1
    output = ''.join(output)
    return output        

def pointToBinary(x):
    output = []
    assert (x>0 and x<1), "this is not a point number"
    sentinal = 1.0
    threshold = 0.01
    if abs(sentinal-x)<threshold:
        return "11111111"
    while(abs(x)>threshold):
        sentinal /= 2
        if sentinal-x <= 0:
            output.append(str(1))
            x -= sentinal
        else:
            output.append(str(0))
    output = ''.join(output)
    return output
    
    
    
def floatToBinary(x):
    assert ('.' in x), "Input must has a decimal point"
    parts = x.split('.')
    assert (len(parts)==2), "Input must follow format: XX.XX"
    p1 = posIntToBinary(int(parts[0]))
    p2 = pointToBinary(float('0.'+parts[1]))
    return p1 + '.' + p2

x = 34
print posIntToBinary(x)
y = x & 0xf0
print y
z = 2
print z>>1
print 2**7
x = -1
print x
print floatToBinary('33.1415926')