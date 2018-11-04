# usr/bin/env python
#-*-coding:utf-8-*-

import random


def quicksort(array, start, end):
    if len(array) < 2 or (len(array) == 2 and array[0] == array[1]):
        return array
    pivot = random.randint(start, end)
    left = [m for m in array[start:] if m < array[pivot]]
    mid = [m for m in array[start:] if m == array[pivot]]
    right = [m for m in array[start:] if m > array[pivot]]
    return quicksort(left, 0, len(left)-1) + quicksort(mid, 0, len(mid)-1) + quicksort(right, 0, len(right)-1)


alist = [54, 54, 26, 93, 17, 77, 31, 44, 55, 20]
sorted_alist = quicksort(alist, 0, len(alist)-1)
print(sorted_alist)
