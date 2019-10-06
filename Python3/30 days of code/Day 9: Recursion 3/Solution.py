#!/bin/python3
#Task
'''Write a factorial function that takes a positive integer,N  as a parameter and prints the result of N ( factorial).

Note: If you fail to use recursion or fail to name your recursive function factorial or Factorial, you will get a score of 0.

Input Format

A single integer, N (the argument to pass to factorial).

Constraints: 2<=N<=12

Your submission must contain a recursive function named factorial.
Output Format

Print a single integer denoting N .

Sample Input

3
Sample Output

6'''
import math
import os
import random
import re
import sys

# Complete the factorial function below.
def factorial(n):
    if n <= 1:
        return (1)
    else:
        result = n * factorial(n - 1)
        return result

if __name__ == '__main__':

    n = int(input())

    result = factorial(n)
    print(result)

