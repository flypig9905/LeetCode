'''

Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

For example,
S = "ADOBECODEBANC"
T = "ABC"
Minimum window is "BANC".

Note:
If there is no such window in S that covers all characters in T, return the emtpy string "".

If there are multiple such windows, you are guaranteed that there will always be only one unique minimum window in S.

Created on Feb 4, 2014

@author: Songfan
'''
''' two hashtable: has found, need to find
   +two pointer:   one front, one back
    
    algorithm: 
        If not all char needed are found: increase faster and update tables
        while all char are found: record result, increase slower, and update table, 
   
'''
class Solution:
    # @return a string
    def minWindow(self, S, T):
        n = len(S)
        char_need, char_have, char_T = {}, {}, {}
        for c in T:
            char_need[c] = char_need.get(c,0) + 1
            char_T[c] = char_T.get(c,0) + 1
        
        faster, slower, res = 0, 0, ''
    #    update_table_add(char_need, char_have, char_T, S)
        while faster < n:
            if char_need.keys() != []:
                self.update_table_add(char_need, char_have, char_T, S[faster])
                faster += 1
            while char_need.keys() == []:
                res_len = len(res)
                if res_len == 0 or res_len > faster-slower: res = S[slower:faster]
                slower += 1
                self.update_table_sub(char_need, char_have, char_T, S[slower-1])
        
        return res
    
    def update_table_sub(self, need, have, char_T, c):
        have[c] -= 1
        if c in char_T and have[c] < char_T[c]:
            need[c] = need.get(c,0) + 1
    
    def update_table_add(self, need, have, char_T, c):
        have[c] = have.get(c,0) + 1
        if c in need:
            need[c] -= 1
            need[c] = max(0, need[c]) # need cannot be negative
            if need[c] == 0:
                need.pop(c) 
    
S = "ADOBECODEBANC"
T = "ABC"
ss = Solution()
print ss.minWindow(S, T)    
print ss.minWindow('ab', 'a')

