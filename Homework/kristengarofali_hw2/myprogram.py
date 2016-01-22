import create_linkedlist
from create_linkedlist import LinkedList
from create_linkedlist import Node

list = LinkedList()


print("Inserting int 3 at head")
list.insert_at_head(3)
print("Inserting int 4 at head")
list.insert_at_head(4)
print("Inserting int 5 at head")
list.insert_at_head(5)

print("Deleting head node: {0}".format(list.delete_at_head()))

print("Inserting int 2 at tail")
list.insert_at_tail(2)
print("Inserting int 1 at tail")
list.insert_at_tail(1)
print("Inserting int 42 at tail")
list.insert_at_tail(42)

print("Final linked list:")
create_linkedlist.traverse_linkedlist(list.head)
