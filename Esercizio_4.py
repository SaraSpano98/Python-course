def leggi_ore(impiegato):
    giorni = int(input(f"Employee {impiegato}: How many days? "))
    ore_lavorate = []

    for _ in range(giorni):
        ore = float(input("Hours? "))
        ore_lavorate.append(min(ore, 8))
    return ore_lavorate


ore_impiegato1 = leggi_ore(1)
ore_impiegato2 = leggi_ore(2)
# legge le ore per i due impiegati

# Calcolo dei totali e delle medie
totale_1 = sum(ore_impiegato1)
totale_2 = sum(ore_impiegato2)

media_1 = totale_1/len(ore_impiegato1)
media_2 = totale_2/len(ore_impiegato2)

totale_complessivo = totale_1 + totale_2

# Risultati
print("\nEmployee 1's total hours =", totale_1, f"({media_1:.2f} / day)")
print("Employee 2's total hours =", totale_2, f"({media_2:.2f} / day)")
print("\nTotal hours for both =", totale_complessivo)
