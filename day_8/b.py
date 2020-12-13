class instructions:

    def __init__(self):
        self.lines = []

    def add_line(self, command, value):
        self.lines.append((command, value))

    def __str__(self):
        s = ""
        for line in self.lines:
            s += line[0] + " " + str(line[1]) + "\n"
        return s

    def __len__(self):
        return len(self.lines)

    def traverse(self, x):
        visited = set()
        total = 0
        while x not in visited:
            visited.add(x)
            inc, x = self.do(x)
            if x == None:
                return total, True
            total += inc
        return total, False

    def traverse_with_flipped_bit(self, x, flipped_x):
        visited = set()
        total = 0
        while x not in visited:
            visited.add(x)
            inc, x = self.do(x, flipped_x == x)
            if x is None:
                return total, True
            total += inc
        return total, False

    def do(self, x, flipped):
        if x == len(self.lines):
            return 0, None
        command = self.lines[x]
        if (not flipped and command[0] == "nop") or (flipped and command[0] == "jmp"):
            return 0, x + 1
        if command[0] == "acc":
            return command[1], x + 1
        if (not flipped and command[0] == "jmp") or (flipped and command[0] == "nop"):
            return 0, x + command[1]
        print('error doing command')
        return 0, None

def make_instructions():
    i = instructions()
    with open('input.txt', 'r') as file:
        for line in file.readlines():
            line = line.strip("\n")
            components = line.split(" ")
            i.add_line(components[0], int(components[1]))
    return i

instruction_set = make_instructions()
for x in range(len(instruction_set)):
    total, traversed = instruction_set.traverse_with_flipped_bit(0, x)
    if traversed:
        print(total)
