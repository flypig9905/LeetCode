'''

The set [1,2,3,...,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order,
We get the following sequence (ie, for n = 3):

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Note: Given n will be between 1 and 9 inclusive.

Created on Feb 13, 2014

@author: Songfan
'''

''' observation: 
    1. there are (n-1)! permutations that start with each digit.
    2. once the first digit is set, there are (n-2)! permutation start with other possible numbers

 maintain a candidate digit list, iteratively decide which digit goes to each position '''

class Solution:
    # @return a string
    def getPermutation(self, n, k):
        if n < 1: return ''
        permNum = self.factorial(n)
        if permNum < k: return ''
        
        candidate = range(1, n + 1)
        res = ''
        cnt = n
        k -= 1
        while cnt > 0:
            fact = self.factorial(cnt - 1)
            res += str(candidate[k / fact])
            candidate.pop(k / fact)
            k %= fact
            cnt -= 1
        return res
            
    def factorial(self, n):
        return self._fact(n, {})
    
    def _fact(self, n, h):
        if n == 0: return 1
        if n in h: return h[n]
        h[n] = n * self._fact(n - 1, h)
        return h[n]
    
    
    
ss = Solution()
print ss.factorial(4), 'should be 24'
print ss.getPermutation(3, 4), 'should be 231'
print ss.getPermutation(3, 6), 'should be 321'