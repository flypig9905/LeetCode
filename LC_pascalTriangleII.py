'''

Given an index k, return the kth row of the Pascal's triangle.

For example, given k = 3,
Return [1,3,3,1].

Note:
Could you optimize your algorithm to use only O(k) extra space?

Created on Feb 9, 2014

@author: Songfan
'''

''' O(k) space: rollover array from rear to front, add 1 to the rear of the updated array '''
def solution(k):
    res = []
    for _ in range(k):
        ''' add from back '''
        for j in range(len(res) - 1, 0, -1):
            res[j] = res[j-1] + res[j]
        res.append(1)
    
    return res

print solution(4)