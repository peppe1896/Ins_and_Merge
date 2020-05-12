import random as rand


def swap_list(A, i, j):
    A[i], A[j] = A[j], A[i]


def partition(A, p, r):
    pivot = A[r]
    i = p-1
    for j in range(p, r):
        if A[j] <= pivot:
            i += 1
            swap_list(A, i, j)
    swap_list(A, i+1, r)
    return i + 1


def quicksort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quicksort(A, p, q-1)
        quicksort(A, q+1, r)


def randomized_quicksort(A, p, r, counting):
    if p < r:
        counting += 1
        q = randomized_partition(A, p, r)
        randomized_quicksort(A, p, q-1, counting)
        randomized_quicksort(A, q+1, r, counting)
    # else:
        # print("Totale funzioni ricorsive chiamate:", counting)


def randomized_partition(A, p, r):
    swap_list(A, p, rand.randint(p, r))
    return partition(A, p, r)


def call_quicksort(A):
    randomized_quicksort(A, 0, len(A)-1, 0)
