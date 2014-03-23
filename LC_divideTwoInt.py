'''

Divide two integers without using multiplication, division and mod operator.

Created on Jan 14, 2014

@author: Songfan
'''

''' algorithm: without mul, div, mod, we are left with bit manipulation, add, subtract '''

def divide(a, b):
    assert(b != 0), 'divide by zero!'
    if a == 0: return 0
    if (a > 0 and b > 0) or (a < 0 and b < 0): sign = 1
    elif (a < 0 and b > 0) or (a > 0 and b < 0): sign = -1
    
    res = -1
    tmp = 0
    while tmp <= a:
        res += 1
        tmp += b
    
    if sign == 1: return res
    else: return -res
        
print divide(0,3),'should be 0'       
print divide(12,3),'should be 4'
print divide(13,3),'should be 4'
print divide(14,3),'should be 4'
print divide(15,3),'should be 5'