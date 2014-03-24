'''

Implement pow(x, n).

Created on Jan 1, 2014

@author: Songfan
'''

''' algorithm: binary search: pow(x,n) = pow(x,n//2) * pow(x, n//2) * pow(x, n%2) '''
class Solution:
    # @param x, a float
    # @param n, a integer
    # @return a float
    def pow(self, x, n):
        # pow(n) = pow(n//2)*pow(n//2)*pow(n%2)
        h = {}
        return self._pow(x,n,h) if n > 0 else 1/self._pow(x,-n,h)
        
    def _pow(self, x, n, h):
        if n == 0: 
            return 1.0 if abs(x) > 0.000000001 else None
        if n == 1: return x
        if n in h: return h[n]
        h[n] = self._pow(x,n//2,h) * self._pow(x,n//2,h) * self._pow(x,n%2,h)
        return h[n]
    
ss = Solution()
print ss.pow(34.00515, -3)