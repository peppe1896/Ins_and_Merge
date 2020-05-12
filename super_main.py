import main

# SETUP
SimulationMode = True  # IF FALSE: PLOT MODE
switch = 2  # 0=Casuale 1=Invertito 2=Ordinato | 3=Tutti i plot dello stesso algoritmo
#           # 4-5-6 compara i due algoritmi in: RAND-INV-ORD
algoritmo = "QuickSort"  # InsertionSort | MergeSort | QuickSort
dim_array = 50000000  # For simulation
full = False
alg_da_comparare = "MergeSort"

########################################################################################
main.setup(SimulationMode, switch, algoritmo, alg_da_comparare, dim_array, full=full)  #
########################################################################################
