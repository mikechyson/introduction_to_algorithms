from chyson.algorithm.utils import *
from chyson.algorithm.array import A1
from introduction_to_algorithms.c6_heapsort.heapsort import max_heapify, parent
import sys


def heap_maximum(A):
    return A[1]


def heap_extract_max(A):
    if A.heap_size < 1:
        raise Exception('heap underflow')
    max = A[1]
    A[1] = A[A.heap_size]
    A.heap_size = A.heap_size - 1
    max_heapify(A, 1)
    return max


def heap_increase_key(A, i, key):
    if key < A[i]:
        raise Exception('new key is smaller than current key')
    A[i] = key
    while i > 1 and A[parent(i)] < A[i]:
        swap(A, i, parent(i))
        i = parent(i)


def max_heap_insert(A, key):
    A.heap_size = A.heap_size + 1
    A.append(-sys.maxsize)
    heap_increase_key(A, A.heap_size, key)


if __name__ == '__main__':
    A = A1([16, 14, 10, 8, 7, 9, 3, 2, 4, 1])
    print(heap_maximum(A))  # expected: 16
    print('=' * 100)

    A = A1([16, 14, 10, 8, 7, 9, 3, 2, 4, 1])
    print(heap_extract_max(A))
    print(A)
    print(A.heap_size)
    print(len(A))
    print('=' * 100)

    A = A1([16, 14, 10, 8, 7, 9, 3, 2, 4, 1])
    heap_increase_key(A, 9, 15)  # expected: [16, 15, 10, 14, 7, 9, 3, 2, 8, 1]
    print(A)
    print('=' * 100)

    A = A1([16, 14, 10, 8, 7, 9, 3, 2, 4, 1])
    max_heap_insert(A, 15)  # expected: [16, 15, 10, 8, 14, 9, 3, 2, 4, 1, 7]
    print(A)
