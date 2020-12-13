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

    def contiguous(self, target):
        for a in range(len(self.data)):
            b, found = self.a_b_test(a, target)
            if found:
                return self.data[a:b+1]
        return 0, 0

    def a_b_test(self, a, target):
        for b in range(a, len(self.data)):
            total = sum(self.data[a:b+1])
            if total > target:
                return 0, False
            if total == target:
                return b, True
        return 0, False

def merry_xmas(preamble_length):
    data = xmas(preamble_length)
    with open('input.txt', 'r') as file:
        for line in file.readlines():
            n = int(line.strip("\n"))
            if not data.add_number(n):
                contiguous = data.contiguous(n)
                return min(contiguous), max(contiguous)

print(sum(merry_xmas(25)))

