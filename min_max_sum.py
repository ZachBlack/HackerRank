#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Bubble sort array, increasing order
    # print the sum of index 0-3 and 1-4
    
    for i in range(4, 0, -1):
        for index in range(i):
            if arr[index] > arr[index+1]:
                arr[index+1], arr[index] = arr[index], arr[index+1]
    
    print("{} {}".format(sum(arr[0:4]), sum(arr[1:])))
    
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
