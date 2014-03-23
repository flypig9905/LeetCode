'''
Given an array of integers, every element appears THREE times except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Created on Dec 28, 2013

@author: Songfan
'''

''' To solve this problem using only constant space, you have to rethink how the numbers are being represented in computers -- using bits.

If you sum the ith bit of all numbers and mod 3, it must be either 0 or 1 due to the constraint of this problem where each number must appear either three times or once. This will be the ith bit of that "single number".

A straightforward implementation is to use an array of size 32 to keep track of the total count of ith bit. '''

def singleNumber(arr):
    count = [0]*32
    result = 0
    for i in range(32):
        for e in arr:
            if e >> i & 1:
                count[i] += 1
                
        result |= count[i] % 3 << i # after mod 3, shift this bit by i, or it with 'result'
    return result

arr = [1,1,1,2,2,3,2,3,4,3]
print singleNumber(arr)