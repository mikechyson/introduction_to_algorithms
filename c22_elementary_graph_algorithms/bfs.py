import queue

vertices = {}


class Node:
    def __init__(self, vertex):
        self.vertex = vertex

    def __eq__(self, other):
        if self.vertex == other.vertex:
            return True
        else:
            return False

    def __hash__(self):
        return ord(self.vertex)

    def __str__(self):
        if self.__dict__['parent'] is not None:
            self.__dict__['parent'] = self.__dict__['parent'].vertex
        return str(self.__dict__)


def bfs(G, s):
    """
    Breadth first search
    :param G: an adjacency-list representation of graph
    :param s: source vertex in graph
    :return:
    """
    # init

    for u in G:
        if u != s:
            node = Node(u)
            node.color = 'white'
            node.d = 'infinity'
            node.parent = None
            vertices[u] = node
    s_node = Node(s)
    s_node.color = 'gray'
    s_node.d = 0
    s_node.parent = None
    vertices[s] = s_node

    # FIFO queue containing node value
    q = queue.Queue()
    q.put(s)

    while not q.empty():
        u = q.get()
        u_node = vertices[u]
        for v in G[u]:
            v_node = vertices[v]
            if v_node.color == 'white':
                v_node.color = 'gray'
                v_node.d = u_node.d + 1
                v_node.parent = u_node
                vertices[v] = v_node
                q.put(v)
        u_node.color = 'black'
        vertices[u] = u_node


def print_path(G, s, v):
    if v == s:
        print(s)
    elif vertices[v].parent is None:
        print('no path from {} to {} exists'.format(s, v))
    else:
        print_path(G, s, vertices[v].parent)
        print(v)


if __name__ == '__main__':
    G = {'s': list('rw'),
         'r': list('sv'),
         'v': list('r'),
         'w': list('stx'),
         't': list('wxv'),
         'x': list('wtuy'),
         'u': list('txy'),
         'y': list('xu')}
    s = 's'

    bfs(G, s)
    for v in vertices.values():
        print(v)
    # {'vertex': 'r', 'color': 'black', 'd': 1, 'parent': 's'}
    # {'vertex': 'v', 'color': 'black', 'd': 2, 'parent': 'r'}
    # {'vertex': 'w', 'color': 'black', 'd': 1, 'parent': 's'}
    # {'vertex': 't', 'color': 'black', 'd': 2, 'parent': 'w'}
    # {'vertex': 'x', 'color': 'black', 'd': 2, 'parent': 'w'}
    # {'vertex': 'u', 'color': 'black', 'd': 3, 'parent': 'x'}
    # {'vertex': 'y', 'color': 'black', 'd': 3, 'parent': 'x'}
    # {'vertex': 's', 'color': 'black', 'd': 0, 'parent': None}

    v = 'v'

    print_path(G, s, v)
