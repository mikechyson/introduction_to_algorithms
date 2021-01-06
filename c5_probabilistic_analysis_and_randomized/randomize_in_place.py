import numpy as np


def random_in_place(a):
    n = len(a)
    for i in range(n):
        tmp = a[i]
        random_idx = np.random.randint(i, n)
        a[i] = a[random_idx]
        a[random_idx] = tmp
    return a


a = np.arange(1, 10)
print(a)
print(random_in_place(a))
