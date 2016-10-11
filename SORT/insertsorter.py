#########################################################################
# File Name: insertsorter.py
# Purpose:
#	This file is to implement insert sort algo
# History:
#	Created Time: 2016-10-11
# Author: Don E-mail: dpdeng@whu.edu.cn
#########################################################################

from sorter import Sorter
import unittest

class InsertSorter(Sorter):
    def sort(self):
        for i in range(1,len(self.array)):
            key=self.array[i]
            j=i-1
            while j>=0 and key<self.array[j]:
                self.array[j+1]=self.array[j]
                j=j-1
            self.array[j+1]=key
        return self.array

class TestInsertSorter(unittest.TestCase):
    def test_sortNorm(self):
        self.assertEqual(InsertSorter([1,6,4,2]).sort(), [1,2,4,6])

    def test_sortOne(self):
        self.assertEqual(InsertSorter([1]).sort(), [1])

    def test_sortFloat(self):
        self.assertEqual(InsertSorter([1.2, 2.0, 1.5]).sort(), [1.2, 1.5, 2.0])

    def test_sortChar(self):
        self.assertEqual(InsertSorter(['c', 'b', 'a']).sort(), ['a', 'b', 'c'])

    def test_longArray(self):
        unsort_array=[i for i in range(999,0,-1)]
        sorted_array=[i for i in range(1,1000)]
        self.assertEqual(InsertSorter(unsort_array).sort(), sorted_array)

    def test_getSortTime(self):
        self.assertIsInstance(InsertSorter([1,6,5]).getSortTime(), float)

if __name__ == '__main__':
    unittest.main()
