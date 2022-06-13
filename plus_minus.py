#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # get the length of array from arr[0]
    # loop through array at arr[1]
    # if number == 0, add to zero var
    # elif number == -1 add to neg var
    # elif number == 1 add to pos var
    # print pos/length to 6 decimal places
    # print neg/length to 6 decimal places
    # print zerp/length to 6 decimal places
    
    length = len(arr)
    
    pos, neg, zero = 0, 0, 0
    
    for i in range(length):
        if arr[i] == 0:
            zero+=1
        elif arr[i] < 0:
            neg+=1
        else:
            pos+=1
    
    print("{:.6f}".format(pos/length))
    print("{:.6f}".format(neg/length))
    print("{:.6f}".format(zero/length))
    
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
