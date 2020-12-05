class seat:
    def __init__(self, boarding_pass):
        self.row, self.col = parse_boarding_pass(boarding_pass)
        self.id = self.row * 8 + self.col

    def __lt__(self, other):
        return self.id < other.id

    def __str__(self):
        return str(self.id)

def parse_boarding_pass(boarding_pass):
    # f is 0
    # b is 1
    # make it in binary
    row = boarding_pass[:7]
    col = boarding_pass[7:]
    return get_binary(row, "B"), get_binary(col, "R")


def get_binary(value, one):
    s = ""
    for v in value:
        if v == one:
            s += "1"
            continue
        s += "0"
    return int(s, 2)

def get_seats():
    seats = []
    with open('input.txt', 'r') as file:
        for line in file.readlines():
            line = line.strip("\n")
            seats.append(seat(line))
    return seats


def get_your_seat(seats):
    seats.sort()
    prev = seats[0]
    for s in seats[1:]:
        if s.id - prev.id > 1:
            return s.id - 1
        prev = s


seats = get_seats()
print(get_your_seat(seats))


