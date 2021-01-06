class Node:
    def __init__(self, key, parent, left_child, right_sibling):
        self.key = key
        self.parent = parent
        self.left_child = left_child
        self.right_sibling = right_sibling


class RootedTree:
    def __init__(self, width=2):
        self.root = None
        self.width = width
