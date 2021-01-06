from chyson.algorithm.utils import *
import numpy as np


def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in close_range(p, r - 1):
        if A[j] <= x:
            i = i + 1
            swap(A, i, j)
    swap(A, i + 1, r)
    return i + 1


def quicksort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quicksort(A, p, q - 1)
        quicksort(A, q + 1, r)


def randomized_partition(A, p, r):
    i = np.random.randint(p, r, dtype=int)
    swap(A, r, i)
    return partition(A, p, r)


def randomized_quicksort(A, p, r):
    if p < r:
        q = randomized_partition(A, p, r)
        randomized_quicksort(A, p, q - 1)
        randomized_quicksort(A, q + 1, r)


if __name__ == '__main__':
    A = A1([2, 8, 7, 1, 3, 5, 6, 4])
    quicksort(A, 1, len(A))  # expected: [1, 2, 3, 4, 5, 6, 7, 8]
    print(A)

    A = A1([2, 8, 7, 1, 3, 5, 6, 4])
    randomized_quicksort(A, 1, len(A))
    print(A)
