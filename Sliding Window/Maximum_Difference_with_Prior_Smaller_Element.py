#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'maxTrailing' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def maxTrailing(arr):
    # Write your code here
    """
    Given an array of integers, without
    reordering, determine the maximum
    difference between any element and
    any prior smaller element. If there
    is never a lower prior element,
    return -1. 
    
    (Implement sliding window algoritm)
    """
    if len(arr)==1:
        return -1

    if len(arr)==2:
        return arr[1]-arr[0] if arr[1]>arr[0] else -1
        
    cur=1
    prior=arr[0]
    diff=-1
    while cur<len(arr):
        if arr[cur]<prior:
            prior=arr[cur]
        elif arr[cur]>prior:
            diff= max(diff, arr[cur]-prior)
        cur+=1
        
    return diff


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = []

    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = maxTrailing(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
