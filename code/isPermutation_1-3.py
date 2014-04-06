'''
CTCI P73 1-3
Given two strings, decide if one is a permutation of the other

Created on Nov 20, 2013

@author: Songfan
'''
def isPermutation(s1,s2):

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

                
        