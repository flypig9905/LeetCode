'''
Created on Nov 7, 2013

@author: Songfan
'''
def checkTriangle(a,b,c):
    return a+b>c and a+c>b and c+b>a

print checkTriangle(2,4,3)
print checkTriangle(1,5,9)