# https://en.wikipedia.org/wiki/Hexagonal_Efficient_Coordinate_System

hexes = {}

class hex:

    def __init__(self, a, r, c):
        self.black = False
        self.a, self.r, self.c = a, r, c
        self.future_black = None
        self.neighbours = None

    def calculate_future(self):
        if self.neighbours is None:
            self.neighbours = []
            for d in directons.values():
                a, r, c = d(self.a, self.r, self.c)
                if (a, r, c) in hexes:
                    h = hexes[(a, r, c)]
                else:
                    h = hex(a, r, c)
                    hexes[a, r, c] = h
                self.neighbours.append(h)
        total = 0
        for tile in self.neighbours:
            total += tile.black
        if not self.black and total == 2:
            self.future_black = True
        elif self.black and (total == 0 or total > 2):
            self.future_black = False
        else:
            self.future_black = self.black

    def time_passes(self):
        self.black = self.future_black

    def flip(self):
        self.black = not self.black

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
    with open('input.txt', 'r') as file:
        for line in file.readlines():
            line = line.strip("\n")
            instructions = parse_instructions(line)
            a, r, c = 0, 0, 0
            for i in instructions:
                a, r, c = i(a, r, c)
            if (a, r, c) in hexes:
                hexes[(a, r, c)].flip()
            else:
                h = hex(a, r, c)
                h.flip()
                hexes[a, r, c] = h
    return hexes

def pass_time():
    keys = []
    for k in tiles.keys():
        keys.append(k)
    for key in keys:
        hexes[key].calculate_future()
    for key in keys:
        hexes[key].time_passes()

tiles = make_tiles()
keys = []
for k in tiles.keys():
    keys.append(k)
for key in keys:
    hexes[key].calculate_future()
for i in range(100):
    pass_time()
black = 0
for h in tiles.values():
    if h.black:
        black += 1
print(black)
