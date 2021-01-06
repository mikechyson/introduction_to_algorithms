class ListFromOne(list):
    def __getitem__(self, item):
        return super().__getitem__(item - 1)

    def __setitem__(self, key, value):
        return super().__setitem__(key - 1, value)


if __name__ == '__main__':
    A = [1, 2, 3]
    A = ListFromOne(A)
    print(A[1])
    A[1]=10
    print(A)
