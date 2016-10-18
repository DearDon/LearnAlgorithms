#########################################################################
# File Name: unittest_insertsorter.py
# Purpose:
#	This file is to unit test insertsorter
# History:
#	Created Time: 2016-10-16
# Author: Don E-mail: dpdeng@whu.edu.cn
#########################################################################

import unittest
import insertsorter

class UnitTest_InsertSorter(unittest.TestCase):
    def test_sortNorm(self):
        self.assertEqual(insertsorter.InsertSorter([1,6,4,2]).sort(), [1,2,4,6])

    def test_sortOne(self):
        self.assertEqual(insertsorter.InsertSorter([1]).sort(), [1])

    def test_sortFloat(self):
        self.assertEqual(insertsorter.InsertSorter([1.2, 2.0, 1.5]).sort(), [1.2, 1.5, 2.0])

    def test_sortChar(self):
        self.assertEqual(insertsorter.InsertSorter(['c', 'b', 'a']).sort(), ['a', 'b', 'c'])

    def test_longArray(self):
        unsort_array=[i for i in range(999,0,-1)]
        sorted_array=[i for i in range(1,1000)]
        self.assertEqual(insertsorter.InsertSorter(unsort_array).sort(), sorted_array)

    def test_getSortTime(self):
        self.assertIsInstance(insertsorter.InsertSorter([1,6,5]).getSortTime(), float)

def fullSuite():
    suite=unittest.TestSuite()
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(UnitTest_InsertSorter))
    return suite

def partSuite():
    suite=unittest.TestSuite()
    suite.addTest(UnitTest_InsertSorter("test_sortNorm"))
    return suite

if __name__ == '__main__':
    unittest.main()
