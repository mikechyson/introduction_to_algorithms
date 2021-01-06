from chyson.algorithm.utils import close_range
from chyson.algorithm.priority_queue import MinPriorityQueue


class CF:
    def __init__(self, key, character):
        """

        :param key:
        :param character:
        """
        self.key = key
        self.character = character


class Node:
    def __init__(self, left=None, right=None, key=None, p=None, character=None):
        self.left = left
        self.right = right
        self.key = key
        self.p = p
        self.character = character


def huffman(C):
    n = len(C)
    Q = C  # min-priority queue
    for i in close_range(1, n - 1):
        z = Node()
        z.left = x = Q.extract_min()
        z.right = y = Q.extract_min()
        z.key = x.key + y.key
        Q.insert(z)
    return Q.extract_min()


# O(n) time
def inorder_tree_walk(x, simple_path=''):
    if x is not None:
        if x.character is None:  # internal node
            inorder_tree_walk(x.left, simple_path + '0')
            inorder_tree_walk(x.right, simple_path + '1')
        else:
            print('character: {} with frequency: {}; the simple path is: {}'.format(x.character, x.key, simple_path))


if __name__ == '__main__':
    C = MinPriorityQueue()
    fc = zip([45, 13, 12, 16, 9, 5], list('abcdef'))

    for f, c in fc:
        C.insert(CF(f, c))
    # print(C.heap_size)

    # for i in range(6):
    #     c = C.extract_min()
    #     print(c.key, c.character)

    root = huffman(C)
    print(root.key)  # 100

    inorder_tree_walk(root)
    # character: a with frequency: 45; the simple path is: 0
    # character: c with frequency: 12; the simple path is: 100
    # character: b with frequency: 13; the simple path is: 101
    # character: f with frequency: 5; the simple path is: 1100
    # character: e with frequency: 9; the simple path is: 1101
    # character: d with frequency: 16; the simple path is: 111

# debug
# obj.key: 45; A[1].key: 9223372036854775807
# obj.key: 13; A[2].key: 9223372036854775807
# obj.key: 12; A[3].key: 9223372036854775807
# obj.key: 16; A[4].key: 9223372036854775807
# obj.key: 9; A[5].key: 9223372036854775807
# obj.key: 5; A[6].key: 9223372036854775807
# obj.key: 14; A[5].key: 16
# obj.key: 25; A[4].key: 45
# obj.key: 30; A[3].key: 45
# obj.key: 55; A[2].key: 45
# obj.key: 100; A[1].key: 55
# 11
