'''
given a lower case string, generate all possible combinations including upper and lower case

Created on Mar 13, 2014

@author: Songfan
'''

'''
dfs
'''

def caseCombo(s):
    result, interm, index = [], [], 0
    _dfs(s, result, interm, index)
    return result

def _dfs(s, result, interm, index):
    if index >= len(s):
        result.append(''.join(interm[:]))
        return
    c = s[index]
    # search lower case
    interm.append(c)
    _dfs(s, result, interm, index+1)
    interm.pop()
        
    # sear upper case
    interm.append(c.upper())
    _dfs(s, result, interm, index+1)
    interm.pop()

print caseCombo('abc')