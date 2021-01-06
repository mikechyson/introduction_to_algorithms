from chyson.algorithm.utils import *
from chyson.algorithm.table import *
from chyson.algorithm.array import *


def lcs_length(X, Y):
    m = len(X)
    n = len(Y)
    b = Table(m, n)  # record the lcs construction
    c = Table(m + 1, n + 1, x_shift=0, y_shift=0)  # record the lcs length
    for i in close_range(1, m):
        for j in close_range(1, n):
            if X[i] == Y[j]:
                c.set(i, j, c.get(i - 1, j - 1) + 1)
                # I use number to indicate the direction
                # because I use numpy as the base of the table
                b.set(i, j, -2)  # up left
            elif c.get(i - 1, j) >= c.get(i, j - 1):
                c.set(i, j, c.get(i - 1, j))
                b.set(i, j, 1)  # up
            else:
                c.set(i, j, c.get(i, j - 1))
                b.set(i, j, -1)  # right
    return c, b


def print_lcs(b, X, i, j):
    if i == 0 or j == 0:
        return
    if b.get(i, j) == -2:
        print_lcs(b, X, i - 1, j - 1)
        print(X[i], end='')
    elif b.get(i, j) == 1:
        print_lcs(b, X, i - 1, j)
    else:
        print_lcs(b, X, i, j - 1)


if __name__ == '__main__':
    X = list('ABCBDAB')
    Y = list('BDCABA')
    X = ArrayFromOne(X)
    Y = ArrayFromOne(Y)
    c, b = lcs_length(X, Y)
    # print(c)
    # print(b)
    # [[0 0 0 0 0 0 0]
    #  [0 0 0 0 1 1 1]
    #  [0 1 1 1 1 2 2]
    #  [0 1 1 2 2 2 2]
    #  [0 1 1 2 2 3 3]
    #  [0 1 2 2 2 3 3]
    #  [0 1 2 2 3 3 4]
    #  [0 1 2 2 3 4 4]]
    # [[ 1  1  1 -2 -1 -2]
    #  [-2 -1 -1  1 -2 -1]
    #  [ 1  1 -2 -1  1  1]
    #  [-2  1  1  1 -2 -1]
    #  [ 1 -2  1  1  1  1]
    #  [ 1  1  1 -2  1 -2]
    #  [-2  1  1  1 -2  1]]

    print_lcs(b, X, len(X), len(Y))  # BCBA
