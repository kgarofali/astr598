from __future__ import print_function
import numpy as np
import bst
from bst import BinarySearchTree

bst = BinarySearchTree()
rand_ints = np.random.randint(1,100,100).tolist()
print("Unsorted array: {0}".format(rand_ints))
print("Inserting 100 random integers into bst")
[bst.insert(i) for i in rand_ints]
print("bst is empty: {0}".format(bst.isEmpty()))
print("Traversing bst in order:")
bst.traverse_in_order()
print("bst minimum: {0}".format(bst.min()))
print("bst maximum: {0}".format(bst.max()))
