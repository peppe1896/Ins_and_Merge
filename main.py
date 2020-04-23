from timeit import default_timer as timer
import array_creator as ac
import merge_sort as msort
import insertion_sort as isort
import datetime as dt
import plott as plt


def simulate_n_save(dim_array=10, switch=0, algorithm="MergeSort"):
    ####################
    # Parte I : SIMULA #
    ####################

    # Imposta algoritmo da usare
    algoritmo = algorithm

    # Crea il vettore da ordinare usando dim e tipo di array
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

    # Simula
    print("N", dim_array, "valori di INPUT")
    h_inizio = dt.datetime.now()
    str_start = "Inizio:: " + str(h_inizio.hour) + ":" + str(h_inizio.minute) + ":" + str(h_inizio.second)
    print("Il risultato sarà salvato in: ./Test/"+tipo_input+"/"+algoritmo+"/ e il file si chiama In="+str(dim_array))
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
    h_fine = dt.datetime.now()
    str_end = "Fine:: "+ str(h_fine.hour) + ":" + str(h_fine.minute) + ":" + str(h_fine.second)
    print(str_end)

    ############################
    # Parte II : SALVA SU FILE #
    ############################

    nome_file = "In=" + str(dim_array)
    out = open("./Test/" + tipo_input + "/" + algoritmo + "/" + nome_file + ".txt", "w")
    out.write(str(delta) + "\n\nAlgoritmo: " + algoritmo + "\nDimensione Input: " + str(
        dim_array) + "\nTempo impiegato ad ordinare: " +
              str(delta) + "\nInput: " + tipo_input + "\n")
    out.write("Data " + str(h_inizio.day) + "/" + str(h_inizio.month) + "/" + str(h_inizio.year))
    out.write("\n\n"+str(str_start))
    out.write("\n"+str(str_end))
    out.close()


def plot_mode(tipo_input, algoritmo):

    if tipo_input == 0:
        print("Uso input CASUALE::")
        tipo_input = "Casuale"
    elif tipo_input == 1:
        print("Uso input INVERTITO::")
        tipo_input = "Invertito"
    elif tipo_input == 2:
        print("Uso input ORDINATO::")
        tipo_input = "Ordinato"
    else:
        print("DEFAULT INPUT TYPE: Random")
        tipo_input = "Casuale"

    print("Plotting:", str(tipo_input) + ", generato da " + str(algoritmo))
    if algoritmo == "MergeSort":
        lista_input = [1000, 10000, 20000, 50000, 60000, 100000, 120000, 500000,
                       1200000, 5000000, 12000000, 25000000, 50000000]
        plt.draw_graphic(lista_input, tipo_input, algoritmo)
    elif algoritmo == "InsertionSort":
        lista_input = [1000, 10000, 20000, 50000, 60000, 100000, 120000]
        plt.draw_graphic(lista_input, tipo_input, algoritmo)
