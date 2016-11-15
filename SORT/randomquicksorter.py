#########################################################################
# File Name: randomquicksorter.py
# Purpose:
#	This file is to implement random quick sort method 
# History:
#	Created Time: 2016-11-15
# Author: Don E-mail: dpdeng@whu.edu.cn
#########################################################################
import random
from quicksorter import QuickSorter

class RandomQuickSorter(QuickSorter):
    def sort(self):
        self.randomquicksort(self.array, 0, len(self.array)-1)
        return self.array

    def randomquicksort(self, array, p, r):
        if p<r:
            i=random.randint(p, r)
            array[i], array[r] = array[r], array[i]
            q=self.partition(array, p, r)
            self.randomquicksort(array, p, q-1)
            self.randomquicksort(array, q+1, r)

if __name__=='__main__':
    rqs=RandomQuickSorter([1,6,5,3])
    print rqs.sort()
