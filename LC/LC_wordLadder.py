'''
Given two words (start and end), and a dictionary, find the length of shortest transformation sequence from start to end, such that:

Only one letter can be changed at a time
Each intermediate word must exist in the dictionary
For example,

Given:
start = "hit"
end = "cog"
dict = ["hot","dot","dog","lot","log"]
As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.

Note:
Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.

Created on Jan 5, 2014

@author: Songfan
'''

''' algorithm: bfs
    also, since we know start string and end string, we could also try double bfs, one from start string, one from end string
    source : http://yucoding.blogspot.com/2013/08/leetcode-question-127-word-ladder.html '''

from queue import Queue
import string

def wordLadder(start, end, d):
    # assume correct input
    q = Queue()
    q.enqueue(start)
    q.enqueue('endLevel')
    visitedWord = []
    res = 1
    while not q.isEmpty():
        tmpWord = q.dequeue()
        if tmpWord == 'endLevel':
            res += 1
            q.enqueue('endLevel')
            continue
        visitedWord.append(tmpWord)
        for i in range(len(tmpWord)):
            for c in string.lowercase[:26]:
                newWord = tmpWord[:i] + c + tmpWord[i+1:]
                if end == newWord: return res
                elif newWord in d and newWord not in visitedWord and newWord not in q:
                    q.enqueue(newWord)
    return 0

def ladderLength(start, end, dict):
    q = Queue()
    h, step = {}, 1
    h[start] = 0
    q.enqueue(start)
    q.enqueue(0)
    while not q.isEmpty():
        curr = q.dequeue()
        if curr == 0:
            if q.isEmpty(): return h.get(end,0)
            else: 
                q.enqueue(0)
                step += 1
        else:
            for i in range(len(curr)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    tmp = curr[:i] + c + curr[i+1:]
                    if tmp == end: return step
                    if tmp in dict:
                        if tmp not in h:
                            q.enqueue(tmp)
                            h[tmp] = step

start = "hit"
end = "cog"
d = ["hot","dot","dog","lot","log"]
print wordLadder(start, end, d), 'should be 4'
        
print wordLadder('a', 'c', ['a','b','c']), 'should be 1'
        
print ladderLength(start, end, d), 'should be 4'  
print ladderLength('a', 'c', ['a','b','c']), 'should be 1'    
    
    
    
    