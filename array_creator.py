import numpy as np
import random
from timeit import default_timer as timer



def create_rand_array(size, low_bound=0, upp_bound=100):
    r = []
    start = timer()
    for i in range(size):
        r.append(random.randint(low_bound, upp_bound))
    end = timer()
    print("Temp creazione rand. array:", (end-start))
    return r


def create_ordered_array(size):
    o = []
    start = timer()
    for j in range(size):
        o.append(int(j))
    end = timer()
    print("Temp creazione ord. array:", (end-start))
    return o


def create_inverted_array(size):
    u = []
    start = timer()
    for i in range(size):
        u.append(int(-i))
    end = timer()
    print("Temp creazione inv. array:", (end-start))
    return u
