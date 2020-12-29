class xmas:

    def __init__(self, preamble_length):
        self.preamble_length = preamble_length
        self.data = []
        self.preamble = set()

    def add_number(self, x):
        self.data.append(x)
        if len(self.data) <= self.preamble_length:
            self.preamble.add(x)
            return True
        if not self.is_valid(x):
            return False
        self.preamble.remove(self.data[-(self.preamble_length + 1)])
        self.preamble.add(x)
        return True

    def is_valid(self, x):
        for value in self.preamble:
            if x - value in self.preamble:
                return True
        return False

def merry_xmas(preamble_length):
    data = xmas(preamble_length)
    with open('input.txt', 'r') as file:
        for line in file.readlines():
            line = line.strip("\n")
            if not data.add_number(int(line)):
                return line

print(merry_xmas(25))

