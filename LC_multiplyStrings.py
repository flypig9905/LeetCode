'''

Given two numbers represented as strings, return multiplication of the numbers as a string.

Note: The numbers can be arbitrarily large and are non-negative.

Created on Jan 26, 2014

@author: Songfan
'''

'''big int multiplication, be careful with overflow
    1. reverse string, work from least significant digit
    2. maintain a vector cumulating the product of current digit: d[i+j] = n1[i] * n2[j]
    3. scan d and obtain final digit with carry over
    4. trim leading zeros 

'''

class Solution:
    # @param num1, a string
    # @param num2, a string
    # @return a string
    def multiply(self, num1, num2):
        num1 = list(num1)
        num2 = list(num2)
        num1.reverse()
        num2.reverse()
        n1 = len(num1)
        n2 = len(num2)
        d = [0] * (n1 + n2)
        
        for i in range(n1):
            a = int(num1[i])
            for j in range(n2):
                b = int(num2[j])
                d[i+j] += a * b
                
                
        sRes = []
        for i in range(n1 + n2):
            digit = d[i] % 10
            carry = d[i] // 10
            sRes.insert(0, str(digit))
            if i < n1 + n2 - 1: 
                d[i+1] += carry
                
        # trim leading zeros
        while len(sRes) > 0 and sRes[0] == '0':
            sRes.pop(0)
        
        if len(sRes) == 0: return '0'
        else: return ''.join(sRes)
            
            
ss = Solution()
print ss.multiply('385', '0'), 'should be 37345'
            