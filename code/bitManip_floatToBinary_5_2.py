'''
Created on Nov 7, 2013

@author: Songfan
'''
def intToBinary(x):
    output = ''
    if x == 0:
        return '00000000'
    while(x != 0):
        mask = 2-1
        output = str(x&mask)+output
        x >>= 1 
    return output        

def pointToBinary(x):
    assert (x>0 and x<1), "this is not a point number"
    output=""
    sentinal = 1.0
    threshold = 0.000001
    if x<threshold:
        return "00000000"
    while(abs(x)>threshold):
        sentinal /= 2
        if sentinal-x <= 0:
            output+=str(1)
            x -= sentinal
        else:
            output+=str(0)
    return output
    
    
def floatToBinary(x):
    assert ('.' in x), "Input must has a decimal point"
    parts = x.split('.')
    assert (len(parts)==2), "Input must follow format: XX.XX"
    p1 = intToBinary(int(parts[0]))
    p2 = pointToBinary(float('0.'+parts[1]))
    return p1 + '.' + p2

x = 34
print intToBinary(x)
y = .0000000000000000001
print pointToBinary(y)
print floatToBinary('32.1415926')