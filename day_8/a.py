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

    def traverse(self, x):
        visited = set()
        total = 0
        while x not in visited:
            visited.add(x)
            inc, x = self.do(x)
            total += inc
        return total

    def do(self, x):
        command = self.lines[x]
        if command[0] == "nop":
            return 0, x + 1
        if command[0] == "acc":
            return command[1], x + 1
        if command[0] == "jmp":
            return 0, x + command[1]
        print('error doing command')
        return None

def make_instructions():
    i = instructions()
    with open('input.txt', 'r') as file:
        for line in file.readlines():
            line = line.strip("\n")
            components = line.split(" ")
            i.add_line(components[0], int(components[1]))
    return i

instruction_set = make_instructions()
print(instruction_set.traverse(0))
