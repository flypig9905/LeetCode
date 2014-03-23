'''
Created on Nov 19, 2013

@author: Songfan
'''
import unittest

def isPermutation(s1,s2):
    """ one hash table implementation """
    try:
        assert ((type(s1) is str and type(s2) is str) or (type(s1) is unicode and type(s2) is unicode)), "Input Error: input should be two strings!"
        if(len(s1)!=len(s2)):
            # permutations have to be of same size
            return False
        charCount = {}
        for i in range(len(s1)): 
            assert (s1[i]!=' '),"Input Error: input string should not contain space"
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

class isPermutationTest(unittest.TestCase):

    def testNormalCase(self):
        self.assertTrue(isPermutation('aeiou','aiuoe'))

    def testDifferentLength(self):
        self.assertFalse(isPermutation('abcd','abc'))

    def testEmpty(self):
        self.assertTrue(isPermutation('',''))
        self.assertFalse(isPermutation('a',''))

    def testRedundantSpacing(self):
        self.assertFalse(isPermutation('aei  ou','a ioue'))

    def testUnicode(self):
        self.assertTrue(isPermutation(u'abcde',u'acdbe'))

    def testExactlyOneArgument(self):
        self.assertRaises(TypeError, isPermutation)
        self.assertRaises(TypeError, isPermutation, 'one')
        self.assertRaises(TypeError, isPermutation, 'one', 'two', 'three')

    def testMustBeString(self):
        self.assertRaises((AttributeError,TypeError), isPermutation, 1)

if __name__=='__main__':
    unittest.main()