import main

# SETUP
SimulationMode = False  # IF FALSE: PLOT MODE
######################
# If you are in simulation mode, put the parameters below
dim_array = 1000
switch = 2  # Scegli l'input: 0=Casuale 1=Invertito 2=Ordinato
algoritmo = "MergeSort"  # Scegli l'algoritmo tra (scrivi ESATTAMENTE): InsertionSort MergeSort
######################
if SimulationMode:
    main.simulate_n_save(dim_array, switch, algoritmo)
else:
    main.plot_mode(switch, algoritmo)
