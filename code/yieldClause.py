'''
Created on Mar 27, 2014

@author: Songfan
'''
def ff(a):
    for x in xrange(5):
        for y in xrange(5):
            if x != y:
                for z in xrange(5):
                    if y != z:
                        yield (x, y, z)
                          
                      
g = ff(3)
# for i in g:
#     print i
#     

import itertools
horse = [1,2,3,4]
race = itertools.permutations(horse)
print list(race)
    
a,b,c,d = range(4)
print a
print b
print c
    
    