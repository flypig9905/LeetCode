'''

Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.

2: abc
3: def
4: ghi
5: jkl
6: mno
7: pqrs
8: tuv
9: wxyz

Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:
Although the above answer is in lexicographical order, your answer could be in any order you want.

Created on Jan 14, 2014

@author: Songfan
'''

''' thought: recursion '''
class Solution:
    # @return a list of strings, [s1, s2]

    h = {}
    h[2] = ['a','b','c']
    h[3] = ['d','e','f']
    h[4] = ['g','h','i']
    h[5] = ['j','k','l']
    h[6] = ['m','n','o']
    h[7] = ['p','q','r','s']
    h[8] = ['t','u','v']
    h[9] = ['w','x','y','z']

    def letterCombinations(self, digits):
        return self._helper(digits, len(digits) - 1)

    def _helper(self, s, k):
        assert(len(s) > k), 'input error'
        if k == -1: return [""]
        if k == 0: return self.h[int(s[0])]
        prevList = self._helper(s, k - 1)
        res = []
        for currC in self.h[int(s[k])]:
            for currS in prevList:
                tmp = currS + currC
                if tmp not in res:
                    res.append(tmp)
        return res

s = '23'
ss = Solution()
print ss.letterCombinations(s)


h = {}
h[2] = ['a','b','c']
h[3] = ['d','e','f']
h[4] = ['g','h','i']
h[5] = ['j','k','l']
h[6] = ['m','n','o']
h[7] = ['p','q','r','s']
h[8] = ['t','u','v']
h[9] = ['w','x','y','z']

def letterComboPhoneNum(s):
    # assert s is str
    return _helper(s, len(s) - 1)

def _helper(s, k):
    assert(len(s) > k), 'input error'
    if k == -1: return []
    if k == 0: return h[int(s[0])]
    prevList = _helper(s, k - 1)
    res = []
    for currC in h[int(s[k])]:
        for currS in prevList:
            tmp = currS + currC
            if tmp not in res:
                res.append(tmp)
    return res
    
s = '23'
print letterComboPhoneNum(s)