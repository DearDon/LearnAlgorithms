#########################################################################
# File Name: sorter.py
# Purpose:
#    This program is to implement Sort algo with class
# History:
#    Created Time: Tue 06 Sep 2016 10:33:12 PM CST
#    Author: Don    E-mail: dpdeng@whu.edu.cn
#########################################################################
import timeit
import unittest

class Sorter():
    def __init__(self, array):
        self.array=array

    def sort(self):
        raise NotImplementedError

    def getSortTime(self):

        starttime = timeit.default_timer()
        self.sort()
        stoptime = timeit.default_timer()

        return stoptime-starttime

class HeapSorter(Sorter):
    def sort(self):
        pass #wait to implement

    def heap_minimum(self):
        return self.array[0]

    def heap_extract_min(self):
        pass

    def heap_decrease_key(self):
        pass

    def min_heap_insert(self):
        pass

class TestSorter(unittest.TestCase):
    def test_init(self):
        self.assertIsInstance(Sorter([1,2]), Sorter)

    def test_sort(self):
        with self.assertRaises(NotImplementedError):
            Sorter([1,3]).sort()

if __name__ == '__main__':
    unittest.main()
