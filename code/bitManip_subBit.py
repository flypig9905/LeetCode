'''
CareerCup Problem 3.5

Created on Nov 10, 2013

@author: Songfan
'''
def toBin(x): 
    return "{0:b}".format(x)

def subBitInRange(n, m, i, j):
    ones = 2**16-1
    shake = ones>>16-j+i<<i
    mask = ones^shake
    replace = m<<i
    print toBin(mask)
    print toBin(replace)
    output = mask|n + replace
    print toBin(output)
    

subBitInRange(128,9,3,7)
