# class FibonacciHeap:
#     pass
#
#
# class Node:
#     pass
#
#
# def make_fib_heap():
#     H = FibonacciHeap()
#     H.n = 0
#     H.min = None
#     H.root_list = []
#     return H


# def fib_heap_insert(H, x):
#     x.degree = 0
#     x.p = None
#     x.child = None
#     x.mark = False
#     if H.min is None:
#         # create a root list for H containing just x
#         H.root_list.append(x)
#         H.min = x
#     else:
#         # insert x into H's root list
#         H.root_list.append(x)
#         if x.key < H.min.key:
#             H.min = x
#     H.n = H.n + 1
