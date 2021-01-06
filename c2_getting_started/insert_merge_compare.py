import math

for n in range(1, 100):
    if 8 * n * n <= 64 * n * math.log2(n):
        print(n)

print('-' * 100)
for n in range(1, 100):
    if 100 * n * n <= math.exp(n):
        print(n)

print('-' * 100)
for n in range(1, 1000):
    if n * math.log2(n) <= 1000:
        print(n)

print('-' * 100)


def frac(n):
    f = 1
    for i in range(1, n):
        f *= i
    return f


for i in range(1, 1000):
    if frac(i) <= 1000:
        print(i)
