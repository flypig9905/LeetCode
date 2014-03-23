'''
CTCI P73 1-3
Given two strings, decide if one is a permutation of the other

Created on Nov 20, 2013

@author: Songfan
'''
def isPermutation(s1,s2):
    """ two hash table implementation: could be better by using only one hash table """
#     try:
#         assert (type(s1) is str and type(s2) is str), "Input Error: input should be two strings!"
#         if(len(s1)!=len(s2)):
#             # permutations have to be of same size
#             return False
#         charCount1 = {}
#         charCount2 = {}
#         for i in range(len(s1)):
#             if s1[i] not in charCount1:
#                 charCount1[s1[i]]=1
#             else:
#                 charCount1[s1[i]]+=1
#             if s2[i] not in charCount2:
#                 charCount2[s2[i]]=1
#             else:
#                 charCount2[s2[i]]+=1
#         keys1 = charCount1.keys()
#         keys2 = charCount2.keys()
#         if(keys1!=keys2):
#             # permutations contain same set of keys
#             return False
#         for k in keys1:
#             if charCount1[k] != charCount2[k]:
#                 # the character occurance should be the same for permutations
#                 return False
#         return True
#     except AssertionError as e:
#         print e.args[0]
#         return False
    """ one hash table implementation """
    try:
        assert ((type(s1) is str and type(s2) is str) or (type(s1) is unicode and type(s2) is unicode)), "Input Error: input should be two strings!"
        if(len(s1)!=len(s2)):
            # permutations have to be of same size
            return False
        charCount = {}
        for i in range(len(s1)):
            charCount[s1[i]] = charCount.get(s1[i],0)+1
        for k in s2:
            if charCount.get(k,0) <= 0:
                return False
            else:
                charCount[k]-=1
        return True
    except AssertionError as e:
#         print e.args[0]
        return False
        

# unitest
posTests = [[u'aeiou', u'aiuoe'], ['','']]
negTests = [['','aei'], ['abcd','abcc'], ['abc','ab'], [112,'ewa']]

for i,testPair in enumerate(posTests):
    if isPermutation(testPair[0],testPair[1]):
        print 'Positive test '+str(i)+' passed'
    else:
        print 'Positive test '+str(i)+' failed'

for i,testPair in enumerate(negTests):
    if not isPermutation(testPair[0],testPair[1]):
        print 'Negative test '+str(i)+' passed'
    else:
        print 'Negative test '+str(i)+' failed'

                
        