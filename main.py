from timeit import default_timer as timer
import array_creator as ac
import merge_sort as msort
import insertion_sort as isort

dim_array = 10000
ordered = ac.create_ordered_array(dim_array)
tipo_input = "ORDINATO"
# rand_array = ac.create_rand_array(dim_array, -dim_array, dim_array)
print("N ", dim_array, " valori di INPUT")
start = timer()
msort.MergeSort(ordered)
#array = isort.insertion_sort(ordered)
stop = timer()
delta = stop - start
print("Tempo Ins sort:", delta, "secondi. Input:", dim_array)
nome_file = "ins_sort"+"--Ord--N="+str(dim_array)
out = open(nome_file+".txt", "w")
out.write("Algoritmo: INSERTION SORT.\n\nINPUT="+str(dim_array)+"\n\n"+"Tempo impiegato ad ordinare:" + str(delta)+"\n\nL'input è "+tipo_input)

out.close()
