#########################################################################
# File Name: choosesorter.py
# Purpose:
#       This program is to implement choose sort method
# History:
#	Created Time: 2016-10-12
# Author: Don E-mail: dpdeng@whu.edu.cn
#########################################################################

import sorter

class ChooseSorter(sorter.Sorter):
    def sort(self):
        for i in range(0,len(self.array)-1):
            key=i
            for j in range(i+1,len(self.array)):
                if self.array[key]>self.array[j]:
                    key=j
            self.array[i],self.array[key]=self.array[key],self.array[i]
        return self.array

if __name__=='__main__':
    pass
