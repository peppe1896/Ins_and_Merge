import main
import main_object as mo

# SETUP
simulation_mode = True  # IF FALSE: PLOT MODE
switch = 0  # 0=Casuale 1=Invertito 2=Ordinato | 3=Tutti i plot dello stesso algoritmo
#           # 4-5-6 compara i due algoritmi in: RAND-INV-ORD
algoritmo = "InsertionSort"  # InsertionSort | MergeSort | QuickSort | RadixSort
dim_array = 80000
full = False
alg_da_comparare = "InsertionSort"
is_obj = True


def super_main_func():
    if is_obj:
        mo.setup(simulation_mode, dim_array, switch, algoritmo, alg_da_comparare)
    else:
        main.setup(simulation_mode, switch, algoritmo, alg_da_comparare, dim_array, full=full)


if __name__ == "__main__":
    super_main_func()
