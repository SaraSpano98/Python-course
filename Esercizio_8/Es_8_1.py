def input_stats(file_path):
    with open(file_path, 'r') as file:
        longest = ""
        for line in file:
            line = line.rstrip('\n')
            if len(line) > len(longest):
                longest = line

    print("La linea più lunga è:", len(longest))
    print(longest)


input_stats("carroll.txt.txt")
