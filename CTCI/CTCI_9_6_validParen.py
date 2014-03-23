'''
generate n-paris of parentheses
n=1: ()
n=2: (()), ()()

Created on Dec 2, 2013

@author: Songfan
'''
# def validParen1(n):
#     assert(n>=0 and isinstance(n,int)),'input error'
#     if n==0: return ['']
#     if n==1: return ['()']
#     h = {}
#     if n in h.keys(): return h[n]
#     else:
#         prev = validParen1(n-1)
#         result = []
#         for c in prev:
#             for i in range(1,len(c)+1):
#                 tmp = c[:i]+'()'+c[i:]
#                 if tmp not in result:
#                     result.append(tmp)
#         h[n] = result
#         return result
    

def validParen(n):
    assert(isinstance(n,int) and n>=0),'input error'
    return _validParen(n,{})
    
    
def _validParen(n,h):
    if n==0: return ['']
    if n==1: return ['()']
    if n in h: return h[n]
    prev = _validParen(n-1,h)
    result = []
    for e in prev:
        for i in range(len(e)):
            curr = e[:i]+'()'+e[i:]
            if curr not in result:
                result.append(curr)
    h[n] = result
    return h[n]    
    



n = 4
print validParen(n)
print len(validParen(n))