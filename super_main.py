import main
import main_object as mo

# SETUP
simulation_mode = False  # IF FALSE: PLOT MODE
switch = 4  # 0=Casuale 1=Invertito 2=Ordinato | 3=Tutti i plot dello stesso algoritmo
#           # 4-5-6 compara i due algoritmi in: RAND-INV-ORD
algoritmo = "RadixSort"  # InsertionSort | MergeSort | QuickSort | RadixSort
dim_array = 500000
full = False  # Aggiungi valori di input
alg_da_comparare = "InsertionSort"  # Un secondo algoritmo da comparare con il primo algoritmo
is_obj = True  # Se vuoi usare le funzioni per ottenere la memoria consumata, e i grafici


def super_main_func():
    if is_obj:
        mo.setup(simulation_mode, dim_array, switch, algoritmo, alg_da_comparare)
    else:
        main.setup(simulation_mode, switch, algoritmo, alg_da_comparare, dim_array, full=full)


if __name__ == "__main__":
    super_main_func()
