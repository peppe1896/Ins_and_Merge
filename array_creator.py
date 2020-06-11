import numpy as np
import random
from timeit import default_timer as timer


def create_rand_array(size, low_bound=0, upp_bound=10000):
    r = np.zeros(size, dtype=int)
    start = timer()
    for i in range(size):
        r[i] = random.randint(low_bound, upp_bound)
    end = timer()
    print("Temp creazione array (random):", (end-start), "secondi")
    return r


def create_ordered_array(size):
    o = np.zeros(size, dtype=int)
    start = timer()
    for j in range(size):
        o[j] = (int(j))
    end = timer()
    print("Temp creazione array (ordinato):", (end-start))
    return o


def create_inverted_array(size):
    u = np.zeros(size, dtype=int)
    start = timer()
    i = size - 1
    while i >= 0:
        u[i] = (int(i))
        i -= 1
    end = timer()
    print("Temp creazione array (invertito):", (end-start))
    return u
