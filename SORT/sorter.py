#########################################################################
# File Name: sort.py
# Purpose:
#    This program is to implement Sort algo with class
# History:
#    Created Time: Tue 06 Sep 2016 10:33:12 PM CST
#    Author: Don    E-mail: dpdeng@whu.edu.cn
#########################################################################
import argparse

def get_args():
    parser=argparse.ArgumentParser(description="this program is to sort integer arrays")
    parser.add_argument("-a", "--array", help="the array to sort", type=int, nargs='+',default=[1,3,2,4])
    return parser.parse_args()

class Sorter():
    def sort(self):
        pass
    def __init__(self, array):
        self.array=array

class InsertSorter(Sorter):
    def sort(self):
        for i in range(1,len(self.array)):
            key=self.array[i]
            j=i-1
            while j>=0 and key<self.array[j]:
                self.array[j+1]=self.array[j]
                j=j-1
            self.array[j+1]=key
        return self.array

class HeapSorter(Sorter):
    def sort(self):
        pass #wait to implement
    def heap_minimum(self):
        return self.array[0]
    def heap_extract_min(self):
        pass
    def heap_decrease_key(self):
        pass
    def min_heap_insert(self):
        pass

def main():
    args=get_args()
    array=args.array
    sorter=InsertSorter(array)

    print("before sort: ")
    print(array)
    print("after sort: ")
    print(sorter.sort())

if __name__=='__main__':
    main()
