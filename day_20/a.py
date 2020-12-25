from collections import defaultdict

class tile:

    def __init__(self, tile_id, contents):
        self.id = tile_id
        self.contents = []
        for row in contents:
            self.contents.append([x == "." for x in row])
        self.top_hash = hash_line(self.contents[0])
        self.bottom_hash = hash_line(self.contents[-1])
        self.left_hash = hash_line([x[0] for x in self.contents])
        self.right_hash = hash_line([x[-1] for x in self.contents])

    def __repr__(self):
        s = "\nTile %d:\n" % self.id
        for row in self.contents:
            s += "".join(map(lambda x: "." if x else "#", row)) + "\n"
        return s

    def hashes(self):
        return self.top_hash, self.bottom_hash, self.left_hash, self.right_hash

def hash_line(row):
    a = create_int(row)
    b = create_int(row[::-1])
    return create_int(row) * create_int(row[::-1]) + a + b

def create_int(row):
    return int("".join("1" if x else "0" for x in row), 2)


def make_tiles():
    with open('test_input.txt', 'r') as file:
        tiles = []
        line = file.readline().strip("\n")
        while line:
            tile_id = int(line.replace("Tile ", "").strip(":"))
            line = file.readline().strip("\n")
            content = []
            while line:
                content.append(line)
                line = file.readline().strip()
            tiles.append(tile(tile_id, content))
            line = file.readline().strip("\n")
    return tiles

tiles = make_tiles()
hashes = defaultdict(list)
for tile in tiles:
    for h in tile.hashes():
        hashes[h].append(tile.id)

edges = defaultdict(int)
for ids in hashes.values():
    if len(ids) == 1:
        edges[ids[0]] += 1

product = 1
for edge in edges:
    if edges[edge] == 2:
        product *= edge
        print(edge)
print(product)
