def tronca(lista):
    if len(lista) >= 2:
        del lista[0]
        del lista[-1]
    elif len(lista) == 1:
        del lista[0]


dati = [10, 20, 30, 40]
tronca(dati)
print(dati)
print(tronca(dati))
