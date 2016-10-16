#########################################################################
# File Name: sorter_unittest.py
# Purpose:
#	This file is to test sorter
# History:
#	Created Time: 2016-10-16
# Author: Don E-mail: dpdeng@whu.edu.cn
#########################################################################
import unittest
import sorter

class Sorter_UnitTest(unittest.TestCase):
    def test_init(self):
        self.assertIsInstance(sorter.Sorter([1,2]), sorter.Sorter)

    def test_sort(self):
        with self.assertRaises(NotImplementedError):
            sorter.Sorter([1,3]).sort()

def fullSuite():
    suite=unittest.TestSuite()
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(Sorter_UnitTest))
    return suite

def partSuite():
    suite=unittest.TestSuite()
    suite.addTest(Sorter_UnitTest("test_init"))
    return suite

if __name__ == '__main__':
    unittest.main()
