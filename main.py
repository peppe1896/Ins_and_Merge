from timeit import default_timer as timer
import array_creator as ac
import merge_sort as msort
import insertion_sort as isort
import datetime as dt

##############################################################################
#                         SEZIONE EDITABILE
dim_array = 1000
switch = 1  # Scegli l'input: 0=Casuale 1=Invertito 2=Ordinato
algoritmo = "MergeSort"  # Scegli l'algoritmo tra (scrivi ESATTAMENTE): InsertionSort MergeSort

# IL FILE DI RISULTATO E' in : ./Test/{TIPO_INPUT}/{ALGORITMO}/ e il file si chiama In={numInput}#
##############################################################################

tipo_input = ""
array = []
if switch == 0:
    print("Uso input CASUALE::", end=" ")
    tipo_input = "Casuale"  # Casuale Invertito Ordinato
    array = ac.create_rand_array(dim_array)
elif switch == 1:
    print("Uso input INVERTITO::", end=" ")
    tipo_input = "Invertito"
    array = ac.create_inverted_array(dim_array)
elif switch == 2:
    print("Uso input ORDINATO::", end=" ")
    tipo_input = "Ordinato"
    array = ac.create_ordered_array(dim_array)
else:
    print("DEFAULT INPUT TYPE: Random", end=" ")
    tipo_input = "Casuale"
    array = ac.create_rand_array(dim_array)

# NON TOCCARE
print("N", dim_array, "valori di INPUT")
orario_inizio = dt.datetime.now()
str_start = "Inizio:: " + str(orario_inizio.hour) + ":" + str(orario_inizio.minute) + ":" + str(orario_inizio.second)
print(str_start)
start = timer()
if algoritmo == "InsertionSort":
    print("Uso InsertionSort::", end=" ")
    array = isort.insertion_sort(array)
elif algoritmo == "MergeSort":
    print("Uso MergeSort::", end=" ")
    msort.MergeSort(array)
else:
    print("DEFAULT CASE: MergeSort -- ARRAY: RANDOM", end=" ")
    msort.MergeSort(array)
stop = timer()
delta = stop - start
print("\nTempo " + algoritmo + " :", delta, "secondi. Input:", dim_array)
orario_fine = dt.datetime.now()
str_end = "Fine:: "+ str(orario_fine.hour) + ":" + str(orario_fine.minute) + ":" + str(orario_fine.second)
print(str_end)
nome_file = "In=" + str(dim_array)
out = open("./Test/" + tipo_input + "/" + algoritmo + "/" + nome_file + ".txt", "w")
out.write(str(delta) + "\n\nAlgoritmo: " + algoritmo + "\nDimensione Input: " + str(
    dim_array) + "\nTempo impiegato ad ordinare: " +
          str(delta) + "\nInput: " + tipo_input + "\n")
out.write("Data " + str(orario_inizio.day) + "/" + str(orario_inizio.month) + "/" + str(orario_inizio.year))
out.write("\n\n"+str(str_start))
out.write("\n"+str(str_end))
out.close()
