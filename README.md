## Homework 3: Insertion Sort and Merge Sort
Questo Homework mostra quanto tempo è richiesto per eseguire un ordinamento in base a varie condizioni di input, 
sfruttando l'algoritmo **_Merge Sort_** e l'algoritmo **_InsertionSort_**. 
Sono salvati, nella cartella "_Plot_", gli andamenti dei vari casi visitati in una immagine formato png.
Nella cartella "_Test_" sono invece salvati i risultati dei vari test eseguiti, ordinati per algoritmo e tipo di input.

    Per usare il programma bisogna avviarlo da super_main.py, nel quale ci sono 3 flag da poter modificare:


- **`SimulationMode`**: Se true, gli altri input verranno usati nella simulazione
- **`Switch`**: un intero da 0 a 6:
    - `0`: Ordinamento Casuale
    - `1`: Ordinamento Invertito
    - `2`: Ordinamento Ordinato
    - `3`: Grafico di tutti e 3 tipi di ordinamento
    - `4`: Compara Casuale di _algoritmo1_ con _algoritmo2_
    - `5`: Compara Invertito di _algoritmo1_ con _algoritmo2_
    - `6`: Compara Ordinato di _algoritmo1_ con _algoritmo2_
    
    E' da far notare che `3` `4` `5` `6` valgono solamente per il plot. `0` `1` e `2` valgono per entrambi.

- **`Full`** (che è un boolean) se impostato su True, inserisce nei plot anche alcuni valori in più.

**Per aggiungere punti** al plot bisogna, **oltre che fare le simulazioni**, anche aggiungere dentro main.py i valori per i
quali si sta simulando. Es: Se voglio aggiungere al plot il risultato della simulazione 10, nel file main.py, 
più precisamente alla fine, dentro la funzione `plot_mode` e in **modo ordinato**, bisogna **aggiungere** anche il valore in **entrambe le liste**,
essendo quelle le liste che vanno a essere _plottate_.

**NUOVA AGGIUNTA.**

**`AGGIUNGERE ALTRI ALGORITMI/LAVORARE SU QUELLI ESISTENTI`**
Questo programma è scritto in modo molto basilare da una persona che di esperienza non ne ha. Quindi per chiunque, compreso lui
stesso, questo programma risulta indecifrabile. Ma in un momento di lucidità, ho deciso di scrivermi 2 righe per il me 
futuro che vorra aggiungere altri algoritmi o modificare i plot.

**_Aggiunta di un algoritmo nuovo:_**
- Crea un file di .py in cui ci metti il codice. Crea anche una funzione semplificata che lanci l'algoritmo.
- Includi dentro **main.py** questo file e modifica le seguenti funzioni:
    - Modifica la funzione `setup`: 
        - Aggiungi nel _PRIMO_ `if` il nome dell'algoritmo
    - Modifica la funzione `simulate_n_save`:
        - Nella parte "**Simula**", che si trova dopo il primo blocco di switch (quello che crea l'input), aggiungi un elif 
        e completalo come gli altri.
        - Nella parte  "**Salva su file**" non fare niente, ma crea una cartella in _Test/_ con il nome dell'algoritmo e 3 
        sottocartelle "_Ordinato_" "_Invertito_" "_Ordinato_"
    - Modifica la funzione `plot_mode` aggiungendo, nel caso volessi, altri input oltre a quelli di base, o in generale
    se avessi bisogno di altre info particolari per l'algoritmo in questione
- Ora vai su **plott.py**:
    - Modifica la funzione `draw_graphic` aggiungendo nell'else il nome dell'algoritmo nuovo e impostando 
    colori e marker