'''
generate n-paris of parentheses
n=1: ()
n=2: (()), ()()

Created on Dec 2, 2013

@author: Songfan
'''
def validParen(n):
    assert(n>=0 and isinstance(n,int)),'input error'
    if n==0: return ['']
    if n==1: return ['()']
    h = {}
    if n in h.keys(): return h[n]
    else:
        prev = validParen(n-1)
        result = []
        for c in prev:
            for i in range(1,len(c)+1):
                tmp = c[:i]+'()'+c[i:]
                if tmp not in result:
                    result.append(tmp)
        h[n] = result
        return result
    

n = 5
print validParen(n)
print len(validParen(n))