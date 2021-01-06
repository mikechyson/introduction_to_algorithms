class Node:
    def __init__(self, key, left=None, right=None, p=None, color='red'):
        self.key = key
        self.left = left
        self.right = right
        self.p = p
        self.color = color


nil = Node(None, color='black')


class RedBlackTree:
    def __init__(self):
        self.nil = nil
        self.root = nil

    def inorder_walk(self, x):
        if x is not None and x.key is not None:
            self.inorder_walk(x.left)
            print(x.key)
            self.inorder_walk(x.right)

    def insert(self, z):
        y = self.nil
        x = self.root

        # walk down
        while x != self.nil:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right

        # determine if the tree is empty or left or right child
        z.p = y
        if y == self.nil:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z

        z.left = self.nil
        z.right = self.nil
        z.color = 'red'

        self.insert_fixup(z)
        return z

    def left_rotate(self, x):
        # local operation while maintaining the binary search tree property
        # http://chyson.net/notes/algorithm/introduction-to-algorithms/note.html#sec-4-4-2
        y = x.right  # set y

        # beta part in the fig
        x.right = y.left
        if y.left != self.nil:
            y.left.p = x

        # y part
        y.p = x.p
        if x.p == self.nil:
            self.root = y
        elif x == x.p.left:
            x.p.left = y
        else:
            x.p.right = y

        # x part
        y.left = x
        x.p = y

    def right_rotate(self, y):
        # http://chyson.net/notes/algorithm/introduction-to-algorithms/note.html#sec-4-4-2
        x = y.left  # set x

        # beta part
        y.left = x.right
        if x.right != self.nil:
            x.right.p = y

        # x part
        x.p = y.p
        if y.p == self.nil:
            self.root = x
        elif y == y.p.left:
            y.p.left = x
        else:
            y.p.right = x

        # y part
        x.right = y
        y.p = x

    def insert_fixup(self, z):
        # the inserted node's color is red
        while z.p.color == 'red':
            if z.p == z.p.p.left:
                y = z.p.p.right  # save z.p.p.right
                # case 1: z.p is z.p.p's left child and
                # z.p.p's right child is 'red'
                if y.color == 'red':
                    # change z.p.p's left and right child to black
                    # change z.p.p to red and z.p.p is not z that
                    # need to be fixed up
                    z.p.color = 'black'
                    y.color = 'black'
                    z.p.p.color = 'red'
                    z = z.p.p
                # case 2: z.p is z.p.p's right child and
                # z.p.p's right child is 'black' and z is right child
                # Note: the following else if part is prone to be implemented with error
                else:
                    if z == z.p.right:
                        z = z.p
                        self.left_rotate(z)

                    # case 3: z is left child
                    z.p.color = 'black'
                    z.p.p.color = 'red'
                    self.right_rotate(z.p.p)
            else:
                y = z.p.p.left
                if y.color == 'red':
                    z.p.color = 'black'
                    y.color = 'black'
                    z.p.p.color = 'red'
                    z = z.p.p
                else:
                    if z == z.p.left:
                        z = z.p
                        self.right_rotate(z)
                    z.p.color = 'black'
                    z.p.p.color = 'red'
                    self.left_rotate(z.p.p)
        self.root.color = 'black'

    def transplant(self, u, v):
        if u.p == self.nil:
            self.root = v
        elif u == u.p.left:
            u.p.left = v
        else:
            u.p.right = v
        v.p = u.p

        # the tree_minimum can not be used here
        # because the NIL is used with None
        # but here the NIL is use as the self.nil

    def minimum(self, x):
        while x.left != self.nil:
            x = x.left
        return x

    def delete(self, z):
        y = z
        y_original_color = y.color
        if z.left == self.nil:
            x = z.right
            self.transplant(z, z.right)
        elif z.right == self.nil:
            x = z.left
            self.transplant(z, z.left)
        else:
            y = self.minimum(z.right)
            y_original_color = y.color
            x = y.right
            if y.p == z:
                x.p = y
            else:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.p = y
            self.transplant(z, y)
            y.left = z.left
            y.left.p = y
            y.color = z.color
        if y_original_color == 'black':
            self.delete_fixup(x)

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


def build_node(key):
    return Node(key, left=nil, right=nil)


if __name__ == '__main__':
    t = RedBlackTree()
    for i in [3, 8]:
        t.insert(build_node(i))
    x = t.insert(build_node(1))
    for i in [0, 2, 4]:
        t.insert(build_node(i))
    y = t.insert(build_node(17))
    for i in [30, 33, 5]:
        t.insert(build_node(i))

    t.inorder_walk(t.root)

    print('=' * 100)
    t.delete(x)
    t.delete(y)
    t.inorder_walk(t.root)
