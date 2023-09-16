"""
test heap class with maxMin function
"""

from heap import Heap

def maxMin(operations, x):
    # Write your code here
    """
    Make a max heap and a min heap.
    Return the product of both roots.
    """
    maxim= Heap()
    minim= Heap(lambda small,big: small<big)
    max_min= []

    for index, elem in enumerate(x):
        if operations[index]== 'push':
            maxim.insert(elem)
            minim.insert(elem)

        if operations[index]== 'pop':
            maxim.remove(elem)
            minim.remove(elem)

        max_min.append(maxim.root()*minim.root())

    return max_min

maxMin(['push']*3+['pop'], [1,2,3,1])    # -> [1,2,3,6]
