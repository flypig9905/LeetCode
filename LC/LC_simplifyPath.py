'''

Given an absolute path for a file (Unix-style), simplify it.

For example,
path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"

Corner Cases:
Did you consider the case where path = "/../"?
In this case, you should return "/".
Another corner case is the path might contain multiple slashes '/' together, such as "/home//foo/".
In this case, you should ignore redundant slashes and return "/home/foo".

Created on Feb 6, 2014

@author: Songfan
'''
from stack import Stack

def solution(path):
    n = len(path)
    if n == 0: return ''
    if path[0] != '/': return ''

    s = Stack()
    i = 0
    while i < n:
        if '/' in path:
            j = path[i:].index('/')
            dir = path[i:j+i]
            if len(dir) != 0 and dir != '.':
                if dir == '..':
                    if not s.isEmpty():
                        s.pop()
                else:
                    s.push('/' + dir)
            if j != 0:
                i += j
            else:
                i += 1
        else:
            break
    res = []
    if s.isEmpty():
        res.append('/')
    while not s.isEmpty():
        res.append(s.pop())
    res = ''.join(res[::-1])
    return res     
            
path = "/a/./b/../../c/"
print solution(path), 'should be /c'


path = "/../"
print solution(path), 'should be /'

path = "/home//foo/"
print solution(path), 'should be /home/foo'

            
        
    
    