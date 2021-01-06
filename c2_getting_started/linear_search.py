def linear_search(lst, v):
    for i in range(len(lst)):
        if lst[i] == v:
            return i
    return None


lst = [1, 2, 5, 3, 6, 10, 44, 34, 22, 35, 21, 8]
v = 6
print(linear_search(lst, v))
v = 100
print(linear_search(lst, v))
