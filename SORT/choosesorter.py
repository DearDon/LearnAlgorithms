#########################################################################
# File Name: choosesort.py
# Purpose:
#    This program is to implement choose sort method
# History:
#    Created Time: Wed 24 Aug 2016 10:59:39 PM CST
#    Author: Don    E-mail: dpdeng@whu.edu.cn
#########################################################################

import argparse as arg
from sorter import Sorter
import unittest

class ChooseSorter(Sorter):
    def sort(self):
        for i in range(0,len(self.array)-1):
            key=i
            for j in range(i+1,len(self.array)):
                if self.array[key]>self.array[j]:
                    key=j
            self.array[i],self.array[key]=self.array[key],self.array[i]
        return self.array

def get_args():
    parser = arg.ArgumentParser(description='sort a given array')
    parser.add_argument("-a", type=int, nargs='+', help="the array to be sorted, eg. -a 1 4 2 3")
    return parser.parse_args()

if __name__ == "__main__":
    args = get_args()

    if args.a:
        if False:
            array=args.a.split(',')
            for i in range(len(array)):
                array[i]=int(array[i])
        array = args.a
    else:
        array=[1,3,2,4]

    sorter=ChooseSorter(array)

    print(sorter.sort())
