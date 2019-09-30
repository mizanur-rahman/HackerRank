#Task
'''Given a string ,S, of length N  that is indexed from 0 to N-1 , print its even-indexed and odd-indexed characters as 2 space-separated strings on a single line (see the Sample below for more detail).

Note: 0 is considered to be an even index.'''
#Solution: 
import math
import os
import random
import re
import sys


T=int(input())
for N in range(T):
    S = input()
    print(S[::2], S[1::2])
