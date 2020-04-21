import numpy as np


def get_sentinel(array):
    if len(array) != 0:
        max_s = max(array)
    else:
        max_s = 1000000
    return max_s + 1


def merge(arr, p, q, r):
    print("metgesord")
    L = arr[p:q]
    R = arr[q:r]
    i = j = 0
    L = np.append(L, 1000)
    R = np.append(R, 900)
    for k in range(p, r):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1


def merge_sort(arr, p, r):
    if p < r:
        q = (p + r)//2
        merge_sort(arr, p, q)
        merge_sort(arr, q+1, r)
        merge(arr, p, q, r)
    print("hello", arr)
