#Task:
'''Given a base- 10 integer,n , convert it to binary (base-2). Then find and print the base-10 integer denoting the maximum number of consecutive 1's in n's binary representation.'''
#Solution:

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    b=bin(n)[2:].split('0')
    print(max(len(i) for i in b))
