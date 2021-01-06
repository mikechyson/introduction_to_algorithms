# An interval tree is a red-black tree that maintains a dynamic set of elements, with
# each element x containing an interval x.int.
import collections
import sys

from chyson.algorithm.tree import func_max
from chyson.algorithm.tree import insert_fixup
from chyson.algorithm.tree import left_rotate
from chyson.algorithm.tree import right_rotate
from chyson.algorithm.tree import transplant, minimum

Interval = collections.namedtuple('Interval', 'low high')


class Node:
    def __init__(self, interval=Interval(-sys.maxsize, -sys.maxsize), max_=-sys.maxsize, left=None, right=None, p=None,
                 color='red'):
        self.interval = interval
        self.max_ = max_
        self.left = left
        self.right = right
        self.p = p
        self.color = color


nil = Node(color='black')


def overlap(i, j):
    if i.low <= j.high and j.low <= i.high:
        return True
    return False


class IntervalTree:

    def __init__(self):
        self.root = nil
        self.nil = nil

    def search(self, i):
        x = self.root
        while x != self.nil and not overlap(i, x.interval):
            if x.left != self.nil and x.left.max_ >= i.low:
                x = x.left
            else:
                x = x.right
        return x

    def inorder_walk(self, x):
        if x is not None and x.interval.low is not None:
            self.inorder_walk(x.left)
            if x.interval.low != -sys.maxsize:
                print(x.interval, x.max_)
            self.inorder_walk(x.right)

    def insert(self, z):
        y = self.nil
        x = self.root
        while x != self.nil:
            y = x
            if z.interval.low < x.interval.low:
                x = x.left
            else:
                x = x.right
        z.p = y
        if y == self.nil:
            self.root = z
        elif z.interval.low < y.interval.low:
            y.left = z
        else:
            y.right = z

        z.left = self.nil
        z.right = self.nil
        z.color = 'red'

        self.insert_fixup(z)
        self.max_fixup(self.root)
        return z

    def left_rotate(self, x):
        left_rotate(self, self.nil, x, func_max)

    def right_rotate(self, y):
        right_rotate(self, self.nil, y, func_max)

    def insert_fixup(self, z):
        insert_fixup(self, z, func_max)

    def delete(self, z):
        y = z
        y_original_color = y.color
        if z.left == self.nil:
            x = z.right
            transplant(self, z, z.right)
        elif z.right == self.nil:
            x = z.left
            transplant(self, z, z.left)
        else:
            y = minimum(self, z.right)
            y_original_color = y.color
            x = y.right
            if y.p == z:
                x.p = y
            else:
                transplant(self, y, y.right)
                y.right = z.right
                y.right.p = y
            transplant(self, z, y)
            y.left = z.left
            y.left.p = y
            y.color = z.color
        if y_original_color == 'black':
            self.delete_fixup(x)
        self.max_fixup(self.root)

    def delete_fixup(self, x):
        while x != self.nil and x.color == 'black':
            if x == x.p.left:
                w = x.p.right  # w is x's sibling
                # in this case: turn w's color into black
                if w.color == 'red':
                    w.color = 'black'
                    x.p.color = 'red'
                    self.left_rotate(x.p)
                    w = x.p.right
                # in this case: move x up
                if w.left.color == 'black' and w.right.color == 'black':
                    w.color = 'red'
                    x = x.p
                else:
                    # in this case: turn w.right.color into red
                    if w.right.color == 'black':
                        w.left.color = 'black'
                        w.color = 'red'
                        self.right_rotate(w)
                        w = x.p.right
                    w.color = x.p.color
                    x.p.color = 'black'
                    w.right.color = 'black'
                    self.left_rotate(x.p)
                    x = self.root
            else:
                if x == x.p.right:
                    w = x.p.left  # w is x's sibling
                    # in this case: turn w's color into black
                    if w.color == 'red':
                        w.color = 'black'
                        x.p.color = 'red'
                        self.right_rotate(x.p)
                        w = x.p.left
                    # in this case: move x up
                    if w.right.color == 'black' and w.left.color == 'black':
                        w.color = 'red'
                        x = x.p
                    else:
                        # in this case: turn w.left.color into red
                        if w.left.color == 'black':
                            w.right.color = 'black'
                            w.color = 'red'
                            self.left_rotate(w)
                            w = x.p.left
                        w.color = x.p.color
                        x.p.color = 'black'
                        w.left.color = 'black'
                        self.right_rotate(x.p)
                        x = self.root
        x.color = 'black'

    def max_fixup(self, x):
        if x.left == self.nil and x.right == self.nil:
            x.max_ = x.interval.high
            return x.max_
        elif x.left == self.nil:
            x.max_ = max(x.interval.high, self.max_fixup(x.right))
            return x.max_
        elif x.right == self.nil:
            x.max_ = max(x.interval.high, self.max_fixup(x.left))
            return x.max_
        else:
            x.max_ = max(x.interval.high, self.max_fixup(x.left), self.max_fixup(x.right))
            return x.max_


def build_node(low, high):
    return Node(Interval(low, high), left=nil, right=nil)


if __name__ == '__main__':
    t = IntervalTree()
    t.insert(build_node(10, 100))
    x = t.insert(build_node(5, 20))
    y = t.insert(build_node(1, 30))
    t.insert(build_node(15, 25))
    t.inorder_walk(t.root)

    print('=' * 100)
    result = t.search(Interval(8, 80))
    print(result.interval)

    print('=' * 100)
    t.delete(x)
    t.inorder_walk(t.root)

# Interval(low=1, high=30) 30
# Interval(low=5, high=20) 100
# Interval(low=10, high=100) 100
# Interval(low=15, high=25) 25
# ====================================================================================================
# Interval(low=5, high=20)
# ====================================================================================================
# Interval(low=1, high=30) 30
# Interval(low=10, high=100) 100
# Interval(low=15, high=25) 25
