import numpy as np


def permute_by_sorting(inp):
    n = len(inp)

    # priority list
    priority = np.random.randint(1, n ** 3, (n,))

    input_priority = zip(inp, priority)
    input_priority = sorted(input_priority, key=lambda x: x[1])
    print(input_priority)

    return [x[0] for x in input_priority]


a = [1, 2, 1, 2, 3, 4, 5]
print(permute_by_sorting(a))
