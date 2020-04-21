from timeit import default_timer as timer
import array_creator as ac
import merge_sort as msort
import numpy as np
import insertion_sort as isort

dim_array = 10


sdd = timer()
#array = isort.insertion_sort(array)
dds = timer()
print("Tempo Insertion sort:", (dds - sdd), "secondi")

arraio = [81, 16, 2, 1616, 69]
print("arraio", arraio)
msort.merge_sort(arraio, 0, len(arraio)-1)
print(arraio)
