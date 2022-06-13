#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # If first two chars are 12 and last two are 'AM'
        # set first two chars to '00'
        # remove last two chars
    # elif the second to last diget is 'P'
        # remove last two chars
        # convert first two chars to int
        # add 12
    # else
        #remove last two chars
        
    if s[0:2]=='12' and s[-2]=='A':
        return ('00'+s[2:8])
    
    elif s[-2]=='A' or s[0:2]=='12':
        return s[:8]
    
    else:
        return (str(int(s[0:2])+12)+s[2:8])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
