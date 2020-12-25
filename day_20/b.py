from collections import defaultdict
import math

class grid:


    def __init__(self, size, corners, edges):
        self.size = size
        self.edges = set(edges)
        self.corners = set(corners)
        self.tiles = []
        for x in range(self.size):
            self.tiles.append([None] * self.size)

    def add_tiles(self, tiles):
        # add top left corner first
        corner_a = self.corners.pop()
        for corner in self.corners:
            self.edges.add(corner[0])
            self.edges.add(corner[1])
        top_left = None
        n = 0
        top_hash, left_hash = corner_a
        while top_left is None:
            t = tiles[n]
            t_hashes = t.hashes()
            if top_hash in t_hashes and left_hash in t_hashes:
                top_left = t
            n += 1
        tiles.remove(top_left)
        # rotate correctly
        while top_left.get_hash(0) != top_hash:
            top_left.rotate(1)
        if top_left.get_hash(3) != left_hash:
            top_left.flip_x()
        if top_left.get_hash(3) != left_hash:
            print("error rotating first tile")
            return
        self.tiles[0][0] = top_left

        # add top edges
        for y in range(1, self.size):
            left_match = self.tiles[0][y-1]
            left_row = left_match.row(1)[::-1]
            left_hash = left_match.get_hash(1)
            right = None
            n = 0
            while right is None:
                t = tiles[n]
                t_hashes = t.hashes()
                if left_hash in t_hashes:
                    right = t
                n += 1
            # rotate correctly
            while right.get_hash(3) != left_hash:
                right.rotate(1)
            if right.row(3) != left_row:
                right.flip_y()
                if right.row(3) != left_row:
                    print("error rotating in top row")
                    return
                if right.get_hash(0) not in self.edges:
                    print("error with edge list")
                    return
            tiles.remove(right)
            self.tiles[0][y] = right

        # add other edges
        for x in range(1, self.size):
            for y in range(0, self.size):
                top_match = self.tiles[x-1][y]
                top_row = top_match.row(2)[::-1]
                top_hash = top_match.get_hash(2)
                top = None
                n = 0
                while top is None:
                    t = tiles[n]
                    t_hashes = t.hashes()
                    if top_hash in t_hashes:
                        top = t
                    n += 1
                # rotate correctly
                while top.get_hash(0) != top_hash:
                    top.rotate(1)
                if top.row(0) != top_row:
                    top.flip_x()
                    if top.row(0) != top_row:
                        print("error rotating in other row")
                        return
                tiles.remove(top)
                self.tiles[x][y] = top

    def trimmed_edges(self):
        length = len(self.tiles[0][0].contents)
        trimmed_size = length - 2
        trimmed = []
        for x in range(trimmed_size * self.size):
            trimmed.append([None] * (trimmed_size * self.size))
        for x in range(self.size):
            for y in range(self.size):
                x_offset, y_offset = x * trimmed_size, y * trimmed_size
                for tile_x in range(1, trimmed_size + 1):
                    for tile_y in range(1, trimmed_size + 1):
                        value = "." if self.tiles[x][y].contents[tile_x][tile_y] else "#"
                        trimmed[x_offset + tile_x - 1][y_offset + tile_y - 1] = value
        return trimmed

sea_monster = \
'''                  # 
#    ##    ##    ###
 #  #  #  #  #  #   '''

sea_monster_patter = [[x == "#" for x in line] for line in sea_monster.split("\n")]

class tile:

    def __init__(self, tile_id, contents):
        self.id = tile_id
        self.size = len(contents)
        self.contents = []
        for x in range(self.size):
            self.contents.append([])
            for y in range(self.size):
                self.contents[x].append(contents[x][y] == ".")

    def __repr__(self):
        s = "\nTile %d\n" % self.id
        for x in range(self.size):
            s += "".join(["." if value else "#" for value in self.contents[x]]) + "\n"
        return s

    def hashes(self):
        return [self.get_hash(i) for i in range(4)]

    def row(self, id):
        if id == 0:
            return list(self.contents[0])
        elif id == 1:
            return [self.contents[x][-1] for x in range(0, self.size)]
        elif id == 2:
            return list(self.contents[-1][::-1])
        elif id == 3:
            return [self.contents[x][0] for x in range(self.size - 1, -1, -1)]

    def get_hash(self, id):
        return hash_line(self.row(id))

    def rotate(self, id):
        for r in range(id):
            self.contents = list(zip(*self.contents[::-1]))

    def flip_x(self):
        for x in range(self.size):
            self.contents[x] = self.contents[x][::-1]

    def flip_y(self):
        flipped_contents = []
        for x in range(self.size - 1, -1, -1):
            flipped_contents.append(self.contents[x])
        self.contents = flipped_contents

    def count_pattern(self, pattern):
        matches = set()
        pattern_length = len(pattern[0])
        pattern_height = len(pattern)
        for start_x in range(self.size - pattern_height):
            for start_y in range(self.size - pattern_length):
                match = True
                sea_monster_tiles = []
                x = 0
                while match and x < len(pattern):
                    y = 0
                    while match and y < len(pattern[0]):
                        if pattern[x][y]:
                            if not self.contents[x + start_x][y + start_y]:
                                sea_monster_tiles.append((x + start_x, y + start_y))
                                # print(start_x, start_y, x, y, sea_monster_tiles)
                            else:
                                match = False
                        y += 1
                    x += 1
                if match:
                    for t in sea_monster_tiles:
                        matches.add(t)
        return len(matches)

    def count_water(self):
        total = 0
        for row in self.contents:
            for value in row:
                if not value:
                    total += 1
        return total


def hash_line(row):
    a = create_int(row)
    b = create_int(row[::-1])
    return create_int(row) * create_int(row[::-1]) + a + b + a ** b + b ** a

def create_int(row):
    return int("".join("1" if x else "0" for x in row), 2)

def make_tiles():
    with open('input.txt', 'r') as file:
        tiles = {}
        line = file.readline().strip("\n")
        while line:
            tile_id = int(line.replace("Tile ", "").strip(":"))
            line = file.readline().strip("\n")
            content = []
            while line:
                content.append(line)
                line = file.readline().strip()
            tiles[tile_id] = tile(tile_id, content)
            line = file.readline().strip("\n")
    return tiles

tiles = make_tiles()
hashes = defaultdict(list)
for t in tiles.values():
    for h in t.hashes():
        hashes[h].append(t.id)
        if len(hashes[h]) > 2:
            print("Error with hash function")

edges = defaultdict(int)
for ids in hashes.values():
    if len(ids) == 1:
        edges[ids[0]] += 1

corners = []
edge_list = []
for edge in edges:
    if edges[edge] == 2:
        c = []
        for h in tiles[edge].hashes():
            if len(hashes[h]) == 1:
                c.append(h)
        corners.append(tuple(c))
    else:
        for h in tiles[edge].hashes():
            if len(hashes[h]) == 1:
                edge_list.append(h)

photo = grid(int(math.sqrt(len(tiles))), corners, edge_list)
photo.add_tiles(list(tiles.values()))
trimmed = photo.trimmed_edges()
photo_tile = tile(1, trimmed)
for x in range(4):
    monster_parts = photo_tile.count_pattern(sea_monster_patter)
    if monster_parts > 0:
        water = photo_tile.count_water()
        print(water - monster_parts)
    photo_tile.rotate(1)
photo_tile.flip_x()
for x in range(4):
    monster_parts = photo_tile.count_pattern(sea_monster_patter)
    if monster_parts > 0:
        water = photo_tile.count_water()
        print(water - monster_parts)
    photo_tile.rotate(1)


