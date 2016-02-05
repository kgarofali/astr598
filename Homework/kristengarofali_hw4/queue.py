from __future__ import print_function
import sys

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class Queue:
    def __init__(self, head=None, tail=None, N=0):
        self.head = head
        self.tail = tail
        self.N = N

    def put(self, i):
        n = Node(i,next=None)
        if self.head is None:
            self.head = n
            self.tail = n
        elif self.head == self.tail:
            self.head.next = n
            self.tail = n
        else:
            self.tail.next = n
            self.tail = n

        self.N += 1

    def get(self):
        if self.head is None:
            print("Head node empty")
            sys.exit("Error: Head node empty")
        else:
            i = self.head.data
            self.head = self.head.next
            self.N -= 1
            return i

    def front(self):
        if self.head is None:
            print("Head node empty")
            sys.exit("Error: Head node empty")
        else:
            i = self.head.data
            return i

    def size(self):
        return self.N

    def isEmpty(self):
        if self.N == 0:
            return True
        else:
            return False

def traverse_queue(node):
    list = []
    while node.next is not None:
        list.append(node.data)
        node = node.next
    else:
        list.append(node.data)
    print(list)
