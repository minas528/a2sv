#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'minimumDivisor' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arr
#  2. INTEGER threshold
#

def minimumDivisor(arr, threshold):
    # Write your code here
    summation = sum(arr)
    if summation < threshold:
        return 1
    divisior = 1
    while summation//divisior > threshold:

        divisior += 1
    return divisior


if __name__ == '__main__':
    arr = [32, 305709952, 617901827, 559066417, 846642314, 349430261, 930100012, 425149509, 50710994, 348655290,
           207497545, 663923396, 873283308, 243509537, 657804153, 547001100, 203492670, 344685642, 808597188, 129005353,
           142684482, 387013286, 58302119, 216770904, 793436542, 234999067, 471073451, 42602919, 10272918, 326437084,
           774854236, 544470926, 507360048]
    threshold = 612271938
    result = minimumDivisor(arr, threshold)
    print(result)
