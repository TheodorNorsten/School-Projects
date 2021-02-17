import unittest
from D5 import *

''' Tester för det binära sökträdet '''


class BintreeTest(unittest.TestCase):
    '''Lägger till noder i trädet och testar med metoden assertequal '''
    
    def testInsert(self):
        träd= Bintree()
        träd.store('adam',123)
        nod= träd.rot
        self.assertEqual(nod.key,'adam')
        self.assertEqual(nod.value,123)


    def testInsertMore(self):
        ''' lägger till flera noder i trädet och testar med metodeen assertequal'''
        träd = Bintree()
        träd.store(10, 10)
        träd.store(5, 5)
        träd.store(20, 20)
        nod = träd.rot
        left = nod.left
        right = nod.right
        self.assertEqual(left.value, 5)
        self.assertEqual(right.value, 20)

    def testContains(self):
        träd = Bintree()
        träd.store(10, 10)
        träd.store(5, 5)
        träd.store(20, 20)
        #self.assertIn(5, träd)
        #self.assertNotIn(8, träd)


    def testSearch(self):
        ''' lägger till noder och testar att funktionen search fungerar.'''
        träd = Bintree()
        träd.store(10, "tio")
        träd.store(5, "fem")
        träd.store(20, "tjugo")
        self.assertEqual(träd.search(10), "tio")


    def KeyError(self):
        
        träd= Bintree()
        with self.assertRaises(KeyError):
            träd.search('eva')




if __name__ == '__main__':
    unittest.main()


    
