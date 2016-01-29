from __future__ import print_function
import sys

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class Stack:

    def __init__(self, head=None, N=0):
        self.head = head
        self.N = N

    def push(self, i):
        n = Node(i,self.head)
        self.head = n
        self.N += 1


    def pop(self):
        if self.head is None:
            print("Head node empty")
            sys.exit("Error: Head node empty")
        else:
            i = self.head.data
            self.head = self.head.next
            self.N -= 1
            return i

    def top(self):
        i = self.head.data
        return i

    def size(self):
        return self.N

    def isEmpty(self):
        if self.head is None:
            return True
        else:
            return False

def traverse_stack(node):
    list = []
    while node.next is not None:
        list.append(node.data)
        node = node.next
    else:
        list.append(node.data)
    print(list)
