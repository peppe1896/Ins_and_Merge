import numpy as np


class insertionsort(object):
    def __init__(self):
        self.A = None

    def insertion_sort(self, A):
        self.A = A
        for j in range(1, len(self.A)):
            key = self.A[j]
            i = j - 1
            while i >= 0 and self.A[i] > key:
                self.A[i + 1] = self.A[i]
                i -= 1
            self.A[i + 1] = key

    def getsize(self):
        string = str(int(self.__sizeof__()))
        string = string + "\nPeso array: " + str(np.ndarray.__sizeof__(self.A))
        return string
