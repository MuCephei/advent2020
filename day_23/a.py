class wrapping_list:

    def __init__(self, l):
        self.l = l

    def wrapping_index(self, i):
        if i is None:
            return
        return i % len(self)

    def index(self, value):
        if value not in self.l:
            return -1
        return self.l.index(value)

    def __len__(self):
        return len(self.l)

    def __getitem__(self, i):
        if type(i) is slice:
            return [self.l[self.wrapping_index(x)] for x in range(i.start, i.stop, 1 if i.step is None else i.step)]
        return self.l[self.wrapping_index(i)]

    def __delitem__(self, i):
        del self.l[self.wrapping_index(i)]

    def __setitem__(self, i, v):
        self.l[self.wrapping_index(i)] = v

    def __str__(self):
        return str(self.l)

    def min(self):
        return min(self.l)

    def max(self):
        return max(self.l)

    def insert(self, i, values):
        self.l = self[0:i] + values + self[i:len(self.l)]

    def remove(self, v):
        if type(v) is list:
            for value in v:
                self.l.remove(value)
            return
        self.l.remove(v)

class cup:

    def __init__(self, order):
        self.order = wrapping_list(order)
        self.current = self.order[0]

    def __repr__(self):
        index = self.order.index(1)
        s = ""
        for x in range(index + 1, index + len(self.order)):
            s += str(self.order[x])
        return s

    def move(self):
        index = self.order.index(self.current)
        holding = self.order[index+1:index+4]
        self.order.remove(holding)
        target = self.current
        target_index = -1
        while target_index == -1:
            target = target - 1
            if target < self.order.min():
                target = self.order.max()
            target_index = self.order.index(target)
        self.order.insert(target_index + 1, holding)
        self.current = self.order[self.order.index(self.current) + 1]


def make_cups():
    with open('input.txt', 'r') as file:
        for line in file.readlines():
            line = line.strip("\n")
            return cup([int(x) for x in line])

cups = make_cups()
for n in range(100):
    cups.move()
print(cups)