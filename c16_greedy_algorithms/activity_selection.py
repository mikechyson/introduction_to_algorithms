from chyson.algorithm.utils import *
from chyson.algorithm.array import list1


def recursive_activity_selector(s, f, k, n):
    """

    :param s: a list of start time, the first element is 0
    :param f: a list of finish time, the first element is 0
    :param k: the smallest finish time activity
    :param n: the length of the activities
    :return: a optimal activity selection
    """

    m = k + 1
    while m <= n and s[m] < f[k]:  # find the first activity in S k to finish
        m = m + 1
    if m <= n:
        return ['a_{}'.format(m)] + recursive_activity_selector(s, f, m, n)
    else:
        return []


def greedy_activity_selector(s, f):
    """

    :param s: a list of start time
    :param f: a list of finish time,
    :return: a optimal activity selection
    """
    n = len(s)
    A = ['a_{}'.format(1)]  # the activities is sorted in monotonically increasing order of finish time
    k = 1  # the first is the greedy choice, i.e. the finishing time is the minimal
    for m in close_range(2, n):
        if s[m] >= f[k]:  # compatible
            A = A + ['a_{}'.format(m)]
            k = m
    return A


if __name__ == '__main__':
    s = [0, 1, 3, 0, 5, 3, 5, 6, 8, 8, 2, 12]
    f = [0, 4, 5, 6, 7, 9, 9, 10, 11, 12, 14, 16]

    result = recursive_activity_selector(s, f, 0, len(s) - 1)
    print(result)
    # ['a_1', 'a_4', 'a_8', 'a_11']

    s = [1, 3, 0, 5, 3, 5, 6, 8, 8, 2, 12]
    f = [4, 5, 6, 7, 9, 9, 10, 11, 12, 14, 16]
    s = list1(s)
    f = list1(f)
    result = greedy_activity_selector(s, f)
    print(result)  # ['a_1', 'a_4', 'a_8', 'a_11']
