'''

Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.

Created on Jan 10, 2014

@author: Songfan
'''

''' algorithm: iterative through every element, if the current value (the opposite for index) of later element is greater than previous element, 
    this means we falsely add the previous element, then we subtract twice the previous element from the current value and add to the result '''
    
Radix = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
Symbol = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']

def roman2Int(s):
    res = 0
    for i in range(len(s)):
        symIdx2 = Symbol.index(s[i])
        if i > 0:
            symIdx1 = Symbol.index(s[i-1])
        if i > 0 and symIdx1 > symIdx2:
            res += Radix[symIdx2] - 2 * Radix[symIdx1]
        else:
            res += Radix[symIdx2]
    return res

print roman2Int('IXVIV'), 'should be 18'
print roman2Int('XVIV'), 'should be 19'

