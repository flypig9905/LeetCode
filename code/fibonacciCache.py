'''
Created on Nov 18, 2013

@author: Songfan
'''
import collections
import functools
import time

class memoized(object):
    '''Decorator. Caches a function's return value each time it is called.
    If called later with the same arguments, the cached value is returned
    (not reevaluated).
    '''
    def __init__(self, func):
        self.func = func
        self.cache = {}
    
    def __call__(self, *args):
        if not isinstance(args, collections.Hashable):
            # uncacheable. a list, for instance.
            # better to not cache than blow up.
            return self.func(*args)
        if args in self.cache:
            return self.cache[args]
        else:
            value = self.func(*args)
            self.cache[args] = value
            return value
   
#     def __repr__(self):
#         '''Return the function's docstring.'''
#         return self.func.__doc__
#     
#     def __get__(self, obj, objtype):
#         '''Support instance methods.'''
#         return functools.partial(self.__call__, obj)

def fibonacci(n):
    "Return the nth fibonacci number."
    if n in (0, 1):
        return n
    return fibonacci(n-1) + fibonacci(n-2)

@memoized
def fibonacciCashe(n):
    "Return the nth fibonacci number."
    if n in (0, 1):
        return n
    return fibonacciCashe(n-1) + fibonacciCashe(n-2)

n = 30
start_time = time.time()
print fibonacci(n)
print time.time() - start_time, "seconds"

start_time = time.time()
print fibonacciCashe(n)
print time.time() - start_time, "seconds"

