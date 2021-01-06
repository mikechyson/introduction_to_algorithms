import sys
import math
import numpy as np
import copy


# assume that A[p,q] and A[q+1,r] are in sorted order
def merge(A, p, q, r):
    # get the sub array length
    n1 = q - p + 1  # left sub array length
    n2 = r - q  # right sub array length

    # copy elements
    # init left and right sub array
    L = []
    R = []
    for i in range(n1):  # copy
        L.append(A[p + i])
    for j in range(n2):  # copy
        R.append(A[q + 1 + j])

    # set the sentinel
    L.append(sys.maxsize)  # sentinel
    R.append(sys.maxsize)  # sentinel

    i = j = 0
    for k in range(p, r + 1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
    return A


def merge_sort(A, p, r):
    if p < r:
        q = math.floor((p + r) / 2)
        merge_sort(A, p, q)
        merge_sort(A, q + 1, r)
        merge(A, p, q, r)
    return A


if __name__ == '__main__':
    np.random.seed(1)
    lst = np.random.randint(1, 100, (10,), dtype='int')
    print(lst)
    A = merge_sort(lst, 0, len(lst) - 1)
    print(A)

    # # debug
    # left = list(range(0, 20, 4))
    # right = list(range(2, 30, 3))
    # A = left + right
    # print(A)
    # A = merge(A, 0, len(left) - 1, len(A) - 1)
    # print(A)
