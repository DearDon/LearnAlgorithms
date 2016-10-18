#########################################################################
# File Name: heapsorter.py
# Purpose:
#	This file is to implement heap sort method
# History:
#	Created Time: 2016-10-12
# Author: Don E-mail: dpdeng@whu.edu.cn
#########################################################################
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
        if self.heap_size <= i or i<0:
            raise Exception(str(i)+" is beyond heap range")
        elif self.array[i] < key:
            raise Exception(str(key)+" is already larger than array[i] "+str(self.array[i]))
        self.array[i]=key
        while self.array[i]<self.array[self.parentIndex(i)]:
            self.array[i], self.array[self.parentIndex(i)]=self.array[self.parentIndex(i)], self.array[i]
            i=self.parentIndex(i)

    def minHeapInsert(self, key):#Done
        if self.heap_size == len(self.array):
            raise Exception("can't insert, array is full")
        self.heap_size += 1
        self.array[self.heap_size-1]=float("inf")
        self.heapDecreaseKey(self.heap_size-1,key)

    def parentIndex(self,i):#Done
        if self.heap_size <= i or i<0:
            raise Exception("element with index "+str(i)+" are out of heap range")

        if i==0:
            return 0
        else:
            return (i-1)/2

    def childrenIndex(self,i):#Done
        if self.heap_size <= i or i<0:
            raise Exception("element with index "+str(i)+" are out of heap range")

        left_child=i*2+1
        if left_child >= self.heap_size:
            return i, i
        elif left_child+1 >= self.heap_size:
            return left_child, i
        else:
            right_child=left_child+1
            return left_child, right_child

if __name__ == '__main__':
    x,y=(1,2)
    x,y=y,x
    print x,y
    print 1/2
