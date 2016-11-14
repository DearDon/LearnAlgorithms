#########################################################################
# File Name: quicksorter.py
# Purpose:
#	This file is to implement quick sort
# History:
#	Created Time: 2016-11-14
# Author: Don E-mail: dpdeng@whu.edu.cn
#########################################################################
import sorter

class QuickSorter(sorter.Sorter):
    def sort(self):
        self.quicksort(self.array, 0, len(self.array)-1)
        return self.array

    def quicksort(self, array, p, r):
        if p<r:
            q=self.partition(array, p, r)
            self.quicksort(array, p, q-1)
            self.quicksort(array, q+1, r)

    def partition(self, array, p, r):
        i=p
        for j in range(p, r):
            if array[j] < array[r]:
                array[i], array[j] = array[j], array[i]
                i+=1

        array[r], array[i] = array[i], array[r]
        return i


if __name__=='__main__':
    pass
