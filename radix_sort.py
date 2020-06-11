import numpy as np


def counting_sort(A, B, place, size):
    C = np.zeros(10, dtype=int)
    for i in range(0, size):
        index = A[i] // place
        C[index % 10] += 1

    for i in range(1, 10):
        C[i] += C[i - 1]

    while i >= 0:
        index = A[i] // place
        B[C[index % 10] - 1] = A[i]
        C[index % 10] -= 1
        i -= 1

    for i in range(0, size):
        A[i] = B[i]
        B[i] = 0


def radix_sort(A):
    max_element = max(A)
    place = 1
    size = len(A)
    B = np.zeros(size, dtype=int)
    while max_element // place > 0:
        counting_sort(A, B, place, size)
        place *= 10