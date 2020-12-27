class node:

    def __init__(self, value):
        self.value = value
        self.clockwise = None
        self.counter_clockwise = None

    def set_clockwise(self, next):
        self.clockwise = next
        next.counter_clockwise = self

    def set_counter_clockwise(self, prev):
        prev.set_clockwise(self)

    def __repr__(self):
        return str(self.value)

class cups:

    def __init__(self, values, upper_limit = 10):
        values += [x for x in range(len(values) + 1, upper_limit + 1)]
        self.current = node(values[0])
        self.internal_index = [None for _ in range(len(values) + 1)]
        self.internal_index[self.current.value] = self.current
        prev = self.current
        for value in values[1:]:
            curr = node(value)
            self.internal_index[value] = curr
            prev.set_clockwise(curr)
            prev = curr
        curr.set_clockwise(self.current)
        self.min = min(values)
        self.max = max(values)

    def move(self):
        start = self.current.clockwise
        middle = start.clockwise
        end = middle.clockwise
        self.current.set_clockwise(end.clockwise)
        target_value = self.current.value - 1
        if target_value < self.min:
            target_value = self.max
        while target_value == start.value or target_value == middle.value or target_value == end.value:
            target_value = target_value - 1
            if target_value < self.min:
                target_value = self.max
        target = self.internal_index[target_value]
        clockwise_target = target.clockwise
        target.set_clockwise(start)
        end.set_clockwise(clockwise_target)
        self.current = self.current.clockwise

    def __repr__(self):
        curr = self.current
        linked_list = []
        for x in range(len(self.internal_index) - 1):
            linked_list.append(str(curr.value))
            curr = curr.clockwise
        return "Current: %s [%s]" % (self.current.value, ",".join(linked_list))

def make_cups():
    with open('input.txt', 'r') as file:
        for line in file.readlines():
            line = line.strip("\n")
            return cups([int(x) for x in line], upper_limit = 1000000)

circle = make_cups()
for x in range(10):
    for y in range(1000000):
        circle.move()
a = circle.internal_index[1].clockwise
b = a.clockwise
print(a, b)
print(a.value * b.value)
