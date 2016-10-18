#########################################################################
# File Name: unittest_choosesorter.py
# Purpose:
#	This file is to unit test choosesorter
# History:
#	Created Time: 2016-10-16
# Author: Don E-mail: dpdeng@whu.edu.cn
#########################################################################
import unittest
from choosesorter import ChooseSorter

class UnitTest_ChooseSorter(unittest.TestCase):
    def test_sortNorm(self):
        self.assertEqual(ChooseSorter([1,6,5]).sort(), [1,5,6])

    def test_sortOne(self):
        self.assertEqual(ChooseSorter([1]).sort(), [1])

    def test_sortFloat(self):
        self.assertEqual(ChooseSorter([1.2, 2.0, 1.5]).sort(), [1.2, 1.5, 2.0])

    def test_sortChar(self):
        self.assertEqual(ChooseSorter(['c', 'b', 'a']).sort(), ['a', 'b', 'c'])

    def test_longArray(self):
        unsort_array=[i for i in range(999,0,-1)]
        sorted_array=[i for i in range(1,1000)]
        self.assertEqual(ChooseSorter(unsort_array).sort(), sorted_array)

    def test_getSortTime(self):
        self.assertIsInstance(ChooseSorter([1,6,5]).getSortTime(), float)

def fullSuite():
    suite=unittest.TestSuite()
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(UnitTest_ChooseSorter))
    return suite

def partSuite():
    suite=unittest.TestSuite()
    suite.addTest(UnitTest_ChooseSorter("test_sortNorm"))
    return suite

if __name__ == "__main__":
    unittest.main()
