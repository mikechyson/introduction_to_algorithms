class Node:
    def __init__(self, key, satellite=None):
        self.key = key
        self.satellite = satellite


class DirectAddressTable:
    def __init__(self, length):
        self.length = length
        self.array = [None] * self.length

    def search(self, k):
        return self.array[k]

    def insert(self, x):
        self.array[x.key] = x

    def delete(self, x):
        self.array[x.key] = None

    def __str__(self):
        return str(self.array)


if __name__ == '__main__':
    d = DirectAddressTable(10)
    print(d)
    print('=' * 100)

    d.insert(Node(5))
    d.insert(Node(8))
    print(d)
    print('=' * 100)

    d.delete(Node(5))
    print(d)
