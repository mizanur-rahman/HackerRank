#!/bin/python3

import math
import os
import random
import re
import sys
def get_max(mat, row,col):
    s=0
    s+=mat[row-1][col-1]
    s+=mat[row-1][col]
    s+=mat[row-1][col+1]
    s+=mat[row][col]
    s+=mat[row+1][col-1]
    s+=mat[row+1][col]
    s+=mat[row+1][col+1]
    return s





if __name__ == '__main__':
    arr = []

    for _ in range(6):
        array_t=(list(map(int, input().rstrip().split())))
        arr.append(array_t)
    max=-63 
    #maximum -9 times 6 is -63
    for i in range(1,5):
        for j in range(1,5):
            sum=get_max(arr, i ,j)
            if max<sum:
                max=sum
    print(max)
