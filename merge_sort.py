import numpy as np


def get_sentinel(array):
    if len(array) != 0:
        max_s = max(array)
    else:
        max_s = 1000000
    return max_s + 1


def merge(arr, p, q, r):
    L = arr[p:q]
    R = arr[q:r + 1]
    L.append(get_sentinel(arr))
    R.append(get_sentinel(arr))
    i = j = 0
    for k in range(p, r+1):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1


def merge_sort(arr, p, r):
    if p < r:
        q = (r+p) // 2
        merge_sort(arr, p, q)
        merge_sort(arr, q + 1, r)
        merge(arr, p, q, r)
        print(arr)


def merge_work(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_work(L)
        merge_work(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
            print("\rMerging from "+str(k)+" to "+str(len(arr)), end="", flush=True)

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


def MergeSort(A):
    merge_work(A)
