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
    def __init__(self, array):#Done
        super(HeapSorter, self).__init__(array)
        self.heap_size=0

    def sort(self):#need to reverse sort
        self.minHeapBuild()
        while self.heap_size>0:
            self.heapExtractMin()
        return self.array

    def minHeapBuild(self):#Done
        self.heap_size=1
        for i in range(1,len(self.array)):
            self.minHeapInsert(self.array[i])

    def heapMinimum(self):#Done
        return self.array[0]

    def heapExtractMin(self):#Done
        if self.heap_size<=0:
            raise Exception("no element in heap with size {}".format(str(i)))

        self.heap_size-=1
        if self.heap_size>0:
            key=self.array[self.heap_size]
            self.array[self.heap_size]=self.array[0]
            self.heapIncreaseKey(0,key)
        return self.array[0:self.heap_size]

    def heapIncreaseKey(self, i, key):#Done
        if self.heap_size <= i or i<0:
            raise Exception(str(i)+" is beyond heap range")
        elif self.array[i] > key:
            raise Exception(str(key)+" is smaller than array[i] "+str(self.array[i]))
        self.array[i]=key
        while self.array[i]>self.array[self.minChildrenIndex(i)]:
            self.array[i], self.array[self.minChildrenIndex(i)]=self.array[self.minChildrenIndex(i)], self.array[i]
            i=self.minChildrenIndex(i)

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

    def minChildrenIndex(self,i):#Done
        if self.heap_size <= i or i<0:
            raise Exception("element with index "+str(i)+" are out of heap range")

        left_child=i*2+1
        right_child=left_child+1

        if left_child >= self.heap_size: #no child
            return i
        elif right_child >= self.heap_size: #only left child
            return left_child
        else: # got two children
            if self.array[left_child] <= self.array[right_child]:
                return left_child
            else:
                return right_child

if __name__ == '__main__':
    x,y,z=(1,2,3)
    x,y,z=z,y,x
    print x,y,z
