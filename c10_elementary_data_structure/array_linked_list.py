import numpy as np
import pprint


class LinkedList:
    def __init__(self, length):
        self.length = length
        # [next, key, prev]
        self.array = [[i, None, None] for i in range(1, length)]
        self.array.append([None, None, None])
        self.free = 0
        self.head = None
        self.tail = None

    def allocate_object(self):
        if self.free is None:
            raise Exception('out of space')
        else:
            idx = self.free
            self.free = self.array[idx][0]
            return idx

    def free_object(self, idx):
        self.array[idx][0] = self.free
        self.free = idx

    def search(self, k):
        idx = self.head
        while idx is not None and self.array[idx][1] != k:
            idx = self.array[idx][0]
        return idx

    def insert(self, k):
        idx = self.allocate_object()
        self.array[idx][1] = k
        self.array[idx][0] = self.head
        if self.head is not None:
            self.array[self.head][2] = idx
        self.head = idx
        self.array[idx][2] = None

    def delete(self, k):  # todo debug
        idx = self.search(k)
        if idx is not None:
            print(self.head)
            print(idx)
            # delete element
            if self.array[idx][2] is not None:
                self.array[self.array[idx][2]][0] = self.array[idx][0]
            else:
                self.head = self.array[idx][0]

            if self.array[idx][0] is not None:
                self.array[self.array[idx][0]][2] = self.array[idx][2]

            # free object
            self.free_object(idx)
        else:
            raise Exception('No such element: {}'.format(k))

    def __str__(self):
        result = ''

        def ap(result, num):
            for i in self.array:
                result += '{: <5}'.format(str(i[num]))
            result += '\n'
            return result

        result = ap(result, 0)
        result = ap(result, 1)
        result = ap(result, 2)
        return result

    def free_elements(self):
        result = []
        idx = self.free
        while idx is not None:
            result.append(idx)
            idx = self.array[idx][0]
        return result

    def contained_element(self):
        result = []
        idx = self.head
        while idx is not None:
            result.append(self.array[idx][1])
            idx = self.array[idx][0]
        return result


if __name__ == '__main__':
    l = LinkedList(10)
    print(l)
    print(l.contained_element())
    print(l.free_elements())
    print('=' * 100)

    l.insert(5)
    l.insert(8)
    l.insert(16)
    print(l)
    print(l.contained_element())
    print(l.free_elements())
    print('=' * 100)

    print(l.search(5))
    print(l.search(8))
    print('=' * 100)

    l.delete(8)
    print(l)
    print(l.contained_element())
    print(l.free_elements())
    l.delete(5)
    print(l)
    print(l.contained_element())
    print(l.free_elements())
