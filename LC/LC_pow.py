'''

Implement pow(x, n).

Created on Jan 1, 2014

@author: Songfan
'''

''' algorithm: binary search: pow(x,n) = pow(x,n//2) * pow(x, n//2) * pow(x, n%2) '''
EPSILON = .0000000001

def power(x, n):
    assert(isinstance(x, float) and isinstance(n, int)),'input error'
    if n < 0: 
        return 1.0 / _pow(x, -n, {})
    else:
        return _pow(x, n, {})

def _pow(x, n, h):
    if n == 0:
        if abs(x) > EPSILON: return 1
        else: return None 
    elif n == 1:
        return x
    elif n in h:
        return h[n]
    else:
        h[n//2] = _pow(x, n//2, h)
        h[n] = h[n//2] * h[n//2] * _pow(x, n%2, h)
        return h[n]
    
    
x = 2.0
n = -3
print power(x, n)