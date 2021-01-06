import sys
from chyson.algorithm.utils import *
import cProfile
from chyson.algorithm.array import list1


def cut_rod(p, n):
    """

    :param p: price table
    :param n: the rod length
    :return: the maximum revenue
    """
    if n == 0:
        return 0
    q = -sys.maxsize  # stands for negative infinity
    for i in close_range(1, n):
        q = max(q, p[i] + cut_rod(p, n - i))
    return q


def memoized_cut_rod_aux(p, n, r):
    """

    :param p: optimal solution (maximum revenue)
    :param n: the rod length
    :param r: revenue list storing revenue computed at a specified length
    :return:
    """
    # that is to say, the revenue is computed before
    # because all the revenue is positive if it has a length
    # then reuse the revenue
    # i.e. to check whether the revenue is known
    if r[n] >= 0:
        return r[n]
    # the rod length is zero
    if n == 0:  # termination condition
        q = 0
    else:
        q = -sys.maxsize
        for i in close_range(1, n):
            q = max(q, p[i] + memoized_cut_rod_aux(p, n - i, r))
    r[n] = q  # save the computed revenue
    return q


def memoized_cut_rod(p, n):
    r = [-sys.maxsize] * (n + 1)  # initialize an revenue array
    return memoized_cut_rod_aux(p, n, r)


def bottom_up_cut_rod(p, n):
    r = [0] * (n + 1)
    # loop the rod length:
    for j in close_range(1, n):
        q = -sys.maxsize  # sentinel
        for i in close_range(1, j):  # i<=j
            q = max(q, p[i] + r[j - i])  # r[j-i] the computed revenue
        r[j] = q  # save the computed revenue
    return r[n]


def extended_bottom_up_cut_rod(p, n):
    r = [0] * (n + 1)
    # # wonderful simpler solution
    # maintaining only element
    s = [0] * (n + 1)
    for j in close_range(1, n):
        q = -sys.maxsize
        for i in close_range(1, j):
            if q < p[i] + r[j - i]:
                q = p[i] + r[j - i]
                s[j] = i  # maintains the length information
        r[j] = q
    return r, s


def print_cut_rod_solution(p, n):
    r, s = extended_bottom_up_cut_rod(p, n)
    while n > 0:
        print(s[n])
        n = n - s[n]  # decomposition


if __name__ == '__main__':
    p = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
    p = list1(p)
    n = len(p)

    # print(cut_rod(p, n))
    # cProfile.run("for i in range(10000): cut_rod(p, n)")
    # print('-' * 100)

    # print(memoized_cut_rod(p, n))
    # cProfile.run('for i in range(10000): memoized_cut_rod(p, n)')
    # print('-' * 100)

    # print(bottom_up_cut_rod(p, n))
    # cProfile.run('for i in range(10000): bottom_up_cut_rod(p, n)')

    # 30
    #          46050003 function calls (35820003 primitive calls) in 16.180 seconds
    #
    #    Ordered by: standard name
    #
    #    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
    #         1    0.005    0.005   16.180   16.180 <string>:1(<module>)
    # 10240000/10000    8.420    0.000   16.175    0.002 rod_cut.py:6(cut_rod)
    #  10230000    3.448    0.000    4.239    0.000 utils.py:41(__getitem__)
    #   5120000    1.582    0.000    1.582    0.000 utils.py:48(close_range)
    #         1    0.000    0.000   16.180   16.180 {built-in method builtins.exec}
    #  10230000    1.933    0.000    1.933    0.000 {built-in method builtins.max}
    #  10230000    0.791    0.000    0.791    0.000 {function ArrayFromOne.__getitem__ at 0x7f3126f0e0d0}
    #         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
    #
    #
    # ----------------------------------------------------------------------------------------------------
    # 30
    #          2320003 function calls (1770003 primitive calls) in 0.737 seconds
    #
    #    Ordered by: standard name
    #
    #    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
    #         1    0.003    0.003    0.737    0.737 <string>:1(<module>)
    # 560000/10000    0.385    0.000    0.729    0.000 rod_cut.py:21(memoized_cut_rod_aux)
    #     10000    0.005    0.000    0.734    0.000 rod_cut.py:46(memoized_cut_rod)
    #    550000    0.175    0.000    0.213    0.000 utils.py:41(__getitem__)
    #    100000    0.030    0.000    0.030    0.000 utils.py:48(close_range)
    #         1    0.000    0.000    0.737    0.737 {built-in method builtins.exec}
    #    550000    0.100    0.000    0.100    0.000 {built-in method builtins.max}
    #    550000    0.039    0.000    0.039    0.000 {function ArrayFromOne.__getitem__ at 0x7f3126f0e0d0}
    #         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
    #
    #
    # ----------------------------------------------------------------------------------------------------
    # 30
    #          1770003 function calls in 0.580 seconds
    #
    #    Ordered by: standard name
    #
    #    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
    #         1    0.003    0.003    0.580    0.580 <string>:1(<module>)
    #     10000    0.234    0.000    0.577    0.000 rod_cut.py:51(bottom_up_cut_rod)
    #    550000    0.170    0.000    0.207    0.000 utils.py:41(__getitem__)
    #    110000    0.034    0.000    0.034    0.000 utils.py:48(close_range)
    #         1    0.000    0.000    0.580    0.580 {built-in method builtins.exec}
    #    550000    0.102    0.000    0.102    0.000 {built-in method builtins.max}
    #    550000    0.038    0.000    0.038    0.000 {function ArrayFromOne.__getitem__ at 0x7f3126f0e0d0}
    #         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
    print('-' * 100)
    print(extended_bottom_up_cut_rod(p, n))
    # ([0, 1, 5, 8, 10, 13, 17, 18, 22, 25, 30], [0, 1, 2, 3, 2, 2, 6, 1, 2, 3, 10])

    for i in close_range(1, 10):
        print_cut_rod_solution(p, i)
        print('-' * 100)
