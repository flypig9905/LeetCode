'''

Follow up for "Search in Rotated Sorted Array":
What if duplicates are allowed?

Would this affect the run-time complexity? How and why?

Write a function to determine if a given target is in the array.

Created on Jan 24, 2014

@author: Songfan
'''

''' thought: because duplicates is allowed, what can happen is [1,3,1,1,1], which we don't know where to search, we have to search for 
both sides in this case '''

class Solution:
    # @param A a list of integers
    # @param target an integer
    # @return a boolean
    def search(self, A, e):
        n = len(A)
        if n == 0: return -1
        left = 0
        right = n - 1
        while left <= right:
            mid = (left + right) // 2
            if A[mid] == e: return True
            ''' caveat: compare A[left] to A[mid] '''
            if A[left] < A[mid]: 
                ''' this means left half is sorted '''
                if A[left] <= e and e < A[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            elif A[left] > A[mid]:
                ''' this means right half is sorted '''
                if A[mid] < e and e <= A[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                ''' we don't know which half is sorted, has to increase left for decrease right similar to linear scan '''
                left += 1
        return False    
    
A = [1,3,1,1,1,1]         
e = 2
ss = Solution()
print ss.search(A, e), 'should be False'

e = 3
print ss.search(A, e), 'should be True'

e = 1
print ss.search(A, e), 'should be True'
