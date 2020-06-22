#  seconda versione del main che prende in ingresso gli oggetti che contengono i metodi per ordinare i vettori contenuti
#  dentro gli oggetti stessi

from timeit import default_timer as timer
import plott as plot
import insertion_sort_obj as iso
import radix_sort_obj as rso
import array_creator as ac
import datetime as dt


def setup(simul, dim, switch, algoritmo, algoritmo2):
    if simul:
        if switch == 0 or switch == 1 or switch == 2:
            simulate_n_save(dim, switch, algoritmo)
        else:
            print("ERROR: invalid switch! Use 0, 1 or 2 for simulation.")
    else:
        if switch == 3:  # Tutti i grafici dello stesso algoritmo
            k = 0
            while k < 3:
                plot_mode(k, algoritmo, name="")
                k += 1
        elif switch == 4:  # Compara 2 algoritmi su input CASUALE
            plot_mode(0, algoritmo, name=str(algoritmo) + "<->" + str(algoritmo2))
            plot_mode(0, algoritmo2, name=str(algoritmo) + "<->" + str(algoritmo2))
        elif switch == 5:  # Compara 2 algoritmi su input INVERTITO
            plot_mode(1, algoritmo, name=str(algoritmo) + "<->" + str(algoritmo2))
            plot_mode(1, algoritmo2, name=str(algoritmo) + "<->" + str(algoritmo2))
        elif switch == 6:  # Compara 2 algoritmi su input ORDINATO
            plot_mode(2, algoritmo, name=str(algoritmo) + "<->" + str(algoritmo2))
            plot_mode(2, algoritmo2, name=str(algoritmo) + "<->" + str(algoritmo2))
        else:
            plot_mode(switch, algoritmo, name=str(algoritmo))  # Stampa solo il grafico per l'input corrente.
        plot.print_plot()


def simulate_n_save(dim_array=10, switch=0, algoritmo="InsertionSort"):
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

    print("-", dim_array, "valori di INPUT")
    h_inizio = dt.datetime.now()
    str_start = "Inizio:: " + str(h_inizio.hour) + ":" + str(h_inizio.minute) + ":" + str(h_inizio.second)
    print("Save in: ./Test/ObjRes/" + algoritmo + "/" + tipo_input + "/ e il file si chiama Obj_In-"
          + str(dim_array) + ".txt")
    print(str_start)
    if algoritmo == "InsertionSort":
        print("Uso InsertionSort::", end=" ")
        obj = iso.insertionsort()
        start = timer()
        obj.insertion_sort(array)

    elif algoritmo == "RadixSort":
        print("Uso RadixSort::", end=" ")
        obj = rso.radixsort()
        start = timer()
        obj.radix_sort(array)
    else:
        print("NESSUN ALGORITMO SELEZIONATO", end=" ")
        start = timer()
    stop = timer()
    delta = stop - start
    print("\nTempo " + algoritmo + " :", delta, "secondi. Input:", dim_array)
    h_fine = dt.datetime.now()
    str_end = "Fine:: " + str(h_fine.hour) + ":" + str(h_fine.minute) + ":" + str(h_fine.second)
    print(str_end)

    ############################
    # Parte II : SALVA SU FILE #
    ############################

    nome_file = "Obj_In-" + str(dim_array)
    out = open("./Test/ObjRes/" + algoritmo + "/" + tipo_input + "/" + nome_file + ".txt", "w")
    out.write(obj.getsize() + "\n\nAlgoritmo: " + algoritmo + "\nDimensione Input: " + str(
        dim_array) + "\nTempo impiegato ad ordinare: " +
              str(delta) + "\nInput: " + tipo_input + "\n")
    out.write("Data " + str(h_inizio.day) + "/" + str(h_inizio.month) + "/" + str(h_inizio.year))
    out.write("\n\n" + str(str_start))
    out.write("\n" + str(str_end))
    out.close()


def plot_mode(tipo_input, algoritmo, name):
    lista_input = [1000, 10000, 20000, 35000, 50000, 60000, 80000, 100000, 120000]  # lista valori asse X

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
    plot.draw_graphic(lista_input, tipo_input, algoritmo, name, object=True)
