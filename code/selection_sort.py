'''
Created on Mar 27, 2014

@author: Songfan
'''

''' idea: select the largest item, and swap in place '''

def sel_sort_rec(seq, i):
    if i == 0: return
    max_j = i
    for j in range(i):
        # look for max item in the previous seq
        if seq[j] > seq[max_j]: max_j = j
    seq[max_j], seq[i] = seq[i], seq[max_j]
    
    # recursive call
    sel_sort_rec(seq, i-1)
    

def sel_sort(seq):    
    for i in range(len(seq)-1, 0, -1):
        max_j = i
        for j in range(i):
            # look for max item in the seq from 0 to i-1
            if seq[j] > seq[max_j]: max_j = j
        seq[max_j], seq[i] = seq[i], seq[max_j]
    
    
    
    
seq = [1,5,7,2,5,9,8,1]
sel_sort_rec(seq, len(seq)-1)
print seq

seq = [1,5,7,2,5,9,8,1]
sel_sort(seq)
print seq
