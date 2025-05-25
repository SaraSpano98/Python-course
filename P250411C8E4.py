def createWordDatabase(filename):
    with open(filename, 'r') as file:
        file_lines = file.readlines()
    unique_words = []
    for line in file_lines:
        line = line.split()
        for word in line:
            word_match = False
            if len(unique_words) != 0:
                for second_word in unique_words:
                    if word == second_word:
                        word_match = True
            if not word_match:
                unique_words.append(word)
    return unique_words


def orderListAZ(list):
    list_length = len(list)
    sorted = False
    while not sorted:
        sorted = True
        for i in range(list_length-1):
            if list[i] > list[i+1]:
                list[i], list[i+1] = list[i+1], list[i]
                sorted = False
    return list


print(orderListAZ(createWordDatabase("romeo.txt")))
