# Input: Two n-bit binary integers, stored in two n-element arrays A and B
# Output: The sum of the two integers stored in binary form in an (n+1)-element array C


def binary_add(A, B):
    # print(A, B)
    carry = 0
    C = list(range(0, len(A) + 1))
    for i in reversed(range(0, len(A))):
        tmp = A[i] + B[i] + carry
        if tmp > 1:
            tmp = tmp - 2
            carry = 1
        else:
            carry = 0
        C[i + 1] = tmp
    C[0] = carry
    return C


list_a = [1, 0, 1, 0]
list_b = [1, 1, 0, 0]
print(binary_add(list_a, list_b))
# [1, 0, 1, 1, 0]


list_a = [1, 0, 1, 0, 1]
list_b = [1, 0, 0, 0, 1]
print(binary_add(list_a, list_b))
# [1, 0, 0, 1, 1, 0]
