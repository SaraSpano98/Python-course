import os


def leggi_file(filename):
    with open(filename, "r", encoding="utf-8") as file:
        righe = file.readlines()
    # print(righe)
    return righe


def estrai_film_con_parola(righe, parola):
    risultati = []
#    print("parola="+parola)
#    print("righe="+str(righe))
    for riga in righe:
        #       print("dentro")
        print(riga)
        parti = riga.strip().split(maxsplit=3)  # Dividi in massimo 5 parti
#        print("len(parti)="+str(len(parti)))
        # if len(parti) < 5:
        #    #print("<5:"+ riga)
        #    continue
        _, voto, _, titolo_completo = parti[0], parti[1], parti[2], parti[3]
#        print("assegna!!!!")
#        print("posizione="+posizione)
#        print("voto="+voto)
#        print("visualizzazioni="+visualizzazioni)
#        print("titolo_completo="+titolo_completo)
        # print(titolo_completo)

        # Cerca la parola come sottostringa nel titolo completo
        # (in modo case insensitive)
        print("parola="+parola, "titolo="+titolo_completo)
        if parola.lower() in titolo_completo.lower():
            # Controlla se la parola è contenuta nel titolo
            risultati.append((titolo_completo, voto))
#            print("risultati="+str(risultati))
        else:
            print("saltato non selezionato")
#            print("risultati="+str(risultati))
    return risultati


def stampa_risultati(risultati):
    print("risultati="+str(risultati))
    if risultati:
        for titolo, voto in risultati:
            print(f"Titolo: {titolo}, Voto: {voto}")
    else:
        print("Nessun risultato trovato.")

# Algoritmo per ordinare una lista senza usare sort (Bubble Sort)


def ordina_lista(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista


def main():
    filename = "film.txt"

    # Assicurati che il percorso del file sia corretto
    percorso_file = os.path.join(os.path.dirname(__file__), filename)
    righe = []
    try:
        righe = leggi_file(percorso_file)
    except FileNotFoundError:
        print(f"Errore: il file {percorso_file} non esiste.")
        return

    parola = input(
        "Inserisci una parola da cercare nei titoli dei film: ").strip()
    risultati = estrai_film_con_parola(righe, parola)
    stampa_risultati(risultati)


if __name__ == "__main__":
    main()
