from timeit import default_timer as timer
import array_creator as ac
import merge_sort as msort
import insertion_sort as isort
import datetime as dt
import plott as plt
import quick_sort as qsort
import radix_sort as rsort


def setup(is_simulation=False, switch=0, algoritmo="MergeSort", algoritmo2="InsertionSort", dim_array=10, full=False):
    if algoritmo == "MergeSort" or algoritmo == "InsertionSort" or algoritmo == "QuickSort" or algoritmo == "RadixSort":
        if is_simulation:
            if switch == 0 or switch == 1 or switch == 2:
                simulate_n_save(dim_array, switch, algoritmo)
            else:
                print("ERROR: invalid switch! Use 0, 1 or 2 for simulation.")
        else:
            if switch == 3:  # Tutti i grafici dello stesso algoritmo
                k = 0
                while k < 3:
                    plot_mode(k, algoritmo, full)
                    k += 1
            elif switch == 4:  # Compara 2 algoritmi su input CASUALE
                plot_mode(0, algoritmo, full, name=str(algoritmo) + "<->" + str(algoritmo2))
                plot_mode(0, algoritmo2, full, name=str(algoritmo) + "<->" + str(algoritmo2))
            elif switch == 5:  # Compara 2 algoritmi su input INVERTITO
                plot_mode(1, algoritmo, full, name=str(algoritmo) + "<->" + str(algoritmo2))
                plot_mode(1, algoritmo2, full, name=str(algoritmo) + "<->" + str(algoritmo2))
            elif switch == 6:  # Compara 2 algoritmi su input ORDINATO
                plot_mode(2, algoritmo, full, name=str(algoritmo) + "<->" + str(algoritmo2))
                plot_mode(2, algoritmo2, full, name=str(algoritmo) + "<->" + str(algoritmo2))
            else:
                plot_mode(switch, algoritmo, full)  # Stampa solo il grafico per l'input corrente.
            plt.print_plot()
    else:
        print(
            'Errore: Non esiste nessun algoritmo ' + algoritmo + '. Input possibili: "MergeSort" | "InsertionSort" |'
                                                                 ' "QuickSort" | "RadixSort')


def check_correctness(array):
    i = 0
    j = 1
    while i < len(array) - 1:
        if abs(array[j]) < abs(array[i]):
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
    # #######
    # Simula
    # #######
    print("N", dim_array, "valori di INPUT")
    h_inizio = dt.datetime.now()
    str_start = "Inizio:: " + str(h_inizio.hour) + ":" + str(h_inizio.minute) + ":" + str(h_inizio.second)
    print("Il risultato sarà salvato in: ./Test/" + algoritmo + "/" + tipo_input + "/ e il file si chiama In="
          + str(dim_array) + ".txt")
    print(str_start)
    start = timer()
    if algoritmo == "InsertionSort":
        print("Uso InsertionSort::", end=" ")
        array = isort.insertion_sort(array)
    elif algoritmo == "MergeSort":
        print("Uso MergeSort::", end=" ")
        msort.MergeSort(array)
    elif algoritmo == "QuickSort":
        print("Uso QuickSort::", end=" ")
        qsort.call_quicksort(array)
    elif algoritmo == "RadixSort":
        print("Uso RadixSort::", end=" ")
        rsort.radix_sort(array)
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
        print(array)
    ############################
    # Parte II : SALVA SU FILE #
    ############################

    nome_file = "In=" + str(dim_array)
    out = open("./Test/" + algoritmo + "/" + tipo_input + "/" + nome_file + ".txt", "w")
    out.write(str(delta) + "\n\nAlgoritmo: " + algoritmo + "\nDimensione Input: " + str(
        dim_array) + "\nTempo impiegato ad ordinare: " +
              str(delta) + "\nInput: " + tipo_input + "\n")
    out.write("Data " + str(h_inizio.day) + "/" + str(h_inizio.month) + "/" + str(h_inizio.year))
    out.write("\n\n" + str(str_start))
    out.write("\n" + str(str_end))
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
    lista_input = [1000, 10000, 20000, 35000, 50000, 60000, 80000, 100000, 120000]  # Base list

    if full and algoritmo == "MergeSort":
        lista_input.append(500000)
        lista_input.append(1200000)
        lista_input.append(5000000)
        lista_input.append(25000000)
        lista_input.append(50000000)
    elif algoritmo == "QuickSort":
        if full and tipo_input != "Ordinato":
            lista_input.append(500000)
            lista_input.append(1200000)
            lista_input.append(5000000)
            lista_input.append(25000000)
            lista_input.append(50000000)
        else:
            print("work in progress: INSERISCI QUI LA LISTA DEI VALORI PER QUICKSORT ORDINATO")
    elif algoritmo == "InsertionSort":
        if tipo_input == "Ordinato" and full:
            lista_input.append(500000)
            lista_input.append(1200000)
            lista_input.append(5000000)
            lista_input.append(12000000)
            lista_input.append(25000000)
            lista_input.append(50000000)
    plt.draw_graphic(lista_input, tipo_input, algoritmo, name)
