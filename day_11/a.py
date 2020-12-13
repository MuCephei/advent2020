class seat:

    def __init__(self, value):
        self.floor = value == "."
        self.occupied = value == "#"
        self.adjacent = []
        self.future_occupied = False

    def add_adjacent(self, other):
        self.adjacent.append(other)
        other.adjacent.append(self)

    def __str__(self):
        if self.floor:
            return "."
        if self.occupied:
            return "#"
        return "L"

    def calculate_future(self):
        if self.floor:
            return
        total = 0
        for s in self.adjacent:
            total += s.occupied
        if self.occupied and total >= 4:
            self.future_occupied = False
            return
        if not self.occupied and total == 0:
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
        current_row = len(self.seats) - 1
        previous_row = current_row - 1
        for n in range(0, len(seats)):
            seat = self.seats[current_row][n]
            if n > 0:
                seat.add_adjacent(self.seats[current_row][n - 1])
                if previous_row >= 0:
                    seat.add_adjacent(self.seats[previous_row][n - 1])
            if previous_row >= 0:
                seat.add_adjacent(self.seats[previous_row][n])
                if n < len(seats) - 1:
                    seat.add_adjacent(self.seats[previous_row][n+1])

    def __str__(self):
        s = ""
        for row in self.seats:
            for seat in row:
                s += str(seat)
            s += "\n"
        return s

    def time_passes(self):
        changed = False
        for row in self.seats:
            for s in row:
                s.calculate_future()
        for row in self.seats:
            for s in row:
                changed = s.future() or changed
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