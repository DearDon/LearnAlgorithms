#########################################################################
# File Name: unittest_quicksorter.py
# Purpose:
#	This file is to unit test quick sort method
# History:
#	Created Time: 2016-11-14
# Author: Don E-mail: dpdeng@whu.edu.cn
#########################################################################
import unittest
from quicksorter import QuickSorter

class UnitTest_QuickSorter(unittest.TestCase):
    def test_partition(self):
        self.assertEqual(QuickSorter([1,6,5]).partition([1,6,2,4,5], 0, 4), 3)
        self.assertEqual(QuickSorter([1,6,5]).partition([1,5,2,4,5], 0, 4), 3)
        self.assertEqual(QuickSorter([1,6,5]).partition([1,6,5], 0, 2), 1)

        qs=QuickSorter([1,6,5])
        self.assertEqual(qs.partition(qs.array, 0, 2), 1)
        self.assertEqual(qs.array, [1,5,6])


    def test_sortNorm(self):
        self.assertEqual(QuickSorter([1,6,5]).sort(), [1,5,6])
        self.assertEqual(QuickSorter([6,5]).sort(), [5,6])

    def test_sortNorm(self):
        self.assertEqual(QuickSorter([1,6,5]).sort(), [1,5,6])

    def test_sortOne(self):
        self.assertEqual(QuickSorter([1]).sort(), [1])

    def test_sortFloat(self):
        self.assertEqual(QuickSorter([1.2, 2.0, 1.5]).sort(), [1.2, 1.5, 2.0])

    def test_sortChar(self):
        self.assertEqual(QuickSorter(['c', 'b', 'a']).sort(), ['a', 'b', 'c'])

    def test_longArray(self):
        unsort_array=[i for i in range(999,0,-1)]
        sorted_array=[i for i in range(1,1000)]
        with self.assertRaises(RuntimeError):
            self.assertEqual(QuickSorter(unsort_array).sort(), sorted_array)

    def test_getSortTime(self):
        self.assertIsInstance(QuickSorter([1,6,5]).getSortTime(), float)

def fullSuite():
    suite=unittest.TestSuite()
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(UnitTest_QuickSorter))
    return suite

def partSuite():
    suite=unittest.TestSuite()
    suite.addTest(UnitTest_QuickSorter("test_sortNorm"))
    return suite

if __name__=='__main__':
    unittest.main()

