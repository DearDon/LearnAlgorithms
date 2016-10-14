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
        super(HeapSorter, self).__init__(array)
        self.heap_size=0

    def sort(self):
        pass #wait to implement

    def minHeapBuild(self):#Done
        self.heap_size=1
        for i in range(1,len(self.array)):
            self.minHeapInsert(self.array[i])

    def heapMinimum(self):#Done
        return self.array[0]

    def heapExtractMin(self):
        pass

    def heapDecreaseKey(self, i, key):#Done
        if self.heap_size <= i:
            raise Exception(str(i)+" is beyond heap range")
        elif self.array[i] < key:
            raise Exception(str(key)+" is already larger than array[i] "+str(self.array[i]))
        self.array[i]=key
        while i != 0 and self.array[i]<self.array[self.parentIndex(i)]:
            self.array[i], self.array[self.parentIndex(i)]=self.array[self.parentIndex(i)], self.array[i]
            i=self.parentIndex(i)

    def minHeapInsert(self, key):#Done
        if self.heap_size == len(self.array):
            raise Exception("can't insert, array is full")
        self.heap_size += 1
        self.array[self.heap_size-1]=float("inf")
        self.heapDecreaseKey(self.heap_size-1,key)

    def parentIndex(self,i):#Done
        if self.heap_size <= i or i == 0:
            raise Exception("element with index "+str(i)+" don't have parentIndex")
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
        hs.heap_size=3

        self.assertEqual(hs.heap_size, 3)
        self.assertEqual(hs.parentIndex(1), 0)
        self.assertEqual(hs.parentIndex(2), 0)

        with self.assertRaises(Exception):
            hs.parentIndex(3)
        with self.assertRaises(Exception):
            hs.parentIndex(0)

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

if __name__ == '__main__':
    unittest.main(verbosity=2)
