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
        self.assertEqual(HeapSorter([1,6,5]).sort(), [6,5,1])

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

    def test_minChildrenIndex(self):
        hs=HeapSorter([1,2,6,4])
        hs.heap_size=4

        self.assertEqual(hs.heap_size, 4)
        self.assertEqual(hs.minChildrenIndex(0), (1))
        self.assertEqual(hs.minChildrenIndex(1), (3))
        self.assertEqual(hs.minChildrenIndex(2), (2))

        with self.assertRaises(Exception):
            hs.parentIndex(4)
        with self.assertRaises(Exception):
            hs.parentIndex(-1)

    def test_heapExtractionMin(self):
        hs=HeapSorter([3,6,5,7,9])
        hs.heap_size=5

        self.assertEqual(hs.heapExtractMin(), [5,6,9,7])
        self.assertEqual(hs.array, [5,6,9,7,3])
        self.assertEqual(hs.heap_size, 4)

        self.assertEqual(hs.heapExtractMin(), [6,7,9])
        self.assertEqual(hs.array, [6,7,9,5,3])
        self.assertEqual(hs.heap_size, 3)

        self.assertEqual(hs.heapExtractMin(), [7,9])
        self.assertEqual(hs.array, [7,9,6,5,3])
        self.assertEqual(hs.heap_size, 2)

        self.assertEqual(hs.heapExtractMin(), [9])
        self.assertEqual(hs.array, [9,7,6,5,3])
        self.assertEqual(hs.heap_size, 1)

        self.assertEqual(hs.heapExtractMin(), [])
        self.assertEqual(hs.array, [9,7,6,5,3])
        self.assertEqual(hs.heap_size, 0)

    def test_increateKey(self):
        hs=HeapSorter([3,6,5,7,9])
        hs.heap_size=5

        hs.heapIncreaseKey(0,4)
        self.assertEqual(hs.array, [4,6,5,7,9])

        hs.heapIncreaseKey(0,8)
        self.assertEqual(hs.array, [5,6,8,7,9])

        hs.heapIncreaseKey(0,8)
        self.assertEqual(hs.array, [6,7,8,8,9])

    def test_decreateKey(self):
        hs=HeapSorter([3,6,5])
        hs.heap_size=3

        hs.heapDecreaseKey(1,4)
        self.assertEqual(hs.array, [3,4,5])

        hs.heapDecreaseKey(2,2)
        self.assertEqual(hs.array, [2,4,3])

    def test_minHeapInsert(self):
        hs=HeapSorter([3,6,5])
        hs.heap_size=1

        hs.minHeapInsert(1)
        self.assertEqual(hs.heap_size, 2)
        self.assertEqual(hs.array, [1,3,5])

        hs.minHeapInsert(1)
        self.assertEqual(hs.heap_size, 3)
        self.assertEqual(hs.array, [1,3,1])

        with self.assertRaises(Exception):
            hs.minHeapInsert(6)

    def test_minHeapBuild(self):
        hs=HeapSorter([1,4,3,2])
        hs.minHeapBuild()
        self.assertEqual(hs.array, [1,2,3,4])

        hs=HeapSorter([4,5,3,2])
        hs.minHeapBuild()
        self.assertEqual(hs.array, [2,3,4,5])

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
