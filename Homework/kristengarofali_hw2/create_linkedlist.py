class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def insert_at_head(self, i):
        if self.head is None:
            n = Node(i,None)
            self.head = n
            self.tail = n
        else:
            old_head = self.head
            n = Node(i, old_head)
            self.head = n
            n.next = old_head

    def delete_at_head(self):
        if self.head is None:
            self.tail = None
        else:
            x = self.head.data
            self.head = self.head.next
            return x

    def insert_at_tail(self, i):
        n = Node(i,None)
        if self.head is None:
            self.head = n
            self.tail = n
        else:
            self.tail.next = n
            self.tail = n

def traverse_linkedlist(node):
    list = []
    while node.next is not None:
        list.append(node.data)
        node = node.next
    else:
        list.append(node.data)
    print list
