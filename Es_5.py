import random


def main():

    try:
        num_partite = int(input("Quante partite vuoi giocare?"))
        if num_partite <= 0:
            print("Il numero di partite deve essere positivo.")
            return
    except ValueError:
        print("Devi inserire un numero intero valido.")
        return

    partite_giocate = 0
    while partite_giocate < num_partite:
        num1 = random.randint(0, 10)
        num2 = random.randint(1, 10)
        somma_corretta = num1 + num2

        try:
            risposta = int(
                input(
                    f"Indovina la somma di questi due numeri casuali: "
                    f"{num1} + {num2}"
                )
            )
            if risposta == somma_corretta:
                print("Complimenti! Hai indovinato!")
                break
            else:
                print("Peccato, risposta errata.")
        except ValueError:
            print("Devi inserire un numero intero valido.")

        partite_giocate += 1

    print("Grazie per aver giocato! Alla prossima!")


if __name__ == "__main__":
    main()
