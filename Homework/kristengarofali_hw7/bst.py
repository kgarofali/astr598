import sys

class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class BinarySearchTree():
    def __init__(self, root=None, N=0):
        self.root = root
        self.N = 0

    def insert(self, i):
        n = Node(i, left=None, right=None)
        self.N += 1

        if self.root is None:
            self.root = n
        else:
            self._insert(self.root,n)

    def _insert(self, local_root, n):
        if local_root is None:
            print("Local root empty")
            sys.exit("Error: Local root empty")

        if n.data < local_root.data:
            if local_root.left is None:
                local_root.left = n
            else:
                self._insert(local_root.left, n)
        else:
            if local_root.right is None:
                local_root.right = n
            else:
                self._insert(local_root.right, n)

    def find(self, i):
        return self._find(self.root, i)

    def _find(self, local_root, i):
        if local_root is None:
            return False
        elif local_root.data == i:
            return True
        elif i < local_root.data:
            return self._find(local_root.left, i)
        elif i > local_root.data:
            return self._find(local_root.right, i)

    def traverse_pre_order(self):
        self._traverse_pre_order(self.root)

    def _traverse_pre_order(self, local_root):
        if local_root is None:
            return
        else:
            print(local_root.data)
            self._traverse_pre_order(local_root.left)
            self._traverse_pre_order(local_root.right)

    def traverse_in_order(self):
        self._traverse_in_order(self.root)

    def _traverse_in_order(self, local_root):
        if local_root is None:
            return
        else:
            self._traverse_in_order(local_root.left)
            print(local_root.data)
            self._traverse_in_order(local_root.right)

    def traverse_post_order(self):
        self._traverse_post_order(self.root)

    def _traverse_post_order(self, local_root):
        if local_root is None:
            return
        else:
            self._traverse_post_order(local_root.left)
            self._traverse_post_order(local_root.right)
            print(local_root.data)

    def min(self):
        if self.root is None:
            print("Root empty")
            sys.exit("Error: Root empty")
        local_root = self.root
        i = local_root.data
        while local_root is not None:
            i = local_root.data
            local_root = local_root.left
        return i

    def max(self):
        if self.root is None:
            print("Root empty")
            sys.exit("Error: Root empty")
        local_root = self.root
        i = local_root.data
        while local_root is not None:
            i = local_root.data
            local_root = local_root.right
        return i

    def size(self):
        return self.N

    def isEmpty(self):
        if self.root is None:
            return True
        else:
            return False
