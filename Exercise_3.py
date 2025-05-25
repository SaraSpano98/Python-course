# ESERCIZIO 1
for i in range(10):
    print(i)

# ESERCIZIO 2


def numeri():
    for i in range(8):
        print(i+1)


for _ in range(2):
    numeri()

# ESERCIZIO 3


def numbers(n=1, m=10):
    for i in range(n, m + 1):
        print(i)


print()

MIN = 5  # variabili globali
MAX = 25

numbers(2, 9)
numbers()
numbers(3)
numbers(m=18)
numbers(MIN, MAX)
