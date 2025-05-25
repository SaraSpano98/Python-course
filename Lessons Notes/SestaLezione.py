# esercizio lancio 2 dadi

import random

while True:
    try:
        a = int(input('Immetti un numero intero tra 2 e 12 o -1 per uscire: '))

        if a == -1:
            print('Gioco finito')
            break
        elif 2 <= a <= 12:
            # simula 2 lanci di un dado a 6 facce
            num = random.randint(1, 6) + random.randint(1, 6)

            if a == num:
                print('hai indovinato: ' + str(a) + ' = ' + str(num))
                break
            else:
                print('non hai indovinato: ' + str(a) +
                      ' <> ' + str(num) + ', ritenta')
        else:
            print('Valore non accettabile, ritenta')

    except ValueError as e:
        print('Errore:', e, '- ritenta')
    except Exception:
        print('Valore non accettabile, ritenta')

# Lettura documentazione relativa ai moduli importati:
print('\nDocumentazione su librerie esterne:')
help(random)
print('----------------------------------------')
help(random.randint)
