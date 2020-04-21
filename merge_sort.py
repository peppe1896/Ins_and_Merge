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


def merge_work(arr):  # online
    if len(arr) > 1:
        mid = len(arr) // 2  # Finding the mid of the array
        L = arr[:mid]  # Dividing the array elements
        R = arr[mid:]  # into 2 halves

        merge_work(L)  # Sorting the first half
        merge_work(R)  # Sorting the second half

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
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
