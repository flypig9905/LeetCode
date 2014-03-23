'''
Implement atoi to convert a string to an integer.

Hint: Carefully consider all possible input cases. If you want a challenge, please do not see below and ask yourself what are the possible input cases.

Notes: It is intended for this problem to be specified vaguely (ie, no given input specs). You are responsible to gather all the input requirements up front.

atoi specification:

The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, 
takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is 
empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned. If the correct value is out of the range of representable values, 
NT_MAX (2147483647) or INT_MIN (-2147483648) is returned.

Created on Dec 30, 2013

@author: Songfan
'''

'''     input could be:
    1. normal: '23'
    2. leading 0: '023'
    3. floating: '34.5'
    4. negative: '-23'
    5. non digit: '24a' -> '24'
    6. white space: '  23' -> '23'
    7. max and min value: return INT_MAX if n > 2147483647; return INT_MIN if n < -2147483648
'''
MAX_INT = 2**32
MIN_INT = -2**32

''' passes all test '''
def strToInt1(s):
    assert(isinstance(s,str)),'input error'
    if s == '': return 0
    sign = 1
    result = 0
    cnt = 0 # serve as the moving pointer
    # strip all white space in the front
    for e in s:
        if e == ' ': 
            cnt += 1
        else:
            break
    
    if not cnt == len(s):
        if s[cnt] == '+':
            cnt += 1
        if s[cnt] == '-': 
            sign = -1
            cnt += 1 
        if not s[cnt].isdigit(): # there cannot be any non digit once + or - appears
            return 0
        for e in s[cnt:]:   # iterate the digit
            if e.isdigit():
                if result > MAX_INT and sign == 1: return MAX_INT
                if result > MAX_INT and sign == -1: return MIN_INT
                result = result * 10 + int(e)
            else:
                break
        return result * sign
    else:   # this means the string is made of white space
        return 0
                

''' too complicated '''
def strToInt(s):
    assert(isinstance(s,str)),'input error'
    if s == '': return 0
    result = ''
    sign = 1
    startFlag = False
    leadingZeroFlag = True
    for e in s:
        if e.isdigit() and not startFlag:
            startFlag = True
            result += e
            continue
            
        if startFlag:
            if e.isdigit():
                if e == '0' and leadingZeroFlag: continue
                else:
                    result += e
                    leadingZeroFlag = False
            else:
                break
        else:
            if e == ' ': continue
            if e == '+': 
                startFlag = True
                continue
            if e == '-':
                sign = -1
                startFlag = True
                continue
    
    if result == ' ':
        return 0   
    else:
        return digitStrToNum(result, sign)
        
def digitStrToNum(s, sign):
    n = len(s)
    if n > 8:
        if sign == 1: return 'MAX_INT'
        else: return 'MIN_INT'
    result = 0
    cnt = 0
    for e in s[::-1]:
        result += int(e) * 10 ** cnt
        cnt += 1
    return sign * result
    

''' unittest digitStrToNum '''
# all pass
# s = '000123'
# sign = -1
# print digitStrToNum(s, sign)
# s = '4444444444444444444444444444'
# print digitStrToNum(s, sign)


''' unittest '''
s = '  -234 xoi234' # return -234
print strToInt1(s)
s = '  + 3209'  # return 0, test in C++
print strToInt1(s)
s = '  -c34'   # return 0
print strToInt1(s)
s = '  5555555555555555'   # return MAX_INT
print strToInt1(s)

    