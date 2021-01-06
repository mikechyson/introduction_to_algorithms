from chyson.algorithm.utils import close_range
from chyson.algorithm.array import list1

t = 4


class Node:
    """
    Node of B-trees.
    """

    def __init__(self, c=[], key=[]):
        self.c = list1(c)
        self.key = list1(key)

    def __str__(self):
        return 'c: {}; key: {}'.format(self.c, self.key)


class T:
    """
    B-tree
    """


def allocate_node(c=[], key=[]):
    """
    Simulate the allocation of a disk storage.
    :return:
    """
    return Node(c, key)


def b_tree_search(x, k):
    """

    :param x: pointer to a node
    :param k: key needed to be searched for
    :return: the node and index if success, None if failed
    """
    i = 1
    while i <= x.n and k > x.key[i]:
        i = i + 1
    if i <= x.n and k == x.key[i]:
        return x, i
    elif x.leaf:
        return None
    else:
        print('DISK-READ(x.c[{}])'.format(i))
        return b_tree_search(x.c[i], k)


def b_tree_create(T):
    """
    Initialize the root attribute of the B-tree.
    :param T: the pointer to the B-tree.
    :return:
    """
    x = allocate_node()
    x.leaf = True
    x.n = 0
    print('DISK-WRITE(x) x=> {}'.format(x))
    T.root = x


def b_tree_split_child(x, i):
    # the child part operation
    z = allocate_node(key=[None] * (t - 1), c=[None] * t)  # because x.c[i] is full, allocate a new node
    y = x.c[i]
    z.leaf = y.leaf
    z.n = t - 1
    for j in close_range(1, t - 1):  # copy right half of the y node to z node
        z.key[j] = y.key[j + t]
    if not y.leaf:
        for j in close_range(1, t):  # copy the children links
            z.c[j] = y.key[j + t]
    y.n = t - 1

    # x node part operation
    # all right part c increase 1
    x.c.append(None)  # extend c length by 1
    x.key.append(None)  # extend c length by 1
    if x.n > 0:  # otherwise there is no need to the following copying
        for j in close_range(x.n + 1, i + 1):
            x.c[j + 1] = x.c[j]
    x.c[i + 1] = z
    # all right part keys increase 1
    if x.n > 0:
        for j in close_range(x.n, i):
            x.key[j + 1] = x.key[j]
    x.key[i] = y.key[t]
    x.n = x.n + 1
    print('DISK-WRITE(y) y=> {}'.format(y))
    print('DISK-WRITE(z) z=> {}'.format(z))
    print('DISK-WRITE(x) x=> {}'.format(x))


def b_tree_insert(T, k):
    r = T.root
    if r.n == 2 * t - 1:
        s = allocate_node()
        T.root = s
        s.leaf = False
        s.n = 0
        s.c.append(r)
        b_tree_split_child(s, 1)
        b_tree_insert_nonfull(s, k)
    else:
        b_tree_insert_nonfull(r, k)


def b_tree_insert_nonfull(x, k):
    i = x.n
    if x.leaf:
        x.key.append(None)  # expand key list by 1
        while i >= 1 and k < x.key[i]:
            x.key[i + 1] = x.key[i]
            i = i - 1
        x.key[i + 1] = k
        x.n = x.n + 1
        print('DISK-WRITE(x:{})'.format(k))
    else:
        while i >= 1 and k < x.key[i]:
            i = i - 1
        i = i + 1
        print('DISK-READ(x.c[{}])'.format(i))
        if x.c[i] == 2 * t - 1:
            b_tree_split_child(x, i)
            if k > x.key[i]:  # right child after split
                i = i + 1
        b_tree_insert_nonfull(x.c[i], k)

def b_tree_expand_child(x,i):
    pass


if __name__ == '__main__':
    tree = T()
    b_tree_create(tree)

    for i in list('abcdefghijklmnopqrstuvwxyz'):
        b_tree_insert(tree, i)

    result = b_tree_search(tree.root,'j')
    print(result)
