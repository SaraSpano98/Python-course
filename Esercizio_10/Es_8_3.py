# Dati di esempio
data_string = """
8.20 3.81 3/21/11
8.08 3.84 3/28/11
8.38 3.92 4/4/11
"""

lines = data_string.strip().split('\n')  # Divide in righe

# Inizializza le liste
prezzi_USA = []
prezzi_Belgio = []

for line in lines:
    parts = line.split()
    if len(parts) == 3:
        prezzo_USA = float(parts[0])
        prezzo_Belgio = float(parts[1])
        prezzi_USA.append(prezzo_USA)
        prezzi_Belgio.append(prezzo_Belgio)

# Calcola le medie
media_USA = sum(prezzi_USA) / len(prezzi_USA)
media_Belgio = sum(prezzi_Belgio) / len(prezzi_Belgio)

# Visto che ora ho ottenuto la media dei prezzi sia per gli USA e per il
# Belgio, devo andarli ad inserire all'interno del file "gasout.txt":

# Salva su file
with open("gasout.txt", "w") as file:
    file.write(f"Media USA: {media_USA:.2f}\n")
    file.write(f"Media Belgio: {media_Belgio:.2f}\n")

print("File creato con successo!")
