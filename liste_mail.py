fname = input("Inserisci il nome del file: ")

try:
    with open(fname, 'r') as file:
        count = 0
        for line in file:
            line = line.strip()
            if line.startswith('From'):  # attenzione allo spazio dopo From
                parole = line.spilt()
                if len(parole) > 1:
                    print(parole[1])
                    count += 1
    print("Ci sono", count, "righe che iniziano con 'From'")
except FileNotFoundError:
    print("Il file non è stato trovato.")
