from introduction_to_algorithms.c22_elementary_graph_algorithms.bfs import Node

vertices = {}
time = 0


def dfs(G):
    for u in G:
        node = Node(u)
        node.color = 'white'
        node.parent = None
        vertices[u] = node

    for u in G:
        u_node = vertices[u]
        if u_node.color == 'white':
            dfs_visit(G, u)


def dfs_visit(G, u):
    global time
    time = time + 1
    u_node = vertices[u]
    u_node.d = time
    u_node.color = 'gray'

    for v in G[u]:
        v_node = vertices[v]
        if v_node.color == 'white':
            v_node.parent = u_node
            vertices[v] = v_node
            dfs_visit(G, v)
    u_node.color = 'black'
    time = time + 1
    u_node.f = time
    vertices[u] = u_node


if __name__ == '__main__':
    G = {
        'u': list('vx'),  # u should be the first element
        'x': list('v'),
        'v': list('y'),
        'y': list('x'),
        'w': list('yz'),
        'z': list('z')
    }
    dfs(G)
    for v in vertices.values():
        print(v)
    # {'vertex': 'u', 'color': 'black', 'parent': None, 'd': 1, 'f': 8}
    # {'vertex': 'x', 'color': 'black', 'parent': 'y', 'd': 4, 'f': 5}
    # {'vertex': 'v', 'color': 'black', 'parent': 'u', 'd': 2, 'f': 7}
    # {'vertex': 'y', 'color': 'black', 'parent': 'v', 'd': 3, 'f': 6}
    # {'vertex': 'w', 'color': 'black', 'parent': None, 'd': 9, 'f': 12}
    # {'vertex': 'z', 'color': 'black', 'parent': 'w', 'd': 10, 'f': 11}
