## Homework 3: Insertion Sort and Merge Sort
Questo Homework mostra quanto tempo è richiesto per eseguire un ordinamento in base a varie condizioni di input, 
sfruttando l'algoritmo **_Merge Sort_** e l'algoritmo **_InsertionSort_**. 
Sono salvati, nella cartella plot, gli andamenti dei vari casi visitati in una immagine formato png.

Per usare il programma:
Si avvia da **super_main.py**. Ci sono 3 impostazioni editabili, e cioè:
- **`SimulationMode`**: Se true, gli altri input verranno usati nella simulazione
- **`Switch`**: un intero da 0 a 6:
    - `0`: Ordinamento Casuale
    - `1`: Ordinamento Invertito
    - `2`: Ordinamento Ordinato
    - `3`: Grafico di tutti e 3 tipi di ordinamento
    - `4`: Compara Casuale di MSort con ISort
    - `5`: Compara Invertito di MSort con ISort
    - `6`: Compara Ordinato di MSort con ISort
    
    E' da far notare che `3` `4` `5` `6` valgono solamente per il plot. `0` `1` e `2` valgono per entrambi.

- **`Full`** (che è un boolean) se impostato su True, inserisce nei plot anche alcuni valori in più.

**Per aggiungere punti** al plot bisogna, **oltre che fare le simulazioni**, anche aggiungere dentro main.py i valori per i
quali si sta simulando. Es: Se voglio aggiungere al plot il risultato della simulazione 10, nel file main.py, 
più precisamente alla fine, dentro la funzione `plot_mode` e in **modo ordinato**, bisogna **aggiungere** anche il valore in **entrambe le liste**,
essendo quelle le liste che vanno a essere _plottate_.
