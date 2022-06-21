#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lonelyinteger' function below.
#
# PROMPT:  Given an array of integers, where all elements but one occur twice, find the unique element.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a):
    # Write your code here
    length = len(a)
    
    if length == 1:
        return a.pop()
    
    while length > 2:
        item = a.pop()
        if item in a:
            a.pop(a.index(item))
        else:
            return item   

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()
