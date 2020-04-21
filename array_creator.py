import numpy as np


def create_rand_array(size, low_bound=-100, upp_bound=100):
    r = np.random.randint(low_bound, upp_bound, size)
    return r


def create_ordered_array(size):
    o = list()
    for j in range(size):
        o.append(int(j))
    return o


def create_inverted_array(size):
    u = list()
    for i in range(size):
        u.append(int(-i))
    return u
