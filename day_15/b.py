class memory:

    def __init__(self):
        self.record = {}
        self.current = 0
        self.turns = 0

    def add_number(self, number):
        if number not in self.record:
            self.current = 0
        else:
            self.current = self.turns - self.record[number]
        self.record[number] = self.turns
        self.turns += 1

    def __str__(self):
        return "Current: %d\nTurns: %d\nRecord: %s" % (self.current, self.turns, str(self.record))

    def play(self, till=1):
        for i in range(self.turns, till):
            self.add_number(self.current)
        return self.current

def init_memory():
    mem = memory()
    with open('input.txt', 'r') as file:
        for line in file.readlines():
            line = line.strip("\n")
            values = line.split(",")
            for v in values:
                mem.add_number(int(v))
    return mem

mem = init_memory()
#not exactly optimized
print(mem.play(30000000-1))
