#########################################################################
# File Name: unittest_randomquicksorter.py
# Purpose:
#	This file is to unit test random quick sort method
# History:
#	Created Time: 2016-11-15
# Author: Don E-mail: dpdeng@whu.edu.cn
#########################################################################
import unittest
from randomquicksorter import RandomQuickSorter

class UnitTest_RandomQuickSorter(unittest.TestCase):
    def test_partition(self):
        qs=RandomQuickSorter([1,6,5])
        self.assertEqual(qs.partition(qs.array, 0, 2), 1)
        self.assertEqual(qs.array, [1,5,6])


    def test_sortNorm(self):
        self.assertEqual(RandomQuickSorter([1,6,5]).sort(), [1,5,6])
        self.assertEqual(RandomQuickSorter([6,5]).sort(), [5,6])

    def test_sortNorm(self):
        self.assertEqual(RandomQuickSorter([1,6,5]).sort(), [1,5,6])

    def test_sortOne(self):
        self.assertEqual(RandomQuickSorter([1]).sort(), [1])

    def test_sortFloat(self):
        self.assertEqual(RandomQuickSorter([1.2, 2.0, 1.5]).sort(), [1.2, 1.5, 2.0])

    def test_sortChar(self):
        self.assertEqual(RandomQuickSorter(['c', 'b', 'a']).sort(), ['a', 'b', 'c'])

    def test_longArray(self):
        unsort_array=[i for i in range(999,0,-1)]
        sorted_array=[i for i in range(1,1000)]
        self.assertEqual(RandomQuickSorter(unsort_array).sort(), sorted_array)
        # with self.assertRaises(RuntimeError):
            # self.assertEqual(RandomQuickSorter(unsort_array).sort(), sorted_array)

    def test_getSortTime(self):
        self.assertIsInstance(RandomQuickSorter([1,6,5]).getSortTime(), float)

def fullSuite():
    suite=unittest.TestSuite()
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(UnitTest_RandomQuickSorter))
    return suite

def partSuite():
    suite=unittest.TestSuite()
    suite.addTest(UnitTest_RandomQuickSorter("test_sortNorm"))
    return suite

if __name__=='__main__':
    unittest.main()
