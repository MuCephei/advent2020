with open('input.txt', 'r') as file:
    for line in file.readlines():
        line = line.strip("\n")
        print("%s!" % line)

