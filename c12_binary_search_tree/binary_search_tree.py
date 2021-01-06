# functional programming
class Node:
    def __init__(self, key, p=None, left=None, right=None):
        self.key = key
        self.p = p
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self):
        self.root = None


# O(n) time
def inorder_tree_walk(x):
    if x is not None:
        inorder_tree_walk(x.left)
        print(x.key)
        inorder_tree_walk(x.right)


def tree_search(x, k):
    if x is None or k == x.key:
        return x
    if k < x.key:
        return tree_search(x.left, k)
    else:
        return tree_search(x.right, k)


def iterative_tree_search(x, k):
    while x is not None and k != x.key:
        if k < x.key:
            x = x.left
        else:
            x = x.right
    return x


def tree_minimum(x):
    while x.left is not None:
        x = x.left
    return x


def tree_maximum(x):
    while x.right is not None:
        x = x.right
    return x


def tree_successor(x):
    if x.right is not None:
        return tree_minimum(x.right)

    y = x.p
    while y is not None and x == y.right:
        x = y
        y = y.p
    return y


def tree_predecessor(x):
    if x.left is not None:
        return tree_maximum(x.left)
    y = x.p
    while y is not None and x == y.left:
        x = y
        y = y.p
    return y


def tree_insert(T, z):
    y = None
    x = T.root
    # walk down
    while x is not None:
        y = x
        if z.key < x.key:
            x = x.left
        else:
            x = x.right
    # link
    z.p = y
    if y is None:
        T.root = z
    elif z.key < y.key:
        y.left = z
    else:
        y.right = z


def transplant(T, u, v):
    """
    replace one subtree as a child of its parent with another subtree.
    :param T:
    :param u:
    :param v:
    :return:
    """
    if u.p is None:
        T.root = v
    elif u == u.p.left:
        u.p.left = v
    else:
        u.p.right = v

    if v is not None:
        v.p = u.p


def tree_delete(T, z):
    if z.left is None:
        transplant(T, z, z.right)
    elif z.right is None:
        transplant(T, z, z.left)
    else:
        y = tree_minimum(z.right)  # successor
        if y.p != z:  # not right child
            transplant(T, y, y.right)
            y.right = z.right
            y.right.p = y
        transplant(T, z, y)
        y.left = z.left
        y.left.p = y


if __name__ == '__main__':
    T = BinaryTree()
    tree_insert(T, Node(5))
    tree_insert(T, Node(8))
    tree_insert(T, Node(19))
    tree_insert(T, Node(1))
    inorder_tree_walk(T.root)
    print('=' * 100)
    print(tree_minimum(T.root).key)
    print(tree_maximum(T.root).key)
    print('=' * 100)
    print(tree_search(T.root, 5).key)
    print('=' * 100)
    x = tree_search(T.root, 5)
    print(tree_successor(x).key)
    print(tree_predecessor(x).key)
    print('=' * 100)
    tree_delete(T, x)
    inorder_tree_walk(T.root)
