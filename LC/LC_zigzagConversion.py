'''

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".

Created on Feb 12, 2014

@author: Songfan
'''

''' set aside an array of array, add item individually to the correct array bucket. Have a indicator(r) moving up and down to point to the corrent row '''

def solution(s, nRows):
    if nRows == 1: return s
    n = len(s)
    if n <= nRows: return s
    
    down = True
    res = {}
    r = 0
    i = 0
    while i < n:
        if r == 0:
            down = True
        elif r == nRows - 1:
            down = False
        tmp = res.get(r, [])
        tmp.append(s[i])
        res[r] = tmp
        if down is True: r += 1
        else: r -= 1
        i += 1
    
    ret = ''   
    for i in range(nRows):
        ret += ''.join(res[i])
    return ret
s = 'PAYPALISHIRING'
print solution(s, 3), 'should be PAHNAPLSIIGYIR'