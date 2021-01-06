from chyson.algorithm.utils import *


def insertion_sort(lst):
    for j in close_range(2, len(lst)):
        key = lst[j]
        # Insert A[j] into the sorted sequence A[1..j-1]
        i = j - 1
        while i > 0 and lst[i] > key:
            lst[i + 1] = lst[i]
            i = i - 1
        lst[i + 1] = key
    # print(lst)


def insertion_sort_decreasing(lst):
    for j in close_range(2, len(lst)):
        key = lst[j]
        # Insert A[j] into the sorted sequence A[1..j-1]
        i = j - 1
        while i > 0 and lst[i] < key:
            lst[i + 1] = lst[i]
            i = i - 1
        lst[i + 1] = key
    # print(lst)


test = [4, 2, 5, 9, 0, 11, 20, 13]
test = ArrayFromOne(test)
insertion_sort(test)  # [0, 2, 4, 5, 9, 11, 13, 20]
insertion_sort_decreasing(test)
