import numpy as np


def get_sentinel(array):
    if len(array) != 0:
        max_s = max(array)
    else:
        max_s = 1000000
    return max_s + 1


def merge(arr, p, q, r, sentinel):
    L = arr[p:q+1]
    R = arr[q+1:r + 1]
    L.append(sentinel)
    R.append(sentinel)
    i = j = 0
    for k in range(p, r+1):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1


def merge_sort(arr, p, r, sentinel):
    if p < r:
        q = (r+p) // 2
        merge_sort(arr, p, q, sentinel)
        merge_sort(arr, q + 1, r, sentinel)
        merge(arr, p, q, r, sentinel)


def MergeSort(A):
    merge_sort(A, 0, len(A)-1, get_sentinel(A))
