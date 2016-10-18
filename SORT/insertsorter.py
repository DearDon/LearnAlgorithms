#########################################################################
# File Name: insertsorter.py
# Purpose:
#	This file is to implement insert sort algo
# History:
#	Created Time: 2016-10-11
# Author: Don E-mail: dpdeng@whu.edu.cn
#########################################################################

import sorter


class InsertSorter(sorter.Sorter):
    def sort(self):
        for i in range(1,len(self.array)):
            key=self.array[i]
            j=i-1
            while j>=0 and key<self.array[j]:
                self.array[j+1]=self.array[j]
                j=j-1
            self.array[j+1]=key
        return self.array

if __name__=='__main__':
    pass
