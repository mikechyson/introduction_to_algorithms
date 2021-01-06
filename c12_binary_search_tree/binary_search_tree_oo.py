class Node:
    def __init__(self, key, p=None, left=None, right=None):
        self.key = key
        self.p = p
        self.left = left
        self.right = right


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def inorder_walk(self, x):
        """

        :param x: The node from where to iterate
        :return: print all the node keys in order
        """
        if x is not None:
            self.inorder_walk(x.left)
            print(x.key)
            self.inorder_walk(x.right)

    def search(self, x, k):
        """

        :param x: The node from where to search for key k
        :param k: the key
        :return:
        """
        if x is None or k == x.key:
            return x
        if k < x.key:
            return self.search(x.left, k)
        else:
            return self.search(x.right, k)

    @staticmethod
    def iterative_search(x, k):
        while x is not None and k != x.key:
            if x < x.key:
                x = x.left
            else:
                x = x.right
        return x

    def iterative_minimum(self):
        x = self.root
        while x.left is not None:
            x = x.left
        return x

    def minimum(self, x):
        if x.left is None:
            return x
        else:
            return self.minimum(x.left)  # remember to return

    @staticmethod
    def iterative_maximum(x):
        while x.right is not None:
            x = x.right
        return x

    def maximum(self, x):
        if x.right is None:
            return x
        else:
            return self.maximum(x.right)  # remember to return

    @staticmethod
    def iterative_successor(x):
        if x.right is not None:
            return BinarySearchTree.iterative_minimum(x.right)

        y = x.p
        while y is not None and x == y.right:
            x = y
            y = y.p
        return y

    def successor(self, x):
        if x.right is not None:
            return self.minimum(x.right)
        y = x.p
        if y is not None and x == y.left:
            return y
        else:
            return self.successor(y)

    @staticmethod
    def iterative_predecessor(x):
        if x.left is not None:
            return BinarySearchTree.iterative_maximum(x.left)
        y = x.p
        while y is not None and x == y.left:
            x = y
            y = y.p
        return y

    def predecessor(self, x):
        if x.left is not None:
            return self.maximum(x.left)
        y = x.p
        if y is not None and x == y.right:
            return y
        else:
            return self.predecessor(y)

    def insert(self, z):
        y = None
        x = self.root
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
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z

    def transplant(self, u, v):
        """
        replace one subtree as a child of its parent with another subtree.
        :param u:
        :param v:
        :return:
        """

        if u.p is None:
            self.root = v
        elif u == u.p.left:
            u.p.left = v
        else:
            u.p.right = v

        if v is not None:
            v.p = u.p

    def delete(self, z):
        if z.left is None:
            self.transplant(z, z.right)
        elif z.right is None:
            self.transplant(z, z.left)
        else:
            y = self.minimum(z.right)  # successor
            if y.p != z:  # not right child
                self.transplant(y, y.right)
                y.right = z.right
                y.right.p = y
            self.transplant(z, y)
            y.left = z.left
            y.left.p = y


if __name__ == '__main__':
    t = BinarySearchTree()
    for i in [5, 8, 19, 1]:
        t.insert(Node(i))
    t.inorder_walk(t.root)
    print('=' * 100)
    print(t.minimum(t.root).key)
    print(t.iterative_minimum().key)
    print('=' * 100)
    print(t.search(t.root, 5).key)
    print(BinarySearchTree.iterative_search(t.root, 5).key)
    print('=' * 100)
    x = t.search(t.root, 5)
    print(t.successor(x).key)
    print(t.predecessor(x).key)
    print('=' * 100)
    t.delete(x)
    t.inorder_walk(t.root)
