from chyson.algorithm.utils import *
import sys
import numpy as np
from chyson.algorithm.table import Table


def matrix_multiply(A, B):
    """

    :param A:
    :param B:
    :return:
    """
    A_row, A_column = A.shape
    B_row, B_column = B.shape
    if A_column != B_row:
        raise Exception('imcompatible dimensions')
    else:
        C = np.zeros((A_row, B_column))
        for i in range(A_row):
            for j in range(B_column):
                for k in range(A_column):
                    C[i][j] = C[i][j] + A[i][k] * B[k][j]
        return C


def matrix_chain_order(p):
    """
    Given a matrix chain, find the parenthesis to minimize the number
    of scala multiplication.
    :param p: The matrix shape list. For example: p = [2, 3, 5, 3]
              starts for matrix multiplication 2x3 * 3x5 * 5x3
    :return:
    """
    n = len(p) - 1  # n = p.length -1
    # minimum scalar multiplication
    # m[i,j]
    m = Table(n, n)
    # record which index of k achieved the optimal cost in computing m[i,j]
    # s[k,k+1]
    s = Table(n - 1, n - 1, x_shift=1, y_shift=2)

    for l in close_range(2, n):
        for i in close_range(1, n - l + 1):
            j = i + l - 1
            m.set(i, j, sys.maxsize)
            for k in close_range(i, j - 1):
                q = m.get(i, k) + m.get(k + 1, j) + p[i - 1] * p[k] * p[j]
                if q < m.get(i, j):
                    m.set(i, j, q)
                    s.set(i, j, k)
    return m, s


def print_optimal_parens(s, i, j):
    """

    :param s: a table that stores the divide index k and k+1
    :param i: the length of one input sequence
    :param j: the length of another input sequence
    :return:
    """
    if i == j:
        print('A[{}]'.format(i), end='')
    else:
        print('(', end='')
        print_optimal_parens(s, i, s.get(i, j))
        print_optimal_parens(s, s.get(i, j) + 1, j)
        print(')', end='')


if __name__ == '__main__':
    np.random.seed(1)
    A = np.random.randint(0, 10, [3, 4])
    B = np.random.randint(0, 10, [4, 3])
    print(A)
    print(B)
    print(np.dot(A, B))
    print(matrix_multiply(A, B))
    print('-' * 100)

    p = [10, 10, 100, 10, 1000, 50]
    m, s = matrix_chain_order(p)
    print(s)
    print_optimal_parens(s, 1, len(p) - 1)
    # [[1 1 3 3]
    #  [0 2 3 3]
    #  [0 0 3 3]
    #  [0 0 0 4]]
    # ((A[1](A[2]A[3]))(A[4]A[5]))
