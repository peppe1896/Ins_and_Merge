import main

# SETUP
SimulationMode = True  # IF FALSE: PLOT MODE
switch = 0  # 0=Casuale 1=Invertito 2=Ordinato | 3=Tutti i plot dello stesso algoritmo
#           #  4-5-6 compara i due algoritmi in: RAND-INV-ORD
algoritmo = "MergeSort"  # InsertionSort | MergeSort
dim_array = 5000000  # For simulation
full = True


######################################################################
main.setup(SimulationMode, switch, algoritmo, dim_array, full=full)  #
######################################################################
