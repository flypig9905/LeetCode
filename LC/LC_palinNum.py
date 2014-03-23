'''

Determine whether an integer is a palindrome. Do this without extra space.

Some hints:
Could negative integers be palindromes? (ie, -1)

If you are thinking of converting the integer to string, note the restriction of using extra space.

You could also try reversing an integer. However, if you have solved the problem "Reverse Integer", you know that the reversed integer might overflow. How would you handle such case?

There is a more generic way of solving this problem.

Created on Jan 31, 2014

@author: Songfan
'''

''' check the first digit and the last digit, and then move towards the middle '''
def palinNum(n):
    if n < 0: return False
    d = 1   # for tracking the first digit
    while n / d >= 10:
        d *= 10
        
    tmp = n
    while tmp > 0:
        a = tmp / d
        b = tmp % 10
        if a != b: return False
        else:
            tmp = tmp % d / 10
            d /= 100
    return True

print palinNum(42324),'should be True'
print palinNum(0),'should be True'
print palinNum(4),'should be True'
print palinNum(423324),'should be True'
print palinNum(42334),'should be False'


            
        
        
        
        
        
        
        