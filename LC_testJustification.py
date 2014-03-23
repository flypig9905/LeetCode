'''

Given an array of words and a length L, format the text such that each line has exactly L characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly L characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left justified and no extra space is inserted between words.

For example,
words: ["This", "is", "an", "example", "of", "text", "justification."]
L: 16.

Return the formatted lines as:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
Note: Each word is guaranteed not to exceed L in length.

click to show corner cases.

Corner Cases:
A line other than the last line might contain only one word. What should you do in this case?
In this case, that line should be left-justified.

Created on Feb 3, 2014

@author: Songfan
'''
def solution(words, L):
    n = len(words)
    if n == 0: return words
    
    res = []
    currWords = []
    availableSpace = L
    
    for wi in range(n):
        w = words[wi]
        wLen = len(w)
        if wLen < availableSpace:
            currWords.append(w)
            availableSpace -= wLen + 1
        else:
            res.append(combineWords(currWords, L))
            currWords = [w]
            availableSpace = L - wLen - 1
    if len(currWords):
        res.append(w + ' ' * (L - wLen))
    return res
    
    
def combineWords(words, L):
    wordNum = len(words)
    wordLen = 0
    for w in words:
        wordLen += len(w)
    spaceNumTotal = L - wordLen
    if wordNum == 1:
        return words[0] + ' ' * spaceNumTotal
    spaceNum = spaceNumTotal // (wordNum - 1)
    additionalSpace = spaceNumTotal % (wordNum - 1)
    
    res = ''
    for wi in range(wordNum):
        if wi == wordNum - 1:
            res += words[wi]
        elif additionalSpace > 0:
            res += words[wi] + ' ' * (spaceNum + 1)
            additionalSpace -= 1
        else:
            res += words[wi] + ' ' * spaceNum
    return res
    
    
    
    
    
    
words = ["This", "is", "an", "example", "of", "text", "justification."]
L = 16
print solution(words, L)


words = ["This", "is", "an", "vervverycrazy", "example", "of", "text", "justification."]
L = 16
print solution(words, L)














