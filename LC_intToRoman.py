'''

Given an integer, convert it to a roman numeral.

Input is guaranteed to be within the range from 1 to 3999.

Created on Jan 10, 2014

@author: Songfan
'''

Radix = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
Symbol = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']

def int2Roman(n):
    res = []
    for i in range(len(Radix)):
        while n >= Radix[i]:
            res.append(Symbol[i])
            n -= Radix[i]
    return ','.join(res)

n = 2085
print int2Roman(n)