"""
A subarray is a contiguous/continuous block
of elements in an array.
Given an array, find the sum of all elements 
in every subarray. 

E.g. [4,5,6]
    subarrays are
    [4], [5], [6]
    [4,5],  [5,6]
    [4,5,6]
    Note: [4,6] is NOT a subarray.

    subarraySum = (4+5+6) + (4+5+5+6) + (4+5+6)
"""

from typing import List

def subarray_sum(arr: List) -> int:
    """
    Use an example and observe for a pattern.
    Consider arr=[1,2,3], n=3. 

    subarrays= [1], [2], [3], [1,2], [2,3], [1,2,3]
    freq(index_0) = 3
    freq(1) = 4
    freq(2) = 3

    Every element arr[i] appears in 2 types of subsets:
    (1) Subarray begins with arr[i]
        Then the max length of this subarray = n-i
        => n-i of such arrays
    (2) Subarray does not begin with arr[i]
        Then subarray must begin with (I) j < i
        && (II) length > i-j
        (I)  There are i elements before arr[i]
        (II) For each subarray including arr[i],
             it may contain n-i-1 more elements
             after arr[i] => n-i
        => (n-i)*i
    => total freq = n-i + (n-i)*(i)
                  = (n-i)(i+1)

    sum = sum(freq(i) * arr[i] for i in range(n))
    """

    result= 0
    n= len(arr)
    for i in range(n):
        result+= (n-i) * (i+1) * arr[i]

    return result
    
