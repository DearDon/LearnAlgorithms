#########################################################################
# File Name: insertion_sort.py
# Purpose:
#    This program is to impliment insertion sort method
# History:
#    Created Time: Tue 23 Aug 2016 09:28:56 PM CST
#    Author: Don    E-mail: dpdeng@whu.edu.cn
#########################################################################

import Argparse as Arg

def sort(A):
    for i in range(1,len(A)):
        key=A[i]
        j=i-1
        while j>=0 and key<A[j]:
            A[j+1]=A[j]
            j=j-1
        A[j+1]=key
    return A


if __name__ == "__main__":
    Arg.set_arg("-a","the array to sort, divided by ',', eg -a 1,3,2,4 ")
    args = Arg.get_args()

    if args.a:
        array=args.a.split(',')
        for i in range(len(array)):
            array[i]=int(array[i])
    else:
        array=[1,3,2,4]

    print(sort(array))
