from chyson.algorithm.utils import *
from chyson.algorithm.array import *


class Queue:
    def __init__(self, length):
        self.length = length
        self.array = ArrayFromOne([0] * (length + 1))
        self.head = 1
        self.tail = 1

    def empty(self):
        if self.head == self.tail:
            return True
        else:
            return False

    def full(self):
        if self.tail - self.head == self.length or self.head - self.tail == 1:
            return True
        else:
            return False

    def enqueue(self, x):
        if self.full():
            raise Exception('overflow')
        else:
            self.array[self.tail] = x
            if self.tail == self.length + 1:
                self.tail = 1
            else:
                self.tail = self.tail + 1

    def dequeue(self):
        if self.empty():
            raise Exception('underflow')
        else:
            x = self.array[self.head]
            if self.head == self.length + 1:
                self.head = self.head + 1
            else:
                self.head = self.head + 1
            return x

    def __str__(self):
        if self.empty():
            return '[]'
        else:
            result = []
            for i in close_range(self.head, self.tail - 1):
                result.append(self.array[i])
            return str(result)


if __name__ == '__main__':
    q = Queue(7)
    print(q.empty())
    print(q)
    # q.dequeue()
    for i in range(1, 8):
        q.enqueue(i)
    print(q)
    # q.enqueue(8)
    print(q.dequeue())
    print(q)
