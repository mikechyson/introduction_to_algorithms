from chyson.algorithm.utils import *
import numpy as np
from introduction_to_algorithms.c7_quicksort.quicksort import randomized_partition
from introduction_to_algorithms.c2_getting_started.insertion_sort import insertion_sort
import math


def minimum(A):
    mi = A[1]
    for i in close_range(2, len(A)):
        if mi > A[i]:
            mi = A[i]
    return mi


def min_max(A):
    if len(A) % 2 == 0:
        if A[1] > A[2]:
            mi = A[2]
            ma = A[1]
        else:
            mi = A[1]
            ma = A[2]
        start = 3
    else:
        mi = A[1]
        ma = A[2]
        start = 2

    for i in close_range(start, len(A), 2):
        if A[i] > A[i + 1]:
            if A[i] > ma:
                ma = A[i]
            if A[i + 1] < mi:
                mi = A[i + 1]
        else:
            if A[i + 1] > ma:
                ma = A[i + 1]
            if A[i] < mi:
                mi = A[i]
    return mi, ma


def randomized_select(A, p, r, i):
    if p == r:
        return A[p]
    q = randomized_partition(A, p, r)
    k = q - p + 1  # between [p, r], there are q-p elements less than A[q]
    if i == k:
        return A[q]
    elif i < k:
        return randomized_select(A, p, q - 1, i)
    else:
        return randomized_select(A, q + 1, r, i - k)


def select(A, ith):
    # divide the list into 5 elements list
    divided = ArrayFromOne()
    for i in close_range(1, len(A), 5):
        buf = ArrayFromOne()
        if i + 4 > len(A):
            for j in close_range(i, len(A)):
                buf.append(A[j])
        else:
            for j in close_range(i, i + 4):
                buf.append(A[j])
        divided.append(buf)
    print(divided)

    # insertion sort and find the medians
    medians = []
    for i in divided:
        insertion_sort(i)
        median = i[math.floor((len(i) + 1) / 2)]
        medians.append(median)
    print(divided)


if __name__ == '__main__':
    np.random.seed(1)
    A = np.random.randint(1, 10, (10,), dtype=int)
    print(A)
    A = ArrayFromOne(A)
    print(minimum(A))
    print('=' * 100)

    print(min_max(A))
    print("=" * 100)

    A = [1, 2, 3, 4, 5, 6, 7]
    A = ArrayFromOne(A)
    for i in range(1, 8):
        print('index: {} with result: {}.'.format(i, randomized_select(A, 1, len(A), i)))
    print('=' * 100)

    A = np.random.randint(1, 100, (33,), dtype=int)
    A = ArrayFromOne(A)
    print(A)
    select(A, 2)
