'''

Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321

click to show spoilers.

Have you thought about this?
Here are some good questions to ask before coding. 
Bonus points for you if you have already thought through this!

If the integer's last digit is 0, what should the output be? ie, cases such as 10, 100.

Did you notice that the reversed integer might overflow? Assume the input is a 32-bit integer, 
then the reverse of 1000000003 overflows. How should you handle such cases?

Throw an exception? Good, but what if throwing an exception is not an option? 
You would then have to re-design the function (ie, add an extra parameter).

Created on Jan 14, 2014

@author: Songfan
'''

''' thought: with 0 to the end
    additional: consider overflow '''

class Solution:
    # @return an integer
    def reverse(self, x):
        ''' consider x being negative number, ex. -12 % 10 = 8, but not 2 or -2 ''' 
        if x == 0: return x
        elif x > 0: sign = 1
        else: sign = -1
        tmp = abs(x)
        res = 0
        while tmp:
            res = res * 10 + tmp % 10
            tmp /= 10
        return sign * res

''' unittest '''
x = 2350
ss = Solution()
print ss.reverse(x), 'should be 532'
    
    