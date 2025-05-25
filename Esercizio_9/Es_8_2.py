input = open("hours.txt")
for line in input:
    id, nome, lun, mar, mer, gio, ven = line.split()
ore = float(lun) + float(mar) + float(mer) + float(gio) + float(ven)

print(nome, "ID", id, "worked", ore, "ore:", ore/5, "/giorni")
