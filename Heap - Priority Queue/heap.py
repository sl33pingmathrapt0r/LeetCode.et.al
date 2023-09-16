"""
Module containig Heap class.
Instantiate to use methods.
"""

from typing import List, Callable
from inspect import getfullargspec as arg

class Heap:
    """
    Heap Class for priority queues.
    """

    def __init__(self, comparator: Callable= lambda first, second: first>second):
        """
        Initialise an empty heap with
        optional comparator function.
        Default max heap.
        """
        assert hasattr(comparator, '__call__'), "provide a function"
        assert len(arg(comparator).args)==2, "function must take 2 arguments"
        self.comparator= comparator
        self.__heap= []

    def __repr__(self) -> str:
        """
        Representation method.
        """
        return  "Heap object at id: " + str(id(self))

    def __str__(self) -> str:
        """
        Pretty printing...
        But I'm too lazy to fix this shyt,
        printing a regular list instead.
        """
        return self.__heap.__str__()

    def __len__(self) -> int:
        """
        Return length of heap (list).
        """
        return self.__heap.__len__()

    def __getitem__(self, index):
        """
        Return item at given index.
        """
        return self.__heap.__getitem__(index)

    def __setitem__(self,index, value):
        """
        Mutate item at given index to new value.
        """
        return self.__heap.__setitem__(index, value)

    def heapify(self, elements: List):
        """
        Assign the heap with a given
        list of elements.
        """
        assert isinstance(elements, list), "provide a list"
        self.__heap= elements
        length= len(self)
        last_parent= length//2 -1
        for parent_node in range(last_parent, -1, -1):
            self.fix_heap(parent_node)

    def get_heap(self) -> List:
        """
        Return heap (list).
        """
        return self.__heap

    def root(self):
        """
        Return element at root of tree.
        """
        return self[0]

    def index(self, element) -> int:
        """
        Find index of element.
        """
        assert element in self.__heap, "element not in heap"
        return self.__heap.index(element)

    def fix_heap(self, index: int):
        """
        Fix binary heap (tree) from given index,
        after a single mutation (insert/remove).
        If index==0, equivalent to fixing the
        entire heap.
        """
        assert isinstance(index, int), "index must be an integer"

        # no child nodes
        if 2*index+1 >= len(self.__heap):
            pass

        # only 1 child node
        elif 2*index+2 >= len(self.__heap):
            if self.comparator(self[2*index+1], self[index]):
                self[index], self[2*index+1]= \
                    self[2*index+1], self[index]

        # 2 child nodes
        elif self.comparator(self[2*index+1], self[index]) or \
            self.comparator(self[2*index+2], self[index]):

            larger= 2*index+1 \
                if self.comparator(self[2*index+1], self[2*index+2]) \
                else 2*index+2
            self[index], self[larger]= self[larger], self[index]
            return self.fix_heap(larger)

    def insert(self, element):
        """
        Insert element into heap.
        """
        self.__heap.insert(0, element)
        self.fix_heap(0)

    def pop(self, index: int):
        """
        Remove from heap at index.
        """
        assert isinstance(index, int), "index must be an integer"
        self[index]= self[-1]
        self.__heap.pop()
        self.fix_heap(index)

    def remove(self, element):
        """
        Remove element from heap.
        """
        index= self.index(element)
        self.pop(index)
