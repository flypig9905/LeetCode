'''

Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

Created on Jan 29, 2014

@author: Songfan
'''
class TreeNode:
    def __init__(self, val = None, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
        
    def __str__(self):
        return str(self.val)
    
class BinaryTree:
    def __init__(self, root = None):
        self.root = root
        
    def __str__(self):
        return self._display(self.root)
    
    def _display(self, root):
        if root is None: return '*'
        result = str(root.val) + '(' + self._display(root.left) + ',' + self._display(root.right) + ')'
        return result

class ListNode:
    def __init__(self, val = None, next = None):
        self.val = val
        self.next = next
    
    def __str__(self):
        return str(self.val)
    
class LinkedList:
    def __init__(self, head = None):
        self.head = head
        
    def __str__(self):
        cur = self.head
        res = []
        while cur:
            res.append(str(cur.val))
            cur = cur.next
        return '->'.join(res)

''' bottom up approach: O(N) time, use length in the recursive call for easier implementation '''
class Solution:
    # @param head, a list node
    # @return a tree node
    def sortedListToBST(self, head):
        n = 0
        curr = head
        while curr:
            n += 1
            curr = curr.next
        return self.buildBST(head, 0, n - 1)
    
    def buildBST(self, node, first, last):
        if first > last: return None
        mid = first + (last - first) // 2
        left = self.buildBST(node, first, mid - 1)
        
        # find mid node as the parent
        cnt = mid - first
        curr = node
        while cnt > 0:
            curr = curr.next
            cnt -= 1
        parent = TreeNode(curr.val)
        parent.left = left
        
        parent.right = self.buildBST(curr.next, mid + 1, last)
        return parent
        

    
    
n6 = ListNode(6)
n5 = ListNode(5, n6)
n4 = ListNode(4, n5)
n3 = ListNode(3, n4)
n2 = ListNode(2, n3)
n1 = ListNode(1, n2)
print LinkedList(n1)
ss = Solution()
n = ss.sortedListToBST(n1)
print BinaryTree(n)