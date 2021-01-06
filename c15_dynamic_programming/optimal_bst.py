from chyson.algorithm.utils import *
import sys
from chyson.algorithm.table import *
from chyson.algorithm.array import *


def optimal_bst(p, q, n):
    """
    Optimal binary search tree used in language translation like from English to French.
    The key is the English word.
    :param p: English word frequencies
    :param q: dummy frequencies when the search failed
    :param n: the length of the input language
    :return: expected search times and the root of each subtree
    """
    e = Table(n + 1, n + 1, y_shift=0, dtype='float')
    w = Table(n + 1, n + 1, y_shift=0, dtype='float')
    root = Table(n, n)
    for i in close_range(1, n + 1):
        e.set(i, i - 1, q[i - 1])  # empty subtree, only the dummy leaf
        w.set(i, i - 1, q[i - 1])  # empty subtree, only the dummy leaf
    for l in close_range(1, n):  # bottom up, the subtree length
        for i in close_range(1, n - l + 1):  # all subtree
            j = i + l - 1
            e.set(i, j, sys.maxsize)
            w.set(i, j, w.get(i, j - 1) + p[j] + q[j])  # extra space for O(1) time in computing w(i,j)
            for r in close_range(i, j):  # search for the optimal subtree
                t = e.get(i, r - 1) + e.get(r + 1, j) + w.get(i, j)
                if t < e.get(i, j):
                    e.set(i, j, t)
                    root.set(i, j, r)
    return e, root


def construct_optimal_bst(root, i, j, r=None):
    """
    Construct the optimal binary search tree according to the root table.

    :param root: a table return by optimal_bst
    :param i: the start index
    :param j: the end index
    :param r: the root index
    :return:
    """
    if r is None:
        print('k{} is the root'.format(root.get(i, j)))
    else:
        if j == i - 1:  # dummy leaf
            if j == r - 1:
                print('d{} is the left child of k{}'.format(j, r))
            else:
                print('d{} is the right child of k{}'.format(r, r))
        else:  # internal key
            if j < r:
                print('k{} is the left child of k{}'.format(root.get(i, j), r))
            else:
                print('k{} is the right child of k{}'.format(root.get(i, j), r))

    if j != i - 1:
        construct_optimal_bst(root, i, root.get(i, j) - 1, root.get(i, j))
        construct_optimal_bst(root, root.get(i, j) + 1, j, root.get(i, j))


if __name__ == '__main__':
    p = [0.15, 0.10, 0.05, 0.10, 0.20]
    q = [0.05, 0.10, 0.05, 0.05, 0.05, 0.10]
    p = ArrayFromOne(p)
    n = len(p)

    e, root = optimal_bst(p, q, n)
    # print(e)
    # print(root)
    # [[0.05 0.45 0.9  1.25 1.75 2.75]
    #  [0.   0.1  0.4  0.7  1.2  2.  ]
    #  [0.   0.   0.05 0.25 0.6  1.3 ]
    #  [0.   0.   0.   0.05 0.3  0.9 ]
    #  [0.   0.   0.   0.   0.05 0.5 ]
    #  [0.   0.   0.   0.   0.   0.1 ]]
    # [[1. 1. 2. 2. 2.]
    #  [0. 2. 2. 2. 4.]
    #  [0. 0. 3. 4. 5.]
    #  [0. 0. 0. 4. 5.]
    #  [0. 0. 0. 0. 5.]]

    construct_optimal_bst(root, 1, n)
    # k2 is the root
    # k1 is the left child of k2
    # d0 is the left child of k1
    # d1 is the right child of k1
    # k5 is the right child of k2
    # k4 is the left child of k5
    # k3 is the left child of k4
    # d2 is the left child of k3
    # d3 is the right child of k3
    # d4 is the right child of k4
    # d5 is the right child of k5
