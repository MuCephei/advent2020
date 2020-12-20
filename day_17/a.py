from collections import defaultdict

class cubes:

    def __init__(self, initial_cubes, size):
        self.min_size = -1
        self.size = size + 1
        self.d = [(x, y, z) for x in range(-1, 2) for y in range(-1, 2) for z in range(-1, 2)]
        self.d.remove((0, 0, 0))
        self.grid = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: cube())))
        self.active = 0
        for c in initial_cubes:
            x, y, z, active = c
            self.grid[x][y][z].active = active
            self.active += active
        self.assign_all_neighbours()

    def __str__(self):
        s = ""
        for z in range(self.min_size, self.size):
            s += "z=%d\n" % z
            for x in range(self.min_size, self.size):
                for y in range(self.min_size, self.size):
                    s += str(self.grid[x][y][z])
                s += "\n"
            s += "\n\n"
        s += "-----------------"
        return s

    def __len__(self):
        return self.active

    def assign_all_neighbours(self):
        for x in range(self.min_size, self.size):
            for y in range(self.min_size, self.size):
                for z in range(self.min_size, self.size):
                    self.assign_neighbours(x, y, z)

    def assign_neighbours(self, x, y, z):
        c = self.grid[x][y][z]
        c.neighbours = []
        for dx, dy, dz in self.d:
            c.add_neighbour(self.grid[x + dx][y + dy][z + dz])

    def calculate_future(self):
        for x in self.grid.values():
            for y in x.values():
                for c in y.values():
                    c.calculate_future()

    def activate_future(self):
        self.active = 0
        for x in self.grid.values():
            for y in x.values():
                for z in y.values():
                    self.active += z.activate_future()
        self.min_size -= 1
        self.size += 1
        self.assign_all_neighbours()

class cube:

    def __init__(self, active=False):
        self.active = active
        self.neighbours = []
        self.future = False

    def add_neighbour(self, other):
        self.neighbours.append(other)

    def calculate_future(self):
        total = sum(map(lambda a: a.active, self.neighbours))
        if self.active:
            self.future = total == 2 or total == 3
            return
        self.future = total == 3
        return

    def activate_future(self):
        self.active = self.future
        return self.active

    def __str__(self):
        if self.active:
            return "#"
        return "."

def parse():
    layout = []
    with open('input.txt', 'r') as file:
        for line in file.readlines():
            line = line.strip("\n")
            layout.append(list(map(lambda x: x == "#", line)))
    active_cubes = []
    for x in range(len(layout)):
        for y in range(len(layout[x])):
            active_cubes.append((x, y, 0, layout[x][y]))
    return cubes(active_cubes, len(layout))

cube_grid = parse()
for n in range(6):
    cube_grid.calculate_future()
    cube_grid.activate_future()
print(len(cube_grid))

