from sys import maxsize
from warnings import warn
from imp import find_module
from math import floor

try:
    find_module('graphviz')
    from graphviz import Graph

    GRAPHVIZ_AVAILABLE = True
except ImportError as exception:
    GRAPHVIZ_AVAILABLE = False
    warn('Graphviz is not available')

__author__ = "Minasie Alemu"
__credits__ = ["Minasie Alemu"]
__version__ = "1.0.1"
__maintainer__ = "Minasie Alemu"
__email__ = "minalem.5d@gmail.com"


class Heap(object):
    """A (binary) heap data structure is an array object which can be viewed
    as an almost complete binary tree"""

    def __init__(self, max_size=maxsize, input_array=[]):
        self.__array = input_array
        self.__max_size = max_size
        if (input_array):
            self.__build(input_array)
            self.__max_size = self.__size()

    # Private Methods Section #
    def __build(self, input_array):
        start = int(floor(len(input_array) / 2)) - 1
        for i in range(start, -1, -1):
            self.__heapify(i)

    def __parent(self, i):
        return int(floor((i - 1) / 2))

    def __left(self, i):
        return 2 * i + 1

    def __right(self, i):
        return 2 * i + 2

    def __heapify(self, i):
        l = self.__left(i)
        r = self.__right(i)
        size = self.__size()
        if (l < size) and (self.__array[l] < self.__array[i]):
            smallest = l
        else:
            smallest = i
        if (r < size) and (self.__array[r] < self.__array[smallest]):
            smallest = r
        if (smallest != i):
            self.__array[i], self.__array[smallest] = self.__array[smallest], self.__array[i]
            self.__heapify(smallest)

    def __size(self):
        return len(self.__array)

    def __str__(self):
        return str(self.__array)

    # Public Methods Section #
    def get_size(self):
        """Get the current size of the heap, i.e. number of elements stored"""
        return self.__size()

    def get_head(self):
        """Get the head of the Heap without removing it. Given that it is a
        min-heap this corresponds to the minimum stored value"""
        return self.__array[0]

    def pop_head(self):
        """Get the head of the Heap but removing it. This triggers a
        re-organization in order to set the new head of the data structure"""
        size = self.__size()
        if (size == 0):
            warn('Empty Heap!')
        self.__array[0], self.__array[-1] = self.__array[-1], self.__array[0]
        head = self.__array.pop()
        size -= 1
        if (size > 0):
            self.__heapify(0)
        return head

    def update_key(self, i, key):
        """Update a key given its position in the Heap. This may cause a
        re-organization"""
        if key > self.__array[i]:
            # Key might 'float down' #
            self.__array[i] = key
            self.__heapify(i)
        else:
            self.__array[i] = key
            parent = self.__parent(i)
            while (i > 0) and (self.__array[parent] > self.__array[i]):
                self.__array[i], self.__array[parent] = self.__array[parent], self.__array[i]
                i = parent
                parent = self.__parent(i)

    def insert(self, key):
        """Insert a new key into the Heap. The behaviour of this method is slightly
        different from the traditional one. In fact, when the heap is already
        full the new value should be bigger than the lowest one stored in order
        to be succesfully inserted. This particularly useful when the heap is
        used to stored a ranking"""
        size = self.__size()
        if size == self.__max_size:
            if key > self.__array[0]:
                i = 0
                self.update_key(i, key)
            else:
                warn('The key is lower than the smallest value in the heap')
        else:
            i = size
            self.__array.append(key)
            self.update_key(i, key)

    def heapsort(self):
        """Sort the Heap. Attention this operation is destructive. After its
        conclusion the heap will no longer exist"""
        sorted_array = []
        size = self.__size()
        for key in range(0, size):
            sorted_array.append(self.pop_head())
        return sorted_array

    def export_tree(self, comment='', filename='binary_heap'):
        """Print a pretty representation of the Heap as binary tree in pdf format"""
        if GRAPHVIZ_AVAILABLE:
            size = self.__size()
            dot = Graph(comment=comment)
            for i, vertex in enumerate(self.__array):
                dot.node(str(i), label=str(vertex))
                l = self.__left(i)
                r = self.__right(i)
                if l < size:
                    dot.edge(str(i), str(l))
                if r < size:
                    dot.edge(str(i), str(r))
            dot.graph_attr['rankdir'] = 'TB'
            dot.render(filename)


def main():
    # Build a Heap from an input array #
    h = Heap(input_array=[4,1,3,2,16,9,10,14,8,7])
    # Print it #
    print('Heap: ' + str(h))
    # Save it as tree (pdf) #
    h.export_tree()
    # Update a Key and see the result #
    print ('Update Key at position i=1 (value=17)')
    h.update_key(1, 17)
    print ('Heap: ' + str(h))
    # Pop the head of the head and see the result #
    print ('Por the head: ' + str(h.pop_head()))
    # Get the value of its new head  #
    print ("New head: " + str(h.get_head()))
    print ('Heap: ' + str(h))
    # Insert an element and see the result #
    print ('Insert key=6')
    h.insert(6)
    print ('Heap: ' + str(h))
    # Sort the heap #
    print ("Heapsort: " + str(h.heapsort()))
    return 0

if __name__ == '__main__':
    main()