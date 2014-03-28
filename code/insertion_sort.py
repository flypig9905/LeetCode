'''
Created on Mar 27, 2014

@author: Songfan
'''

''' idea: find a right place to insert, A[i] < t < A[i+1] '''


def ins_sort_rec(seq, i):
    if i == 0: return
    ins_sort_rec(seq, i-1)  # assume the lift from 0 to i-1 is sorted
    j = i
    while j > 0 and seq[j-1] > seq[j]:
        seq[j-1], seq[j] = seq[j], seq[j-1]
        j -= 1

def ins_sort(seq):
    for i in range(1, len(seq)):
        j = i
        while j > 0 and seq[j-1] > seq[j]:
            seq[j-1], seq[j] = seq[j], seq[j-1]
            j -= 1



seq = [1,5,7,2,5,9,8,1]
ins_sort_rec(seq, len(seq)-1)
print seq

seq = [1,5,7,2,5,9,8,1]
ins_sort(seq)
print seq
