#########################################################################
# File Name: choosesorter.py
# Purpose:
#       This program is to implement choose sort method
# History:
#	Created Time: 2016-10-12
# Author: Don E-mail: dpdeng@whu.edu.cn
#########################################################################

from sorter import Sorter
import unittest

class ChooseSorter(Sorter):
    def sort(self):
        for i in range(0,len(self.array)-1):
            key=i
            for j in range(i+1,len(self.array)):
                if self.array[key]>self.array[j]:
                    key=j
            self.array[i],self.array[key]=self.array[key],self.array[i]
        return self.array

class TestChooseSorter(unittest.TestCase):
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

if __name__ == "__main__":
    unittest.main()
