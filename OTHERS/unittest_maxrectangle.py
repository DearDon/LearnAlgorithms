#########################################################################
# File Name: unittest_maxrectangle.py
# Purpose:
#	This file is to do unit test
# History:
#	Created Time: 2016-10-22
# Author: Don E-mail: dpdeng@whu.edu.cn
#########################################################################
import unittest
from maxrectangle import MaxRectangle
from maxrectangle import Stack

class UnitTest_MaxRectangle(unittest.TestCase):
    def test_init(self):
        mr=MaxRectangle([3,1,2])
        self.assertEqual(mr.height_array, [3,1,2])
        self.assertEqual(mr.left_boundary, [-1,-1,-1])
        self.assertEqual(mr.right_boundary, [3,3,3])

        mr=MaxRectangle([])
        self.assertEqual(mr.height_array, [])
        self.assertEqual(mr.left_boundary, [])
        self.assertEqual(mr.right_boundary, [])

    def test_calMaxSize(self):
        mr=MaxRectangle([1,6,5,4])
        self.assertEqual(mr.calMaxSize(), 'SUCCESS')
        self.assertEqual(mr.maxsize, 12)
        self.assertEqual(mr.maxlb, 0)
        self.assertEqual(mr.maxrb, 4)

        mr=MaxRectangle([3,1,2])
        self.assertEqual(mr.calMaxSize(), 'SUCCESS')
        self.assertEqual(mr.maxsize, 3)
        self.assertEqual(mr.maxlb, -1)
        self.assertEqual(mr.maxrb, 1)

        mr=MaxRectangle([])
        with self.assertRaises(Exception):
            mr.calMaxSize()

    def test_getSizeBoundary(self):
        mr=MaxRectangle([3,1,2])
        self.assertEqual(mr.getMaxSize(), mr.maxsize)
        self.assertEqual(mr.getMaxBoundary(), (mr.maxlb, mr.maxi, mr.maxrb))
        mr.calMaxSize()
        self.assertEqual(mr.getMaxSize(), mr.maxsize)
        self.assertEqual(mr.getMaxBoundary(), (mr.maxlb, mr.maxi, mr.maxrb))


class UnitTest_Stack(unittest.TestCase):
    def test_init(self):
        s=Stack()
        self.assertEqual(s.stack_lsit, [])
        self.assertEqual(s.top, -1)
        self.assertEqual(s.size, 0)

        s=Stack([1])
        self.assertEqual(s.stack_lsit, [1])
        self.assertEqual(s.top, 1)
        self.assertEqual(s.size, 1)

    def test_push(self):
        s=Stack([1,6,2])
        s.push(7)
        self.assertEqual(s.stack_lsit, [1,6,2,7])
        self.assertEqual(s.top, 7)
        self.assertEqual(s.size, 4)

    def test_pop(self):
        s=Stack([1,6])
        s.pop()
        self.assertEqual(s.stack_lsit, [1])
        self.assertEqual(s.top, 1)
        self.assertEqual(s.size, 1)
        s.pop()
        self.assertEqual(s.stack_lsit, [])
        self.assertEqual(s.top, -1)
        self.assertEqual(s.size, 0)
        with self.assertRaises(Exception):
            s.pop()

if __name__=='__main__':
    unittest.main()
