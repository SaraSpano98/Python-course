""" 
Abbiamo iniziato la lezione parlando di un concetto fondamentale in python, la differenza tra:
    1) Tipi mutable (che possono cambiare): Liste, Dizionari, Set, Classi, ecc.
    2) Tipi immutable (non possono cambiare): str, int, float, Tuple, ecc.
    
Ci siamo soffermati sul concetto di variabile per capire, cosa si intende con cambiare?
"""
# Da questo codice si potrebbe pensare che x stia "cambiando"
x = 10
x += 1
# Da un esame più approfondito però, ci accorgiamo che non è solo il "numero" che cambia, ma x stessa.
x = 10
print(f"x prima dell'incremento: {id(x)}")
x += 1
print(f"x dopo l'incremento: {id(x)}")

"""
La funzione id() in python, ci permette di vedere dove un elemento è posizionato in memoria,
ci dà il suo indirizzo in poche parole.
Questa è la fondamentale differenza tra un tipo mutable ed un tipo immutable:
    - Quando assegno un nuovo valore ad una variabile immutable ottengo una nuova variabile.
    - Quando lo faccio con un mutable, modifico la variabile stessa!
"""
lista = [1, 2, 3, 4]
print(f"lista prima del nuovo elemento: {id(lista)}")
lista.append(2)
print(f"x dopo il nuovo elemento: {id(lista)}")

"""
La domanda spontanea è chiaramente, a cosa mi serve saperlo?
La risposta è che:
    1) Ho bisogno di sapere che se modifico direttamente un mutable, non posso più avere l'originale!
    2) Ho bisogno di sapere che se passo un immutable in una funzione non posso cambiarlo!
"""
lista = [1, 2, 3, 4, 5, 6]
print(f"Questa è la lista originale: {lista}")
nuova_lista = lista
print(f"Questa è la nuova lista: {nuova_lista}")
# Qua potreste pensare che state modificando solo la nuova lista
# ma avete appena perso la lista originale modificandole entrambe
nuova_lista.append(10)
print(f"Nuova lista: {nuova_lista}")
print(f"Lista originale: {lista}")

""" Esempio con le funzioni """

def incrementa(numero):
    numero += 1
    
x = 10
print(f"x prima di incrementa: {x}")
incrementa(x)
print(f"x dopo incrementa: {x}")

def aggiungi_numero(lista, numero):
    lista.append(numero)
    return lista
    
lista = [1, 2, 3, 4, 5, 6]
print(f"lista prima di aggiungi_numero: {lista}")
# Qui avete appena perso la lista originale, non potrete più usarla
nuova_lista = aggiungi_numero(lista, 10)
print(f"lista dopo di aggiungi_numero: {lista}")
print(f"nuova_lista dopo di aggiungi_numero: {nuova_lista}")

"""
Prendendo ad esempio queste differenze abbiamo dato la definizione tra:
    - Procedure: non restituiscono un risultato! Fanno un'azione / modificano un oggetto.
    - Funzioni: restituiscono sempre un risultato
"""

# Esempio di funzione
def somma(a, b):
    return a + b

# esempio di procedura 
def scrivi_file(path, lista):
    fw = open(path, "w+")
    for parola in lista:
        # controllo se parola è una stringa, se non lo è devo trasformarla, write accetta solo str
        if not isinstance(parola, str):
            # altro esempio di funzione 
            parola = str(parola) # Perché non potete scrivere semplicemente str(parola)?
        fw.write(parola)
        fw.write("\n")
    fw.close()
    
# se assegnate il risultato di una funzione ad una procedura, salverete il valore in una variabile
a = 2
b = 4
s = somma(a, b)
print(s)
# se lo fate con una procedura non avrete niente, non c'è un risultato che ritorna!
scrittura = scrivi_file("./ciao.txt", [1, 2, 3, 4, 5])
print(scrittura) # None

"""
In python quando non c'è un return valore è implicito che sia None
Potete anche scrivere:

def procedura():
    return
    
oppure:

def procedura():
    return None
    
Ma sarebbe comunque ridondante, è implicito.
"""

""" Esercizi """
"""
# 1)

## Funzioni da implementare:
- aggiungi_studente(lista, nome)
- aggiungi_voto(lista, nome, voto)
- calcola_media(lista, nome)

## Requisiti:
- se uno studente esiste già, date un messaggio di errore ed uscite dal programma.

studenti = [
    ("primo", [7, 8]),
    ("secondo", [9, 10])
]
"""

"""
2)
### Calcolate il costo di un viaggio:

## L'utente può inserire le seguenti voci (ogni voce è un input):
    1. n° notti di soggiorno.
    2. città di arrivo.
    3. n° giorni noleggio macchina.
    
### Scrivete 3 funzioni per calcolare i costi:
    1. costo_hotel(notti_soggiorno, hotel_notti_costo);
    2. costo_aereo(citta_arrivo, citta_biglietto_costo);
    3. costo_macchina(giorni_noleggio, noleggio_giorni_costo);

### Dati Aggiuntivi: 
- hotel_notti_costo = [(1, 20), (2, 18), (3, 15), (4, 12)] (da 4 in poi è sempre 12) (si intende al giorno)
- citta_biglietto_costo = [("Los Angeles", 1000), ("New York", 1200), ("Las Vegas", 1400)]; 
- noleggio_giorni_costo = [(1, 20), (2, 18), (3, 15), (4, 12)] (si intende al giorno) (da 4 in poi, si paga una tassa aggiuntiva di 1.3 per ogni giorno in più)
- Potete dare per scontato che il costo massimo sia sempre l'ultimo elemento della lista.

### Requisiti:
- Fornite un menù all'utente dal quale possa inserire le variabili di input.
- Validate tutte le variabili, se l'utente sbaglia o il tipo non è giusto, si riparte da capo o da quello che ha sbagliato (come vi piace di più).
- Validate anche la città, DEVE essere tra quelle possibili.
- Il programma finisce quando l'utente ha inserito gli input ed a display si vede il prezzo totale del viaggio.

### Bonus (se non siete soddisfatti):
Scrivete una funzione: 
    - salva viaggio(notti_soggiorno, citta_arrivo, costo_macchina);
    
Questa salva il viaggio che l'utente ha scelto in un file come se fosse un "preventivo":

costo notti: {costo_notti}€ ({numero_notti} notti)
costo biglietto: {costo_aereo}€ ({citta_selezionata})
costo noleggio: {costo_noleggio}€ ({costo_noleggio})
----------------------------------------------------
costo totale: {costo_totale}€
"""