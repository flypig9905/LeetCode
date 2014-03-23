'''
implement subtraction, multiplication, division from addition for integers

Created on Dec 28, 2013

@author: Songfan
'''

def negate(a):
    if a>0:
        d = -1
    else:
        d = 1
    r = 0
    while(a):
        r += d
        a += d
    return r

def absoluteValue(a):
    if a<0:
        r = negate(a)
    else:
        r = a
    return r
    
def subtract(a,b):
    return a+negate(b)
    

def mul(a,b):
    assert(isinstance(a,int)),'input error'
    if a<b:
        return mul(b,a) # this will be faster
    if b==0: return 0
    elif b<0:
        b = absoluteValue(b)
        a = negate(a)
    r = 0
    for i in range(b,0,-1):
        r+=a
    return r

def div(a,b):
    absa = absoluteValue(a)
    absb = absoluteValue(b)
    product = 0
    while(absa>absb):
        product += 1
        absa = subtract(absa,absb)
    if (a<0 and b>0) or (a<0 and b>0):
        product = negate(product)
    return product
    
        
a = 10
print '-',a,'=',negate(a)
print 'abs(',a,') = ', absoluteValue(a)
print '3 * 5 = ',mul(3,5)
print '3 * -5 = ',mul(3,-5)
print '-3 * 5 = ',mul(-3,5)
print '-3 * -5 = ',mul(-3,-5)
print '2 - 7 = ',subtract(2,7)
print '3 / 5 = ',div(3,5)
print '-7 / 2 = ',div(-7,2)