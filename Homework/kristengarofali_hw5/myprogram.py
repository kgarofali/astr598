import priorityqueue
from priorityqueue import PriorityQueue
import numpy as np

pq = PriorityQueue(0,20)
ints = np.random.randint(1,100, size=20)
print("Inserting 20 integers into pq: {0}".format(ints))
[pq.insert(i) for i in ints]
print("pq is full: {0}".format(pq.isFull()))
print("pq size: {0}".format(pq.size()))
print("Deleting 20 integers from pq: {0}".format([pq.delMin() for i in range(20)], sep=','))
print("pq is empty: {0}".format(pq.isEmpty()))
print("pq size: {0}".format(pq.size()))
