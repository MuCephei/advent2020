class seat:

    def __init__(self, value):
        self.floor = value == "."
        self.occupied = value == "#"
        self.future_occupied = False

    def __str__(self):
        if self.floor:
            return "."
        if self.occupied:
            return "#"
        return "L"

    def calculate_future(self, visible):
        if self.floor:
            return
        if self.occupied and visible >= 5:
            self.future_occupied = False
            return
        if not self.occupied and visible == 0:
            self.future_occupied = True
            return
        self.future_occupied = self.occupied

    def future(self):
        if self.floor:
            return False
        changed = self.occupied != self.future_occupied
        self.occupied = self.future_occupied
        self.future_occupied = None
        return changed

class ferry:

    def __init__(self):
        self.seats = []

    def add_row(self, seats):
        self.seats.append(seats)

    def __str__(self):
        s = ""
        for row in self.seats:
            for seat in row:
                s += str(seat)
            s += "\n"
        return s

    def neighbours(self, x, y):
        total_visible = 0
        for direction in [(1,0), (1,1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]:
            total_visible += self.visible_neighbour(x, y, direction[0], direction[1])
        return total_visible

    def visible_neighbour(self, x, y, dx, dy):
        n = 1
        while True:
            curr_x = x + (n * dx)
            curr_y = y + (n * dy)
            if curr_x < 0 or curr_x >= len(self.seats):
                return False
            if curr_y < 0 or curr_y >= len(self.seats[curr_x]):
                return False
            if not self.seats[curr_x][curr_y].floor:
                return self.seats[curr_x][curr_y].occupied
            n += 1

    def time_passes(self):
        changed = False
        for x in range(len(self.seats)):
            for y in range(len(self.seats[x])):
                s = self.seats[x][y]
                if not s.floor:
                    visible = self.neighbours(x, y)
                    self.seats[x][y].calculate_future(visible)
        for x in range(len(self.seats)):
            for y in range(len(self.seats[x])):
                changed = self.seats[x][y].future() or changed
        return changed

    def __len__(self):
        total = 0
        for row in self.seats:
            for s in row:
                total += s.occupied
        return total

def make_ferry():
    f = ferry()
    with open('input.txt', 'r') as file:
        for line in file.readlines():
            line = line.strip("\n")
            row = []
            for l in line:
                row.append(seat(l))
            f.add_row(row)
    return f

f = make_ferry()
changed = True
while changed:
    changed = f.time_passes()
print(f)
print(len(f))