def insertion_sort(A):
    len_A = len(A)
    for j in range(1, len(A)):
        key = A[j]
        i = j - 1
        while i >= 0 and A[i] > key:
            A[i + 1] = A[i]
            i -= 1
        A[i + 1] = key
        print("\rInput "+str(j+1)+" on "+str(len_A), end="")
    print("\n")
    return A
