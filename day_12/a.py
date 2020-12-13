import math

class ship:

    def __init__(self):
        self.facing = 0
        self.location = (0, 0)

    def move(self, instruction, value):
        dx, dy = 0, 0
        if instruction == "F":
            dx, dy = math.cos(self.facing) * value, math.sin(self.facing) * value
        elif instruction == "R":
            self.rotate(-1 * value)
        elif instruction == "L":
            self.rotate(value)
        elif instruction == "N":
            dy = value
        elif instruction == "S":
            dy = -1 * value
        elif instruction == "E":
            dx = value
        elif instruction == "W":
            dx = -1 * value
        self.location = (self.location[0] + dx, self.location[1] + dy)

    def rotate(self, degrees):
        self.facing += math.radians(degrees)

    def __str__(self):
        return "x:%s, y:%s, manhattan:%s" % (self.location[0], self.location[1], abs(self.location[0]) + abs(self.location[1]))

def sail():
    s = ship()
    with open('input.txt', 'r') as file:
        for line in file.readlines():
            line = line.strip("\n")
            s.move(line[0], int(line[1:]))
    return s

print(sail())
