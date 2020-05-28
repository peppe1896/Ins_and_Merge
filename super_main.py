import main

# SETUP
SimulationMode = True  # IF FALSE: PLOT MODE
switch = 0  # 0=Casuale 1=Invertito 2=Ordinato | 3=Tutti i plot dello stesso algoritmo
#           # 4-5-6 compara i due algoritmi in: RAND-INV-ORD
algoritmo = "RadixSort"  # InsertionSort | MergeSort | QuickSort
dim_array = 50000  # For simulation
full = True
alg_da_comparare = "InsertionSort"

########################################################################################
main.setup(SimulationMode, switch, algoritmo, alg_da_comparare, dim_array, full=full)  #
########################################################################################
