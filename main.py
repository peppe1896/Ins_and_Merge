from timeit import default_timer as timer
import array_creator as ac
import merge_sort as msort
import insertion_sort as isort

#                       SEZIONE EDITABILE
##############################################################################

dim_array = 123
switch = 0  # 0=Casuale 1=Invertito 2=Ordinato
algoritmo = "InsertionSort"  # InsertionSort MergeSort

##############################################################################
#                       SEZIONE NON EDITABILE
tipo_input = ""
array = []
if switch == 0:
    tipo_input = "Casuale"  # Casuale Invertito Ordinato
    array = ac.create_rand_array(dim_array)
elif switch == 1:
    tipo_input = "Invertito"
    array = ac.create_inverted_array(dim_array)
elif switch == 2:
    tipo_input = "Ordinato"
    array = ac.create_ordered_array(dim_array)
else:
    print("DEFAULT INPUT TYPE: Random")
    tipo_input = "Casuale"
    array = ac.create_rand_array(dim_array)

# NON TOCCARE
print("N", dim_array, "valori di INPUT")
start = timer()
if algoritmo == "InsertionSort":
    array = isort.insertion_sort(array)
elif algoritmo == "MergeSort":
    msort.MergeSort(array)
else:
    print("DEFAULT CASE: MergeSort -- ARRAY: RANDOM")
    msort.MergeSort(array)
stop = timer()
delta = stop - start
print("Tempo "+algoritmo+" :", delta, "secondi. Input:", dim_array)

nome_file = "In="+str(dim_array)
out = open("./Test/"+tipo_input+"/"+algoritmo+"/"+nome_file+".txt", "w")
out.write(str(delta)+"\n\nAlgoritmo: "+algoritmo+"\nDimensione Input: "+str(dim_array)+"\nTempo impiegato ad ordinare: " +
          str(delta)+"\nInput: "+tipo_input)

out.close()
