from chyson.algorithm.utils import *
import numpy as np
import copy
import math


def counting_sort(A, B, k):
    # init a array C with k elements
    # the initial elements are all 0
    C = []
    for i in close_range(0, k):
        C.append(0)

    for j in close_range(1, len(A)):
        C[A[j]] = C[A[j]] + 1
    # C[i] now contains the number of elements equal to i

    for i in close_range(1, k):
        C[i] = C[i] + C[i - 1]
    # C[i] now contains the number of elements less than or equal to i

    for j in close_range(len(A), 1):
        B[C[A[j]]] = A[j]
        C[A[j]] = C[A[j]] - 1  # update C


def counting_sort2(A):
    # init a array C with k elements
    # the initial elements are all 0

    B = copy.deepcopy(A)
    B = ArrayFromOne(B)
    k = max(A)

    C = []
    for i in close_range(0, k):
        C.append(0)

    for j in close_range(1, len(A)):
        C[A[j]] = C[A[j]] + 1
    # C[i] now contains the number of elements equal to i

    for i in close_range(1, k):
        C[i] = C[i] + C[i - 1]
    # C[i] now contains the number of elements less than or equal to i

    for j in close_range(len(A), 1):
        B[C[A[j]]] = A[j]
        C[A[j]] = C[A[j]] - 1  # update C

    for i in close_range(1, len(B)):
        A[i] = B[i]


def counting_sort3(A, key):
    P = [key(x) for x in A]
    P = ArrayFromOne(P)
    B = copy.deepcopy(A)
    B = ArrayFromOne(B)
    k = max(P)

    C = []
    for i in close_range(0, k):
        C.append(0)

    for j in close_range(1, len(P)):
        C[P[j]] = C[P[j]] + 1
    # C[i] now contains the number of elements equal to i

    for i in close_range(1, k):
        C[i] = C[i] + C[i - 1]
    # C[i] now contains the number of elements less than or equal to i

    for j in close_range(len(P), 1):
        # print('B: {} \nA: {}'.format(B, A))
        # print('B[{}] = A[{}]'.format(C[P[j]], j))
        B[C[P[j]]] = A[j]
        C[P[j]] = C[P[j]] - 1  # update C

    for i in close_range(1, len(B)):
        A[i] = B[i]


def radix_sort(A, d):
    for i in close_range(1, d):
        B = sorted(A, key=lambda x: x // (10 ** (i - 1)) % 10)  # not stable
    print(B)  # [329, 355, 457, 436, 657, 720, 839]


def radix_sort2(A, d):
    for i in close_range(1, d):
        counting_sort3(A, key=lambda x: x // (10 ** (i - 1)) % 10)


def bucket_sort(A):
    B = []
    n = len(A)
    for i in close_range(0, n - 1):
        B.append([])

    for i in close_range(1, n):
        B[math.floor(n * A[i])].append(A[i])

    for i in close_range(0, n - 1):
        B[i] = sorted(B[i])

    R = []
    for i in close_range(0, n - 1):
        R.extend(B[i])

    return R


# def n_digit(a, i):
#     print(a // (10 ** (i - 1)) % 10)


if __name__ == '__main__':
    A = [2, 5, 3, 0, 2, 3, 0, 3]
    A = ArrayFromOne(A)
    k = max(A)
    print(k)

    B = np.random.randint(0, 1, len(A), dtype=int)
    B = ArrayFromOne(B)
    print(B)

    counting_sort(A, B, k)
    print(B)

    A = [2, 5, 3, 0, 2, 3, 0, 3]
    A = ArrayFromOne(A)
    counting_sort2(A)
    print(A)
    print('=' * 100)

    # for i in close_range(1, 3):
    #     n_digit(123, i)
    A = [329, 457, 657, 839, 436, 720, 355]
    radix_sort(A, 3)

    A = ArrayFromOne(A)  # note
    radix_sort2(A, 3)
    print(A)
    print('=' * 100)

    A = [.78, .17, .39, .26, .72, .94, .21, .12, .28, .68]
    A = ArrayFromOne(A)
    A = bucket_sort(A)  # return may be better, because the original list is preserved.
    print(A)
