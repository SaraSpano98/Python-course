parola = input("Inserisci una parola da cercare nel titolo del film: ").lower()

trovato = False

with open("dati.txt", "r") as file:
    for riga in file:
        parti = riga.strip().split(maxsplit=3)
        punteggio = parti[1]
        titolo = parti[3]
        if parola in titolo.lower():
            print(f"Titolo: {titolo}, Punteggio: {punteggio}")
            trovato = True

if not trovato:
    print("Titolo non trovato")
