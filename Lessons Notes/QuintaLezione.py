def invertstr1(testo):
    testo2 = ""
    for ii in range(-1, -1 * len(testo) - 1, -1):
        testo2 = testo2 + testo[ii]
    return testo2


def invertstr2(testo):
    testo2 = ""
    for ii in testo:
        testo2 = ii + testo2
    return testo2.capitalize()


print(invertstr2(input("Inserisci una stringa da invertire: ")))
