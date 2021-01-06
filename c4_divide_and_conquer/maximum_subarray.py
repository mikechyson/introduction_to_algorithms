import sys
import numpy as np
import math


def find_max_crossing_subarray(A, low, mid, high):
    left_sum = -sys.maxsize  # negative infinity
    sum = 0
    for i in range(mid, low - 1, -1):
        sum = sum + A[i]
        if sum > left_sum:
            left_sum = sum
            max_left = i

    right_sum = -sys.maxsize
    sum = 0
    for i in range(mid + 1, high + 1):
        sum = sum + A[i]
        if sum > right_sum:
            right_sum = sum
            max_right = i

    return max_left, max_right, left_sum + right_sum


def find_maximum_subarray(A, low, high):
    if high == low:
        return low, high, A[low]  # bae case: only one element
    else:
        mid = math.floor((low + high) / 2)
        left_low, left_high, left_sum = find_maximum_subarray(A, low, mid)
        right_low, right_high, right_sum = find_maximum_subarray(A, mid + 1, high)
        cross_low, cross_high, cross_sum = find_max_crossing_subarray(A, low, mid, high)
        if left_sum >= right_sum and left_sum >= cross_sum:
            return left_low, left_high, left_sum
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return right_low, right_high, right_sum
        else:
            return cross_low, cross_high, cross_sum


if __name__ == '__main__':
    np.random.seed(2)
    A = np.random.randint(-10, 10, (10,))
    print(A)
    res = find_maximum_subarray(A, 0, len(A) - 1)
    print(res)

    # prove the result
    for i in range(len(A)):
        sum = 0
        sum_max = 0
        for j in range(i, len(A)):
            sum = sum + A[j]
            if sum > sum_max:
                sum_max = sum
        print(sum_max)
