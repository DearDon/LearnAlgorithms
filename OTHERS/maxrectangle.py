#########################################################################
# File Name: maxrectangle.py
# Purpose:
#	This file is to implement the algorithms that get the max size rectangle from histogram
# History:
#	Created Time: 2016-10-22
# Author: Don E-mail: dpdeng@whu.edu.cn
#########################################################################

class MaxRectangle(object):
    def __init__(self, height_array):
        self.height_array=height_array
        self.left_boundary = [-1]*len(self.height_array)
        self.right_boundary = [len(self.height_array)]*len(self.height_array)
        self.index_stack=Stack([0])
        self.maxsize=0
        self.maxlb=-1
        self.maxi=0
        self.maxrb=len(self.height_array)

    def calMaxSize(self):
        if len(self.height_array)==0:
            raise Exception("input height_array can't be []")
        for i in range(1, len(self.height_array)):
            if self.height_array[i] > self.height_array[self.index_stack.top]:
                self.left_boundary[i]=self.index_stack.top
                self.index_stack.push(i)
            else:
                while self.index_stack.size>0 and self.height_array[i]<self.height_array[self.index_stack.top]:
                    self.right_boundary[self.index_stack.top]=i
                    self.index_stack.pop()

                if self.index_stack.size==0:
                    self.index_stack.push(i)
                    continue

                if self.height_array[i]==self.height_array[self.index_stack.top]:
                    self.left_boundary[i]=self.left_boundary[self.index_stack.top]
                else:
                    self.left_boundary[i]=self.index_stack.top
                self.index_stack.push(i)

        for i in range(0, len(self.height_array)):
            size=(self.right_boundary[i]-self.left_boundary[i]-1)*self.height_array[i]
            if size>self.maxsize:
                self.maxsize=size
                self.maxlb=self.left_boundary[i]
                self.maxrb=self.right_boundary[i]
                self.maxi=i
        return 'SUCCESS'

    def getMaxSize(self):
        return self.maxsize

    def getMaxBoundary(self):
        return self.maxlb, self.maxi, self.maxrb

class Stack(object):
    def __init__(self, input_list=[]):
        self.stack_lsit=input_list
        self.size=len(self.stack_lsit)
        if self.size==0:
            self.top=-1
        else:
            self.top=self.stack_lsit[self.size-1]


    def push(self, key):
        self.stack_lsit.append(key)
        self.size+=1
        self.top=key

    def pop(self):
        if self.size==0:
            raise Exception("no element to pop")
        self.size-=1
        if self.size==0:
            self.top=-1
        else:
            self.top=self.stack_lsit[self.size-1]
        self.stack_lsit.pop()

if __name__ == '__main__':
    #mr=MaxRectangle([1,6,5,4])
    #mr=MaxRectangle([])
    mr=MaxRectangle([3,1,2])
    mr.calMaxSize()
    print mr.getMaxSize()
    print mr.getMaxBoundary()
