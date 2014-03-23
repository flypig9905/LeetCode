'''

Validate if a given string is numeric.

Some examples:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true
Note: It is intended for the problem statement to be ambiguous. You should gather all requirements up front before implementing one.

Created on Jan 2, 2014

@author: Songfan
'''

''' thought: 
    1. valid characters are: '+-.e' 
    2. leading or trailing white space are valid
    3. '+' and '-' should only appear in the beginning of the number or after 'e' followed with number
    4. 'e' should follow with a valid number
    
    conclusion:
    1. validNum: divide the number by 'e', first part should be a valid float, second part should be a valid int (with sign allowed)
    2. validFloat: divide the number by '.', first part should be a valid int (with sign allowed), second part should be a valid int (no sign allowed)
    '''

def strip(s, c = ' '):
    if s == '': return s
    startPos = 0
    endPos = len(s)
    for e in s:
        if e == ' ':
            startPos += 1
        else:
            break
    for e in s[::-1]:
        if e == ' ':
            endPos -= 1
        else:
            break
    return s[startPos:endPos]


def findChar(s, c):
    for i in range(len(s)):
        if s[i] == c:
            return i
    return -1


def validFloat(s):
    ''' check if is valid float or int,  (no leading or trailing space or 'e' allowed)'''
    if s == '.': return False
    dotPos = findChar(s, '.')
    if dotPos != -1:
        return validInt(s[:dotPos], True) and validInt(s[dotPos+1:], False)
    else:
        return validInt(s, True)


def validInt(s, signAllowed):
    ''' check if is a valid int (no leading or trailing space allowed), signAllowed is a flag is used for the following situation,
    s = '+23.03', if it is divided by '.', then the front part '+23' is a signAllowed int, while back part '03' is not '''
    for i in range(len(s)):
        if i==0 and signAllowed and s[i] in '+-':
            continue
        elif s[i] in '0123456789':
            continue
        else:
            return False
    return True


def validNum(s):
    # strip the leading and trailing white space
    ss = strip(s)
    ePos = findChar(ss, 'e')
    if ePos != -1:
        # if 'e' exist, then first part should be a valid float number; second part should be a valid int
        return validFloat(ss[:ePos]) and ss[:ePos] != '' \
            and validInt(ss[ePos+1:], True) and ss[ePos+1:] != ''
    else:
        return validFloat(ss)


''' unittest strip '''
print 'unittest: strip'
s = '  34  '
print strip(s) + ' should be 34'
s = ''
print strip(s) + ' should be '''
print
   
''' unittest findChar '''
print 'unittest findChar'
s = '3a4.sf2'
print findChar(s, '.'), ' should be 3'
print findChar(s, '2'), ' should be 6'
s = '23e03'
print findChar(s, 'e'), ' should be 2'
print findChar(s, 'a'), ' should be -1'
print 

''' unittest validFloat'''
print 'unittest validFloat'
s = '+12.45'
print validFloat(s), 'should be True'
s = '-.8'
print validFloat(s), 'should be True'
s = '12.'
print validFloat(s), 'should be True'
s = ' 12.45'
print validFloat(s), 'should be False'
s = '12.-45'
print validFloat(s), 'should be False'
print 

''' unittest validInt '''
print 'unittest validInt'
s = '3425'
print validInt(s,False), 'should be True'
s = '+3425'
print validInt(s,True), 'should be True'
s = '-34'
print validInt(s,True), 'should be True'
s = '3425.'
print validInt(s,False), 'should be False'
s = '34e5'
print validInt(s,False), 'should be False'
s = '-3425.'
print validInt(s,False), 'should be False'
print 

''' unittest validNum '''
   
n = "1." 
print validNum(n), 'should be True'
n = "2e10" 
print validNum(n), 'should be True'
n = "1.e2" 
print validNum(n), 'should be True'
n = ".3   " 
print validNum(n), 'should be True'
n = "+1.e+5" 
print validNum(n), 'should be True'
n = ".e1" 
print validNum(n), 'should be False'
n = "1e.1" 
print validNum(n), 'should be False'
n = "1e1.1" 
print validNum(n), 'should be False'
n = "2.3e" 
print validNum(n), 'should be False'


