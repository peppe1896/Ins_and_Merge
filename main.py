from timeit import default_timer as timer
import array_creator as ac
import merge_sort as msort
import insertion_sort as isort
import datetime as dt
import plott as plt


def setup(is_simulation=False, switch=0, algoritmo="MergeSort", dim_array=10, full=False):
    if algoritmo == "MergeSort" or algoritmo == "InsertionSort":
        if is_simulation:
            if switch == 0 or switch == 1 or switch == 2:
                simulate_n_save(dim_array, switch, algoritmo)
            else:
                print("ERROR: invalid switch! Use 0, 1 or 2 for simulation.")
        else:
            if switch == 3:
                k = 0
                while k < 3:
                    plot_mode(k, algoritmo, full)
                    k += 1
            elif switch == 4:
                if algoritmo == "MergeSort":
                    algoritmo2 = "InsertionSort"
                    plot_mode(0, algoritmo, full)
                    plot_mode(0, algoritmo2, full, name=str(algoritmo) + "<->" + str(algoritmo2))
                elif algoritmo == "InsertionSort":
                    algoritmo2 = "MergeSort"
                    plot_mode(0, algoritmo, full)
                    plot_mode(0, algoritmo2, full, name=str(algoritmo)+"<->"+str(algoritmo2))
            else:
                plot_mode(switch, algoritmo, full)
            plt.print_plot()
    else:
        print('Errore: Non esiste nessun algoritmo '+ algoritmo+'. Input possibili: "MergeSort" oppure "InsertionSort')


def check_correctness(array):
    i = 0
    j = 1
    while i < len(array)-1:
        if array[j] < array[i]:
            return False
        i += 1
        j += 1
    return True


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
        print("ORDINATO?", check_correctness(array))
    elif switch == 1:
        print("Uso input INVERTITO::", end=" ")
        tipo_input = "Invertito"
        array = ac.create_inverted_array(dim_array)
        print("ORDINATO?", check_correctness(array))
    elif switch == 2:
        print("Uso input ORDINATO::", end=" ")
        tipo_input = "Ordinato"
        array = ac.create_ordered_array(dim_array)
        print("ORDINATO?", check_correctness(array))
    else:
        print("DEFAULT INPUT TYPE: Random", end=" ")
        tipo_input = "Casuale"
        array = ac.create_rand_array(dim_array)

    # Simula
    print("N", dim_array, "valori di INPUT")
    h_inizio = dt.datetime.now()
    str_start = "Inizio:: " + str(h_inizio.hour) + ":" + str(h_inizio.minute) + ":" + str(h_inizio.second)
    print("Il risultato sarà salvato in: ./Test/"+tipo_input+"/"+algoritmo+"/ e il file si chiama In="
          + str(dim_array)+".txt")
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
    str_end = "Fine:: " + str(h_fine.hour) + ":" + str(h_fine.minute) + ":" + str(h_fine.second)
    print(str_end)
    print("Verifico che il vettore sia ordinato...", end=" ")
    if check_correctness(array):
        print("Vettore ordinato.")
    else:
        print("Vettore non ordinato.")
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


def plot_mode(tipo_input, algoritmo, full, name=""):

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
        if not full:
            lista_input = [1000, 10000, 20000, 35000, 50000, 60000, 80000, 100000, 120000]
        else:
            lista_input = [1000, 10000, 20000, 35000, 50000, 60000, 80000, 100000, 1200000, 500000, 1200000,
                           5000000, 12000000, 25000000, 50000000]
        plt.draw_graphic(lista_input, tipo_input, algoritmo, name)
    elif algoritmo == "InsertionSort":
        lista_input = [1000, 10000, 20000, 35000, 50000, 60000, 80000, 100000, 120000]
        if tipo_input == "Ordinato" and full:
            lista_input.append(500000)
            lista_input.append(1200000)
            lista_input.append(5000000)
            lista_input.append(12000000)
            lista_input.append(25000000)
            lista_input.append(50000000)
        plt.draw_graphic(lista_input, tipo_input, algoritmo, name)
