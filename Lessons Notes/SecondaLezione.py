# FUNZIONI
# si costruiscono con DEF, Esempio
# def name
#   statement
#   statement
# LE INDENTAZIONI SONO QUEI BLOCCHI DI CODICE INVECE DI {},

# IN PYTHON INVECE è OBBLIGATORIO L'INDENTAZIONE

# def con return sono FUNZIONI PRODUTTIVE

# Anche Python è Camel CaSe:  quindi nella variabile la 1° parola è minuscola,

# la 2° è la 1° lettera è in MAIUSCOLO
# I primi operatori sono uguali a Javascript,
# quelli particolari invece qui in Python non ci sono.
# Al massimo soltanto gli operatori di assegnazione.
# Nelle Variabili non si scrive il tipo e non esistono gli operatori: ++ & --.

# Per il tipo di variabile, scrivere: type(nomevariabile)...

# in javascript si fa con Typeof.  Di questi ci sono: int(numeri interi),

# float(numeri con la virgola) e str(stringa)

# Le stringhe Python possono essere moltiplicate per un valore intero
# Interi e stringhe non si possono concatenare, quindi,

# usare str(value) per CONVERTIRE IL VALORE IN STRINGA

# Oppure... PRINT(EXPR, EXPR) in modo da concatenare
# il tutto all'interno della variabile
# E' presente il ciclo for... esempio:
# for i in range(5):               for i in range(5):
# print("1");   oppure....         print(i);

for line in range(1, 6):
    print((5 - line) * "." + str(line))
