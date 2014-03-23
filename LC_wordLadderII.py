'''

Given two words (start and end), and a dictionary, find all shortest transformation sequence(s) from start to end, such that:

Only one letter can be changed at a time
Each intermediate word must exist in the dictionary
For example,

Given:
start = "hit"
end = "cog"
dict = ["hot","dot","dog","lot","log"]
Return
  [
    ["hit","hot","dot","dog","cog"],
    ["hit","hot","lot","log","cog"]
  ]
Note:
All words have the same length.
All words contain only lowercase alphabetic characters.

Created on Jan 5, 2014

@author: Songfan
'''

''' thought: bfs and add hashtable to store the previous word for each element '''

from queue import Queue
import string

def wordLadderII(start, end, d):
    q = Queue()
    q.enqueue(start)
    q.enqueue('endLevel')
    h = {}
    res = 1
    visitedWord = []
    while not q.isEmpty():
        tmpWord = q.dequeue()
        if tmpWord == 'endLevel':
            res += 1
            q.enqueue('endLevel')
        else:
            for i in range(len(tmpWord)):
                for c in string.lowercase[:26]:
                    newWord = tmpWord[:i] + c + tmpWord[i+1:]
                    if newWord == end:
                        curr = [newWord]
                        prev = h.get(newWord,[tmpWord])
                        prev.extend(curr)
                        return prev
                    elif newWord in d:
                        prev = h.get(newWord,[tmpWord])
                        prevCopy = prev[:]
                        prevCopy.append(tmpWord)
                        h[newWord] = prevCopy
                        if newWord not in q and newWord not in visitedWord:
                            q.enqueue(newWord)
                            
    return 0

start = 'hit'
end = 'dot'
d = ["hot","dot","dog","lot","log"]
print wordLadderII(start, end, d)