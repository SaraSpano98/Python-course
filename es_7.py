import random

# Funzione che genera una tupla di 6 numeri casuali


def generaTupla():
    tupla = tuple(random.randint(1, 100) for _ in range(6))
    return tupla

# Funzione per calcolare il massimo senza usare max()


def calcolaMassimo(tupla):
    massimo = tupla[0]
    for numero in tupla:
        if numero > massimo:
            massimo = numero
    return massimo

# Funzione per raccogliere l'anagrafica di 3 studenti


def raccogliAnagrafica():
    studenti = []
    for i in range(3):
        print(f"\nInserisci i dati dello studente {i+1}:")
        nome = input("Nome: ")
        cognome = input("Cognome: ")
        eta = int(input("Età: "))
        sesso = input("Sesso (M/F): ")
        studenti.append((nome, cognome, eta, sesso))
    return tuple(studenti)

# Funzione per calcolare l'età media


def calcolaEtaMedia(studenti):
    somma_eta = sum(studente[2] for studente in studenti)
    return somma_eta / len(studenti)

# --- Programma principale ---


# 1. Genera tupla e calcola massimo
numeri = generaTupla()
print("Tupla generata:", numeri)
massimo = calcolaMassimo(numeri)
print("Il valore massimo è:", massimo)

# 2. Raccogli e stampa anagrafica
studenti = raccogliAnagrafica()
print("\nAnagrafica degli studenti:")
for studente in studenti:
    print(studente)

# 3. Calcola età media
media_eta = calcolaEtaMedia(studenti)
print(f"\nEtà media degli studenti: {media_eta:.2f}")
