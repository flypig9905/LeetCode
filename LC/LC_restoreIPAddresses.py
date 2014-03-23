'''

Given a string containing only digits, restore it by returning all possible valid IP address combinations.

For example:
Given "25525511135",

return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)

Created on Jan 28, 2014

@author: Songfan
'''

''' dfs:
        step: to track the level of search
        res: store result
        isValid: a function to make sure a certain string is a valid ip sub array
'''

''' dfs main function summary: 
        1. need variables to track the current answer, entire result, and the stop criterion
        2. correct case to add current answer to entire result
        3. iterate over all possibilities for remaining problem, 
            append current choice to current answer
            recursive call dfs at next level
            pop out the current choice
        4. return
'''
            
class Solution:
    # @param s, a string
    # @return a list of strings
    def restoreIpAddresses(self, s):
        res = self._dfs(s, [], [], 0)
        res = ['.'.join(r) for r in res]
        return res

    def _dfs(self, s, curr, res, step):
        if step == 4:
            if s is '':
                tmp = curr[:]
                res.append(tmp)
            return
        for i in range(1, 4):
            if len(s) >= i and self.isValid(s[:i]):
                curr.append(s[:i])
                self._dfs(s[i:], curr, res, step + 1)
                curr.pop()
        return res
                
    def isValid(self, s):
        if s == '0': return True
        elif s[0] != '0' and (0 < int(s) and int(s) <= 255): return True
        else: return False
    
   
    
s = '25525511135'
ss = Solution()
print ss.restoreIpAddresses(s), 'should be ["255.255.11.135", "255.255.111.35"]'

s = '010010'
print ss.restoreIpAddresses(s), 'should be ["0.10.0.10","0.100.1.0"]'

print ss.isValid('01'), 'should be False'
            