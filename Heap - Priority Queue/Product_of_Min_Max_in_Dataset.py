#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maxMin' function below.
#
# The function is expected to return a LONG_INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY operations
#  2. INTEGER_ARRAY x
#

def maxMin(operations, x):
    # Write your code here
    """
    Make a max heap and a min heap.
    Return the product of both roots.
    """
    maxim= []
    minim= []
    max_min= []

    for index in range(len(x)):
        if operations[index]== 'push':
            insert_max_heap(maxim, x[index])
            insert_min_heap(minim, x[index])

        if operations[index]== 'pop':
            cur_max= maxim.index(x[index])
            remove_max_heap(maxim, cur_max)
            cur_min= minim.index(x[index])
            remove_min_heap(minim, cur_min)

        max_min.append(maxim[0]*minim[0])

    return max_min

def fix_max_heap(heap, index):
    """
    Fix max binary heap (tree) from index.
    If index==0, equivalent to fixing the
    entire heap.
    """
    # no child nodes
    if 2*index+1 >= len(heap):
        return
        
    # only 1 child node
    if 2*index+2 >= len(heap):
        if heap[index]<heap[2*index+1]:
            heap[index], heap[2*index+1]= heap[2*index+1], heap[index]
        return

    # 2 child nodes
    if heap[index]<heap[2*index+1] or heap[index]<heap[2*index+2]:
        larger= 2*index+1 if heap[2*index+1]>heap[2*index+2] else 2*index+2
        heap[index], heap[larger]= heap[larger], heap[index]
        return fix_max_heap(heap, larger)

def fix_min_heap(heap, index):
    """
    Fix min binary heap (tree) from index.
    If index==0, equivalent to fixing the
    entire heap.
    """
    # no child nodes
    if 2*index+1 >= len(heap):
        return

    # only 1 child node
    if 2*index+2 >= len(heap):
        if heap[index]>heap[2*index+1]:
            heap[index], heap[2*index+1]= heap[2*index+1], heap[index]
        return

    # 2 child nodes
    if heap[index]>heap[2*index+1] or heap[index]>heap[2*index+2]:
        smaller= 2*index+1 if heap[2*index+1]<heap[2*index+2] else 2*index+2
        heap[index], heap[smaller]= heap[smaller], heap[index]
        return fix_min_heap(heap, smaller)

def insert_max_heap(heap, element):
    """
    Insert element into max heap
    """
    heap.insert(0, element)
    fix_max_heap(heap, 0)

def insert_min_heap(heap, element):
    """
    Insert element into min heap
    """
    heap.insert(0, element)
    fix_min_heap(heap, 0)

def remove_max_heap(heap, index):
    """
    Remove from max heap at index
    """
    heap[index]=heap[-1]
    heap.pop()
    fix_max_heap(heap, index)

def remove_min_heap(heap, index):
    """
    Remove from min heap at index
    """
    heap[index]=heap[-1]
    heap.pop()
    fix_min_heap(heap, index)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    operations_count = int(input().strip())

    operations = []

    for _ in range(operations_count):
        operations_item = input()
        operations.append(operations_item)

    x_count = int(input().strip())

    x = []

    for _ in range(x_count):
        x_item = int(input().strip())
        x.append(x_item)

    result = maxMin(operations, x)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
