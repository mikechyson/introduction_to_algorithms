from chyson.algorithm.utils import *
from chyson.algorithm.array import *


class Stack:
    def __init__(self, length):
        self.top = 0
        self.length = length
        self.array = ArrayFromOne([0] * length)

    def empty(self):
        if self.top == 0:
            return True
        else:
            return False

    def full(self):
        if self.top == self.length:
            return True
        else:
            return False

    def push(self, x):
        if self.full():
            raise Exception('overflow')
        else:
            self.top = self.top + 1
            self.array[self.top] = x

    def pop(self):
        if self.empty():
            raise Exception('underflow')
        else:
            self.top = self.top - 1
            return self.array[self.top + 1]

    def __str__(self):
        stack = []
        for i in close_range(1, self.top):
            stack.append(self.array[i])
        return str(stack)


if __name__ == '__main__':
    s = Stack(3)
    print(s.empty())
    print(s.full())
    # s.pop()
    s.push(1)
    s.push(2)
    s.push(3)
    print(s)
    # s.push(4)
    print(s.pop())
    print(s.pop())
    print(s)
