from collections import defaultdict
# https://en.wikipedia.org/wiki/Hexagonal_Efficient_Coordinate_System

def northwest(a, r, c):
    new_a = 1 - a
    return new_a, r - new_a, c - new_a

def northeast(a, r, c):
    new_a = 1 - a
    return new_a, r - new_a, c + a

def west(a, r, c):
    return a, r, c - 1

def east(a, r, c):
    return a, r, c + 1

def southwest(a, r, c):
    new_a = 1 - a
    return new_a, r + a, c - new_a

def southeast(a, r, c):
    new_a = 1 - a
    return new_a, r + a, c + a

directons = {"nw": northwest, "ne": northeast, "w": west, "e": east, "sw": southwest, "se": southeast}

def parse_instructions(line):
    instructions = []
    while line != "":
        next = line[0]
        if next == "e" or next == "w":
            instructions.append(directons[next])
            line = line[1:]
        else:
            instructions.append(directons[next + line[1]])
            line = line[2:]
    return instructions

def make_tiles():
    hexes = defaultdict(int)
    with open('input.txt', 'r') as file:
        for line in file.readlines():
            line = line.strip("\n")
            instructions = parse_instructions(line)
            a, r, c = 0, 0, 0
            for i in instructions:
                a, r, c = i(a, r, c)
            hexes[(a, r, c)] += 1
    return hexes

tiles = make_tiles()
odd = 0
for flipped in tiles.values():
    if flipped % 2 == 1:
        odd += 1
print(odd)

