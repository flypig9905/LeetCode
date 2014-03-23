'''

There are N children standing in a line. Each child is assigned a rating value.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
What is the minimum candies you must give?

Created on Feb 13, 2014

@author: Songfan
'''

''' 
    Double scan
    left policy: scan from left to right, guarantee candy at current position is one greater than previous, if rating is higher
    right policy: scan from right to left, guarantee the same w.r.t. right position.
    Caveat: during second scan, if the candy for current position is larger than previous, do not change it. '''

class Solution:
    # @param ratings, a list of integer
    # @return an integer
    def candy(self, ratings):
        n = len(ratings)
        if n == 0: return 0
        if n == 1: return 1
        
        res = [1] * n
        
        # left policy
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                res[i] = res[i - 1] + 1
                
        # right policy
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1] and res[i] <= res[i + 1]:
                res[i] = res[i + 1] + 1
                
        return sum(res)
        
ss = Solution()
print ss.candy([2,1,2,4,3,1,2]), 'should be 13'
        