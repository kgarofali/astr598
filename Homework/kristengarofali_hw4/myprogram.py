from __future__ import print_function
import queue
from queue import Queue
from queue import traverse_queue
import numpy as np

new_queue = Queue()

print("Inserting ten random integers in queue")
[new_queue.put(i) for i in np.random.randint(1,10, size=10)]
#traverse_queue(new_queue.head)
print("Queue is empty: {0}".format(new_queue.isEmpty()))
print("Getting ten integers from queue: {0}".format([new_queue.get() for i in range(10)], sep=','))
print("Queue is empty: {0}".format(new_queue.isEmpty()))
