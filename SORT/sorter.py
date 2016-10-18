#########################################################################
# File Name: sorter.py
# Purpose:
#       This program is to implement Sort algo with class
# History:
#	Created Time: 2016-10-12
# Author: Don E-mail: dpdeng@whu.edu.cn
#########################################################################
import timeit

class Sorter(object):
    def __init__(self, array):
        self.array=array

    def sort(self):
        raise NotImplementedError

    def getSortTime(self):
        starttime = timeit.default_timer()
        self.sort()
        stoptime = timeit.default_timer()
        return stoptime-starttime

