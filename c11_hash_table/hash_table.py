from introduction_to_algorithms.c10_elementary_data_structure.linked_list import LinkedList
import math


class Element:
    def __init__(self, key):
        self.key = key


class HashTableChaining:
    def __init__(self, m):
        self.m = m
        self.A = (math.sqrt(5) - 1) / 2
        self.T = []
        for i in range(self.m):
            self.T.append(LinkedList())

    def h(self, k):
        # division method
        return k % self.m

    def h2(self, k):
        # multiplication method
        return math.floor(self.m * (k * self.A % 1))

    def search(self, k):
        lst = self.T[self.h(k)]
        return lst.search(k)

    def insert(self, k):
        lst = self.T[self.h(k)]
        lst.insert(k)

    def delete(self, k):
        lst = self.T[self.h(k)]
        lst.delete(k)

    def __str__(self):
        result = ''
        for i in self.T:
            result += str(i)
            result += '\n'
        return result


if __name__ == '__main__':
    ht = HashTableChaining(10)
    print(ht)

    ht.insert(5)
    ht.insert(6)
    print(ht)

    print(ht.search(5))
    print(ht.search(8))

    ht.delete(5)
    print(ht)
