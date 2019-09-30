import math
import os
import random
import re
import sys


T=int(input())
for N in range(T):
    S = input()
    print(S[::2], S[1::2])