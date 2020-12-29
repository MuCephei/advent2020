tree = "#"
empty = "."


class slope:
    def __init__(self, grid):
        self.grid = grid
        self.y = len(grid)
        self.x = len(grid[0])

    def __str__(self):
        s = ""
        for row in self.grid:
            s += str(row) + "\n"
        return s

    def is_tree(self, x, y):
        if y >= self.y:
            return None
        x = x % self.x
        return self.grid[y][x]

def make_map():
    grid = []
    with open('input.txt', 'r') as file:
        for line in file.readlines():
            line = line.strip("\n")
            grid.append(parse_input_line(line))
    return slope(grid)


def parse_input_line(line):
    output = []
    for spot in line:
        output.append(spot == tree)
    return output


def toboggan(map, x, y):
    trees = 0
    current_x, current_y = 0, 0
    hit = map.is_tree(current_x, current_y)
    while hit is not None:
        trees += hit
        current_x += x
        current_y += y
        hit = map.is_tree(current_x, current_y)
    return trees


toboggan_map = make_map()
product = 1
angles = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
for angle in angles:
    trees = toboggan(toboggan_map, angle[0], angle[1])
    print(trees)
    product *= trees
print("Product:", product)
