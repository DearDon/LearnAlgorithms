#########################################################################
# File Name: choosesorter.py
# Purpose:
#       This program is to implement choose sort method
# History:
#	Created Time: 2016-10-12
# Author: Don E-mail: dpdeng@whu.edu.cn
#########################################################################

from sorter import Sorter

import choosesorter_unittest
import run_unittest

class ChooseSorter(Sorter):
    def sort(self):
        for i in range(0,len(self.array)-1):
            key=i
            for j in range(i+1,len(self.array)):
                if self.array[key]>self.array[j]:
                    key=j
            self.array[i],self.array[key]=self.array[key],self.array[i]
        return self.array

if __name__ == "__main__":
    #unittest
    test_suite=choosesorter_unittest.fullSuite()
    test_result=run_unittest.runTestSuite(test_suite)
    run_unittest.showResult(test_result)
