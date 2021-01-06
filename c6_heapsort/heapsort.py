import math
from chyson.algorithm.utils import swap
from chyson.algorithm.array import A1
from chyson.algorithm.utils import close_range


def parent(i):
    return math.floor(i / 2)


def left(i):
    return 2 * i


def right(i):
    return 2 * i + 1


def max_heapify(A, i):
    l = left(i)
    r = right(i)

    # find the largest element
    if l <= A.heap_size and A[l] > A[i]:
        largest = l
    else:
        largest = i
    if r <= A.heap_size and A[r] > A[largest]:
        largest = r

    if largest != i:
        swap(A, i, largest)
        max_heapify(A, largest)


def build_max_heap(A):
    heap_size = len(A)
    for i in close_range(math.floor(heap_size / 2), 1):
        max_heapify(A, i)


def heapsort(A):
    build_max_heap(A)

    for i in close_range(len(A), 2):
        swap(A, 1, i)
        A.heap_size = A.heap_size - 1
        max_heapify(A, 1)


if __name__ == '__main__':
    A = [16, 4, 10, 14, 7, 9, 3, 2, 8, 1]  # expected: [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]
    A = A1(A)
    max_heapify(A, 2)
    print(A)

    A = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]  # expected: [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]
    A = A1(A)
    build_max_heap(A)
    print(A)

    A = A1([16, 14, 10, 8, 7, 9, 3, 2, 4, 1])  # expected: [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]
    heapsort(A)
    print(A)
