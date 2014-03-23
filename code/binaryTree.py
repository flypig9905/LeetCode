'''
Created on Nov 23, 2013

@author: Songfan
'''
import random

class TreeNode:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data
    
    def __str__(self):
        return str(self.data)
    
#binary tree python
class BinaryTree:
    def __init__(self, data):
        self.root = None
        #-1 means the depth has not been calculated yet.
        self.depth = -1

    def insert(self, root, data):
        if root == None:
            self.insert(self.root, TreeNode(data))
            return
        elif not root.left:
            


    def __str__(self):
        if self.root is None: return '<empty tree>'
        def recurse(node):
            if node is None: return [], 0, 0
            label = str(node.data)
            left_lines, left_pos, left_width = recurse(node.left)
            right_lines, right_pos, right_width = recurse(node.right)
            middle = max(right_pos + left_width - left_pos + 1, len(label), 2)
            pos = left_pos + middle // 2
            width = left_pos + middle + right_width - right_pos
            while len(left_lines) < len(right_lines):
                left_lines.append(' ' * left_width)
            while len(right_lines) < len(left_lines):
                right_lines.append(' ' * right_width)
            if (middle - len(label)) % 2 == 1 and node.parent is not None and \
               node is node.parent.left and len(label) < middle:
                label += '.'
            label = label.center(middle, '.')
            if label[0] == '.': label = ' ' + label[1:]
            if label[-1] == '.': label = label[:-1] + ' '
            lines = [' ' * left_pos + label + ' ' * (right_width - right_pos),
                     ' ' * left_pos + '/' + ' ' * (middle-2) +
                     '\\' + ' ' * (right_width - right_pos)] + \
              [left_line + ' ' * (width - left_width - right_width) +
               right_line
               for left_line, right_line in zip(left_lines, right_lines)]
            return lines, pos, width
        return '\n'.join(recurse(self.root) [0])
        
#Testing

#building testcase 1
bt = BinaryTree(random.randint(0, 100))
for c1 in xrange(0,5):
    bt2 = BinaryTree(random.randint(0, 100))
    bt2.left = bt
    bt=bt2
    
print bt