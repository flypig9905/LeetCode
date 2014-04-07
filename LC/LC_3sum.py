'''
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:
Elements in a triplet (a,b,c) must be in non-descending order. (ie, a <= b <= c)
The solution set must not contain duplicate triplets.
    For example, given array S = {-1 0 1 2 -1 -4},

    A solution set is:
    (-1, 0, 1)
    (-1, -1, 2)


Created on Dec 30, 2013

@author: Songfan
'''


''' algorithm O(N^2): first sort the array, then have two pointers moving from the head and tail of list '''
def sum3(A):
    A.sort()
    n = len(A)
    result = []
    for i in range(n - 1):
        j = i + 1
        k = n - 1
        while j < k:
            curSum = A[i] + A[j] + A[k]
            if curSum == 0:
                ''' alert: need to seperate the if statement and update both j and k '''
                if (A[i],A[j],A[k]) not in result:
                    result.append((A[i], A[j], A[k]))                    
                j += 1
                k -= 1
            elif curSum < 0:
                j += 1
            elif curSum > 0:
                k -= 1
     
    return result


A = [-1, 0, 1, 2, -1, -4]
print sum3(A)
