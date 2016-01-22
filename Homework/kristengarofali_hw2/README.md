Make sure you are in the kristengarofali_hw2 directory, then run ``` python myprogram.py ```
This will output the linked list in python list format.

We do not include a ``` delete_at_tail ``` method in the ``` LinkedList ``` class, because
this method would be O(N) for a singly-linked list, i.e. we would have to traverse the entire
list in order to set the new tail after the old tail is deleted and the value at that node returned.
