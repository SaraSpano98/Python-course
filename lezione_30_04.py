
from support import show_img1, show_img2

"""
Abbiamo parlato di nuovo di variabili in generale e ci siamo soffermati su come queste sono immagazzinate in memoria.
Vi ricordo che con memoria ci stiamo riferendo alla RAM del nostro computer!
"""

# Assegnazione (assegnazione + inizializzazione)
x = 5
y = 7

### Creare una variabile vuol dire inserire un valore da qualche parte in 
# memoria e salvare l'indirizzo di riferimento in un nome scelto da noi. 

#show_img1() # decommentate questa riga e lanciate il programma per vedere l'immagine

# Il risultato di questa assegnazione è che ora x ed y puntano alla stessa area di memoria
y = 5
y = 7
y = x
print(id(x))
print(id(y))
#show_img2() # decommentate questa riga e lanciate il programma per vedere l'immagine

"""
Questa è la vera definizione di variabili mutable e immutable.
Quando modifico una variabile immutable, mi viene restituita una nuova variabile che punta ad 
un indirizzo di memoria diverso (che contiene il nuovo valore assegnato).

Quando modifico una variabile mutable, mi viene restituito lo stesso indirizzo di memoria
ma con la variabile modificata.

Questo è il reale motivo per cui potete modificare una lista all'interno di una tupla.
"""
t = (1, 2.5, [1, 2, 3 , 4, 5])

t[0] = 1 # questo è sbagliato, dal punto di vista della tupla la state modificando
t[2][1] = 100 # questo è lecito, perchè dal punto di vista della tupla non la state modificando

"""
Perché?
Perché abbiamo definito cosa vuol dire modificare.
Modificare non vuol dire solo cambiare il valore di un variabile vuol dire cambiare il suo indirizzo!

In realtà la tupla non conserva il valore, come ci siamo detti, conserva indirizzi di memoria
Potete immaginarla così:
"""

a = 1
b = 2 
c = [1, 2, 3, 4]
t = (a, b, c) #--> t = (id(a), id(b), id(c))

"""
La tupla salva gli indirizzi delle variabili!

Come si accorge se una variabile cambia o meno?

Facile, se il suo indirizzo cambia la state cambiando, se il suo indirizzo non cambia non lo state facendo.

E allora, quando cambiate un intero all'interno di una tupla, state modificando il suo indirizzo, 
questa cosa non vale per un mutable, perché abbiamo visto che quando modificate un mutable il suo indirizzo non cambia!!
"""

"""
## Esecizio

#### In questo esercizio dovrete creare una programma che gestisca una libreria.

#### Create una lista vuota e chiamatela inventario:
- All'interno salverete i libri: liste contenenti [titolo, autore, numero_copie].
- Es: inventario = [[titolo1, autore1, 2], [titolo2, autore2, 0]]

#### Create una lista vuota e chiamatela prestiti
- All'interno salverete tuple del tipo: (nome_utente, [titolo_libro1, titolo_libro2])
- Es: prestiti = [(nome_utente1, [titolo1, titolo2]), (nome_utente2, [titolo1, titolo2])]

### Implementate le seguenti funzioni:

##### def aggiungi_libro(titolo, autore, numero_copie):
- numero copie non è obbligatorio, se non viene passato alla funzione vale 0 (lo sto creando ma non ho copie).
- se inserisco un libro con lo stesso titolo, semplicemente aumentano le copie.
- se le copie arrivano a 0, non elimino il libro!
- un libro con lo stesso titolo non può avere un autore diverso.

##### def presta_libro(nome_utente, titolo_libro):
- per prestare un libro devo averlo in inventario e devo avere almeno una copia, se non ce l'ho dico all'utente che può prenotarlo e riceverà una notifica quando arriva (questa non la implementiamo).
- ogni utente può avere al massimo un libro con lo stesso titolo.
- chiaramente se riesco a prestare il libro, il numero di copie in inventario decresce.

##### def restituisci_libro(nome_utente, titolo_libro):
- verificare che esista un utente con quel nome nella lista prestiti.
- verificare che l'utente abbia in prestito un libro con quel titolo.
- rimuovere il libro dalla lista prestiti relativa a quell'utente senza eliminare l'utente.
- chiaramente se restituisco un libro, il numero in inventario cresce.
- c'è un modo più efficiente per sapere se un utente esiste senza dover usare sempre la lista prestiti??

##### def stampa_libri_inventario()
- stampa tutti i libri che ho all'interno dell'inventario.

##### def stampa_libri_prestati()
- stampa i libri prestati per utente.
- per ogni riga viene visualizzato: nome_utente -> titolo1, titolo2, ....

##### def salva_stato_libreria(inventario, prestiti):
- salva all'interno di un file (o due, come volete) lo stato attuale di inventario e prestiti.
- scegliete voi il formato, a patto che poi possiate recuperarlo.

##### def recupera_stato_libreria(file):
- legge il/i file di stato che avete salvato e carica il contenuto nelle 2 liste (inventario e prestiti).


#### Create un menu per la gestione della libreria usando le varie opzioni.

#### Il programma deve essere persistente, tutte le volte che lo lancio deve prima provare a recuperare i dati dell'inventario e dei prestiti, se non trova niente, crea le due liste vuote.

#### Suggerimento: usate la funzione recupera_stato_libreria all'inizio del vostro programma per provare a caricare le 2 liste

#### N.B: Non c'è nessuna limitazione sul numero di funzioni che potete creare (per chi sa già come fare potete dividerli anche in moduli). Create quindi funzioni ausiliarie per rendere il codice più leggibile.

"""