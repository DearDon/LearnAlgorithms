#########################################################################
# File Name: unittest_heapsorter.py
# Purpose:
#	This file is to unit test heapsorter
# History:
#	Created Time: 2016-10-18
# Author: Don E-mail: dpdeng@whu.edu.cn
#########################################################################
import unittest
from heapsorter import HeapSorter

class UnitTest_HeapSorter(unittest.TestCase):
    def test_sortNorm(self):
        self.assertEqual(HeapSorter([1,6,5]).sort(), [1,5,6])

    def test_sortOne(self):
        self.assertEqual(HeapSorter([1]).sort(), [1])

    def test_sortFloat(self):
        self.assertEqual(HeapSorter([1.2, 2.0, 1.5]).sort(), [1.2, 1.5, 2.0])

    def test_sortChar(self):
        self.assertEqual(HeapSorter(['c', 'b', 'a']).sort(), ['a', 'b', 'c'])

    def test_longArray(self):
        unsort_array=[i for i in range(999,0,-1)]
        sorted_array=[i for i in range(1,1000)]
        self.assertEqual(HeapSorter(unsort_array).sort(), sorted_array)

    def test_getSortTime(self):
        self.assertIsInstance(HeapSorter([1,6,5]).getSortTime(), float)

    def test_parentIndex(self):
        hs=HeapSorter([1,6,2])
        hs.heap_size=3

        self.assertEqual(hs.heap_size, 3)
        self.assertEqual(hs.parentIndex(0), 0)
        self.assertEqual(hs.parentIndex(1), 0)
        self.assertEqual(hs.parentIndex(2), 0)

        with self.assertRaises(Exception):
            hs.parentIndex(3)
        with self.assertRaises(Exception):
            hs.parentIndex(-1)

    def test_maxChildrenIndex(self):
        hs=HeapSorter([6,2,4,1])
        hs.heap_size=4

        self.assertEqual(hs.heap_size, 4)
        self.assertEqual(hs.maxChildrenIndex(0), (2))
        self.assertEqual(hs.maxChildrenIndex(1), (3))
        self.assertEqual(hs.maxChildrenIndex(2), (2))

        with self.assertRaises(Exception):
            hs.parentIndex(4)
        with self.assertRaises(Exception):
            hs.parentIndex(-1)

    def test_heapExtractMax(self):
        hs=HeapSorter([9,6,5])
        hs.heap_size=3

        self.assertEqual(hs.heapExtractMax(), [6,5])
        self.assertEqual(hs.array, [6,5,9])
        self.assertEqual(hs.heap_size, 2)

        self.assertEqual(hs.heapExtractMax(), [5])
        self.assertEqual(hs.array, [5,6,9])
        self.assertEqual(hs.heap_size, 1)

        self.assertEqual(hs.heapExtractMax(), [])
        self.assertEqual(hs.array, [5,6,9])
        self.assertEqual(hs.heap_size, 0)

    def test_maxHeapDecreaseKey(self):
        hs=HeapSorter([9,6,7,5,3])
        hs.heap_size=5

        hs.maxHeapDecreaseKey(0,4)
        self.assertEqual(hs.array, [7,6,4,5,3])

        hs.maxHeapDecreaseKey(0,3)
        self.assertEqual(hs.array, [6,5,4,3,3])

    def test_maxHeapIncreateKey(self):
        hs=HeapSorter([6,3,5])
        hs.heap_size=3

        hs.maxHeapIncreaseKey(2,7)
        self.assertEqual(hs.array, [7,3,6])

        hs.maxHeapIncreaseKey(1,5)
        self.assertEqual(hs.array, [7,5,6])

    def test_maxHeapInsert(self):
        hs=HeapSorter([3,6,5])
        hs.heap_size=1

        hs.maxHeapInsert(1)
        self.assertEqual(hs.heap_size, 2)
        self.assertEqual(hs.array, [3,1,5])

        hs.maxHeapInsert(6)
        self.assertEqual(hs.heap_size, 3)
        self.assertEqual(hs.array, [6,1,3])

        with self.assertRaises(Exception):
            hs.minHeapInsert(6)

    def test_maxHeapBuild(self):
        hs=HeapSorter([1,4,3,2])
        hs.maxHeapBuild()
        self.assertEqual(hs.array, [4,2,3,1])

        hs=HeapSorter([4,5,3,2])
        hs.maxHeapBuild()
        self.assertEqual(hs.array, [5,4,3,2])

def fullSuite():
    suite=unittest.TestSuite()
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(UnitTest_HeapSorter))
    return suite

def partSuite():
    suite=unittest.TestSuite()
    suite.addTest(UnitTest_HeapSorter("test_sortNorm"))
    return suite

if __name__ == '__main__':
    unittest.main(verbosity=2)
