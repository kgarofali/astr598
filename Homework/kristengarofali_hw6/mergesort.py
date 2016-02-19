import numpy as np

def merge_sort(a):

    #base case
    if len(a) <= 1:
        return a
    #recursion, sort left half & right half
    else:
        mid = len(a) / 2
        left = merge_sort(a[:mid])
        right = merge_sort(a[mid:])

        i = 0
        j = 0
        k = 0

        while i < len(left)  and j < len(right):
            if left[i] < right[j]:
                a[k] = left[i]
                i += 1
            else:
                a[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            a[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            a[k] = right[j]
            j += 1
            k += 1
        return a
