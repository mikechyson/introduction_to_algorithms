class Element:
    def __init__(self, key, next=None, prev=None):
        self.key = key
        self.next = next
        self.prev = prev


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def search(self, k):
        x = self.head
        while x is not None and x.key != k:
            x = x.next
        return x

    def insert(self, x):
        x = Element(x)
        x.next = self.head
        if self.head is not None:
            self.head.prev = x
        self.head = x
        x.prev = None

    def delete(self, x):
        e = self.search(x)
        if e is not None:
            if e.prev is not None:
                e.prev.next = e.next
            else:
                self.head = e.next
            if e.next is not None:
                e.next.prev = e.prev
        else:
            print('No such element: {} !'.format(x))

    def __str__(self):
        x = self.head
        result = []
        while x is not None:
            result.append(x.key)
            x = x.next
        return str(result)


class LinkedList2:
    def __init__(self):
        self.nil = Element(None)
        self.nil.next = self.nil
        self.nil.prev = self.nil

    def search(self, k):
        x = self.nil.next
        while x != self.nil and x.key != k:
            x = x.next

        if x is self.nil:
            print('element {} not found!'.format(k))
        else:
            print('element {} found!'.format(k))

        return x

    def insert(self, x):
        x = Element(x)
        x.next = self.nil.next
        self.nil.next.prev = x
        self.nil.next = x
        x.prev = self.nil

    def delete(self, x):
        e = self.search(x)
        if e is not self.nil:
            e.prev.next = e.next
            e.next.prev = e.prev
            print('element {} deleted!'.format(x))
        else:
            print('No such element: {} !'.format(x))

    def __str__(self):
        x = self.nil.next
        result = []
        while x is not self.nil:
            result.append(x.key)
            x = x.next
        return str(result)


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert(4)
    ll.insert(5)
    print(ll)
    print(ll.search(5))
    print(ll.search(7))
    ll.delete(7)
    ll.delete(5)
    print(ll)
    print('=' * 100)

    ll = LinkedList2()
    ll.insert(4)
    ll.insert(5)
    print(ll)
    ll.search(5)
    ll.search(7)
    ll.delete(7)
    ll.delete(5)
    print(ll)
