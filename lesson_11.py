def maxList(lista):
    max = lista[0]
    for item in lista:
        if item > max:
            max = item
    return max

number_list = [[-3, -4, -2, 23, -9],
               [2, 3, 6, 1, -3],
               [34, 2, 8, -45, 3]]

number_list_maxlist = []

for sottolista in number_list:
    number_list_maxlist.append(maxList(sottolista))

risultato = maxList(number_list_maxlist)

print(risultato)