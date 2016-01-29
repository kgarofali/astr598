from __future__ import print_function
import stack
from stack import Stack
from stack import traverse_stack
import numpy as np

new_stack = Stack()

print("Inserting ten random integers in stack")
[new_stack.push(i) for i in np.random.randint(1,10, size=10)]
print("Stack is empty: {0}".format(new_stack.isEmpty()))
print("Popping ten integers from stack: {0}".format([new_stack.pop() for i in range(10)], sep=','))
print("Stack is empty: {0}".format(new_stack.isEmpty()))
