"""
An ideal number is a positive number with
only 3 and 5 as prime factors. It can be
expressed in the form of (3^x + 5^y) where
x and y are non-negative integers.
E.g. 15, 45, 75 are ideal
E.g. 6, 10, 21 are not ideal

Find the number of ideal integers within
a given range, [low, high].
E.g. get_ideal_nums(3,5) -> 2
"""

from typing import List

def get_ideal_nums(low: int, high: int) -> int:
    """
    Consider the knapsack problem:
    The knapsack must have min weight low and
    max weight high. There are only 2 different
    items that can be added, 3 and 5. The number
    of times each item is added corresponds to
    its power.

    This is now a 2D DP problem. The number of
    valid pairs (x,y) is the number of ideal
    integers.
    """
    size= max(get_iterations(high), 2)
    table= [ [0 for i in range(size)] for i in range(size)]
    table[0][0]=1
    table[1][0]=3
    table[0][1]=5

    table_update(size-1, size-1, [table])

    count=0
    for i in range(size):
        count+= sum(low <= x <= high for x in table[i])

    return count

def table_update(three: int, five: int, pointer: List):
    """
    Helper function for DP on get_ideal_nums
    """
    table= pointer[0]
    if three<0 or five<0:
        return
    if table[three][five]==0:
        table[three][five]= 3**three * 5**five
        table_update(three-1, five, pointer)
        table_update(three, five-1, pointer)

def get_iterations(num: int) -> int:
    """
    Find min(x) such that 3^x >= num
    """
    exp = 0
    while num>0:
        exp+=1
        num//=3

    return exp
