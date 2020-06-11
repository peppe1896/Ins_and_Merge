import numpy as np


class radixsort(object):
    def __init__(self, A=None, B=None, place=None, size=None):
        self.A = A
        self.B = B
        self.C = None
        self.place = place
        self.size = size

    def counting_sort(self):
        C = np.zeros(10, dtype=int)
        for i in range(0, self.size):
            index = self.A[i] // self.place
            C[index % 10] += 1

        for i in range(1, 10):
            C[i] += C[i - 1]

        while i >= 0:
            index = self.A[i] // self.place
            self.B[C[index % 10] - 1] = self.A[i]
            C[index % 10] -= 1
            i -= 1

        for i in range(0, self.size):
            self.A[i] = self.B[i]
            self.B[i] = 0

    def radix_sort(self, A):
        self.A = A
        max_element = max(self.A)
        self.place = 1
        self.size = len(self.A)
        self.B = np.zeros(self.size, dtype=int)
        while max_element // self.place > 0:
            self.counting_sort()
            self.place *= 10

    def getsize(self):
        C = np.zeros(10, dtype=int)
        string = str(int(self.__sizeof__() + np.ndarray.__sizeof__(self.B) +
                       np.ndarray.__sizeof__(C)))
        string = string + "\nPeso array input: " + str(np.ndarray.__sizeof__(self.A))
        return string
