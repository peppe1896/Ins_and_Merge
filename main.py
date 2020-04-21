from timeit import default_timer as timer
import array_creator as ac
import merge_sort as msort
import insertion_sort as isort

dim_array = 500
array = ac.create_inverted_array(dim_array)
tipo_input = "Invertito"  # Casuale Invertito Ordinato
algoritmo = "InsertionSort"  # InsertionSort MergeSort


print("N", dim_array, "valori di INPUT")
start = timer()
# msort.MergeSort(array)
array = isort.insertion_sort(array)
stop = timer()
delta = stop - start
print("Tempo Ins sort:", delta, "secondi. Input:", dim_array)

nome_file = "In="+str(dim_array)

# NON TOCCARE

out = open("./Test/"+tipo_input+"/"+algoritmo+"/"+nome_file+".txt", "w")
out.write(str(delta)+"\n\nAlgoritmo: "+algoritmo+"\nDimensione Input:"+str(dim_array)+"\nTempo impiegato ad ordinare:" + str(delta)+"\nInput:"+tipo_input)

out.close()
