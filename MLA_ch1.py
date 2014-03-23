'''
Created on Feb 25, 2014

@author: Songfan
'''

# 1.7 Getting started with NumPy
from numpy import *

a = random.rand(4,4)    # numpy ndarray
print type(a)

randMat = mat(random.rand(2,2))              # numpy matrix
print type(randMat)
invRandMat = randMat.I  # inverse

aMat = array([[2,0],[0,1]])
print type(aMat), aMat

indentityMat = eye(4)