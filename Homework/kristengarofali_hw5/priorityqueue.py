from __future__ import print_function
import sys
import numpy as np

class PriorityQueue:

    def __init__(self, N=0,MAX=100, a=[0]):
        self.N = N
        self.MAX = MAX
        self.a = a

    def insert(self, i):

        if self.N >= self.MAX:
            print("Size greater than array max")
            sys.exit("Error: len(a) must be MAX+1")

        self.a.append(i)
        self.N +=1
        k = self.N

        while ((k>1) & (self.a[k/2] > self.a[k])):
            temp = self.a[k/2]
            self.a[k/2] = self.a[k]
            self.a[k] = temp
            k = k/2

    def delMin(self):
        if self.N == 0:
            print("Empty priority queue")
            sys.exit("Error: Empty priority queue")

        minimum = self.a[1]
        self.a[1] = self.a[self.N]
        self.a[self.N] = 0
        self.N -= 1
        k = 1
        while 2*k <= self.N:
            if ((2*k == self.N) | (self.a[2*k] < self.a[2*k + 1])):
                j = 2*k
            else:
                j = 2*k + 1
            if (self.a[k] > self.a[j]):
                temp = self.a[k]
                self.a[k] = self.a[j]
                self.a[j] = temp
                k = j
            else:
                break

        return minimum

    def min(self):
        if self.N == 0:
            print("Empty priority queue")
            sys.exit("Error: Empty priority queue")

        m = self.a[1]
        return m

    def size(self):
        return self.N

    def isEmpty(self):
        if self.N == 0:
            return True
        else:
            return False

    def isFull(self):
        if self.N == self.MAX:
            return True
        else:
            return False
