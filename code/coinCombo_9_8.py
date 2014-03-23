'''
CTCI 9-8

given coin with 25, 10, 5, 1, find how many ways to represent n

Created on Dec 2, 2013

@author: Songfan
'''

""" need to reimplement """
def coinCombo(n):
    assert(n>=0 and isinstance(n,int)),'input error'
    if n==0: return 0
    if n==1: return 1
    h = {}  # cache
    if n>=1 and n<5:
        h[n] = coinCombo(n-1)
    elif n>=5 and n<10:
        h[n] = 1 + coinCombo(n-5)
    elif n>=10 and n<25:
        h[n] = 1 + coinCombo(n-5) + coinCombo(n-10)
    else:
        h[n] = 1 + coinCombo(n-5) + coinCombo(n-10) + coinCombo(n-25)
    return h[n]

n = 10
print coinCombo(n)