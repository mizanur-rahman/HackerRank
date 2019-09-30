#Task
'''Given an array,A , of  integers,N print A's elements in reverse order as a single line of space-separated numbers.'''
#Solution:

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))
    print(*reversed(arr))
