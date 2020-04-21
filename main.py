from timeit import default_timer as timer
import array_creator as ac
import merge_sort as msort
import numpy as np
import insertion_sort as isort

dim_array = 10
array = [11, 3, 18, 16, 1]
array_Asd = ac.create_rand_array(3)
print("RANDOM ARRAY", array_Asd)
print("random array ele", array_Asd[0])
B = ac.create_ordered_array(dim_array)
C = ac.create_inverted_array(dim_array)

sdd = timer()
#array = isort.insertion_sort(array)
print(array)
dds = timer()
print("Tempo Insertion sort:", (dds - sdd), "secondi")

arraio = np.array([3,2,1,4,7,5,6])
print("arraio", arraio)
msort.merge_sort(arraio, 0, len(arraio) -1 )
print(arraio)
