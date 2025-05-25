dati = open("dati.txt")
for line in dati:
    # print(line)
    # print(line.split())
    titolo = str(line.split(" ")[3:-2])
    print(" ".join(titolo))

dati.close()

parola = input("Che parola vuoi cercare?")
