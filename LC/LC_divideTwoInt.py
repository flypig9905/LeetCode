'''

Divide two integers without using multiplication, division and mod operator.

Created on Jan 14, 2014

@author: Songfan
'''

''' algorithm: without mul, div, mod, we are left with bit manipulation, add, subtract 
    double the divisor and compared with dividend, update result

'''

def divide(a, b):
    if b == 0: return None
    if a == 0: return 0
    
    # init
    if (a > 0 and b > 0) or (a < 0 and b < 0): pos = True
    else: pos = False
    dividend = a if a > 0 else -a
    divisor = b if b > 0 else -b

    res = dividePos(dividend, divisor)
    return res if pos else -res
    
def dividePos(a, b):
    if a < b: return 0
    res, e, divisor = 0, 0, b
    
    while a >= b:
        res += 1<<e
        a -= b
        b <<= 1
        e += 1
    return res + dividePos(a, divisor) if a > 0 else res
    
        
print divide(0,3),'should be 0'       
print divide(12,3),'should be 4'
print divide(13,3),'should be 4'
print divide(14,3),'should be 4'
print divide(15,3),'should be 5'