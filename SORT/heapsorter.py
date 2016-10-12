#########################################################################
# File Name: heapsorter.py
# Purpose:
#	This file is to implement heap sort method
# History:
#	Created Time: 2016-10-12
# Author: Don E-mail: dpdeng@whu.edu.cn
#########################################################################
import unittest
from sorter import Sorter

class HeapSorter(Sorter):
    def __init__(self, array):
        super(HeapSorter, self).__init__()
        self.heap_size=0
    def sort(self):
        pass #wait to implement

    def heapMinimum(self):
        return self.array[0]

    def heapExtractMin(self):
        pass

    def heapDecreaseKey(self):
        pass

    def minHeapInsert(self):
        pass

    def parentIndex(self,i):
        if self.heap_size < i or i == 0:
            return Exception

        return (i-1)/2

class TestHeapSorter(unittest.TestCase):
    @unittest.skip("NotImplemented")
    def test_sortNorm(self):
        self.assertEqual(HeapSorter([1,6,5]).sort(), [1,5,6])

    @unittest.skip("NotImplemented")
    def test_sortOne(self):
        self.assertEqual(HeapSorter([1]).sort(), [1])

    @unittest.skip("NotImplemented")
    def test_sortFloat(self):
        self.assertEqual(HeapSorter([1.2, 2.0, 1.5]).sort(), [1.2, 1.5, 2.0])

    @unittest.skip("NotImplemented")
    def test_sortChar(self):
        self.assertEqual(HeapSorter(['c', 'b', 'a']).sort(), ['a', 'b', 'c'])

    @unittest.skip("NotImplemented")
    def test_longArray(self):
        unsort_array=[i for i in range(999,0,-1)]
        sorted_array=[i for i in range(1,1000)]
        self.assertEqual(HeapSorter(unsort_array).sort(), sorted_array)

    @unittest.skip("NotImplemented")
    def test_getSortTime(self):
        self.assertIsInstance(HeapSorter([1,6,5]).getSortTime(), float)

    def test_devise(self):
        self.assertEqual(1/2, 0)

    def test_parentIndex(self):
        hs=HeapSorter([1,6,2])
        self.assertEqual(hs.parentIndex(1), 0)
        self.assertEqual(hs.parentIndex(2), 0)
        with self.assertRaises(Exception):
            hs.parentIndex(0)


if __name__ == '__main__':
    unittest.main(verbosity=2)
