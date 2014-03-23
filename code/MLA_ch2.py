'''
Created on Feb 25, 2014

@author: Songfan
'''
from numpy import *
import operator

# knn
def createDataset():
    group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels = ['A','A','B','B']
    return group, labels

def classify0(inX, dataset, labels, k):
    datasetSize = dataset.shape[0]  # shape = tuple(row,col)
    diffMat = tile(inX, (datasetSize,1)) - dataset  # tile = repmat for matlab
    sqDiffMat = diffMat ** 2    # element-wise square
    sqDistances = sqDiffMat.sum(axis=1) # axis=1: row sum; axis=0: col sum; default axis=None: sum row and col to a scalar
    distances = sqDistances ** .5
    sortedDistIndicies = distances.argsort()    # return sorted idx
    classCount = {}
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1
    sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1), reverse=True) # sort hashtable based on value, desceding
    return sortedClassCount[0][0]

group, labels = createDataset()
print classify0([0,0], group, labels, 3)



