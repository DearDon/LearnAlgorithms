#########################################################################
# File Name: run.py
# Purpose:
#	This file is to start sortting a array from user
# History:
#	Created Time: 2016-10-11
# Author: Don E-mail: dpdeng@whu.edu.cn
#########################################################################
import argparse
from choosesorter import ChooseSorter

def get_args():
    parser=argparse.ArgumentParser(description="this program is to sort integer arrays")
    parser.add_argument("-a", "--array", help="the array to sort. eg. -a 1 4 2 3", type=int, nargs='+',default=[1,3,2,4])
    return parser.parse_args()

def main():
    args=get_args()
    array=args.array
    sorter=ChooseSorter(array)

    print("before sort: ")
    print(array)
    print("after sort: ")
    print(sorter.sort())

if __name__=='__main__':
    main()
