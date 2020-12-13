import math

class ship:

    def __init__(self, x, y):
        self.waypoint = (x, y)
        self.location = (0, 0)

    def move(self, instruction, value):
        if instruction == "F":
            dx, dy = self.waypoint[0] * value, self.waypoint[1] * value
            self.location = (self.location[0] + dx, self.location[1] + dy)
            return
        elif instruction == "R":
            self.rotate(-1 * value)
        elif instruction == "L":
            self.rotate(value)
        elif instruction == "N":
            self.move_waypoint(0, value)
        elif instruction == "S":
            self.move_waypoint(0, -value)
        elif instruction == "E":
            self.move_waypoint(value, 0)
        elif instruction == "W":
            self.move_waypoint(-value, 0)
        return

    def rotate(self, degrees):
        radians = math.radians(degrees)
        x = (self.waypoint[0] * math.cos(radians)) - (self.waypoint[1] * math.sin(radians))
        y = (self.waypoint[0] * math.sin(radians)) + (self.waypoint[1] * math.cos(radians))
        self.waypoint = (x, y)

    def move_waypoint(self, x, y):
        self.waypoint = (self.waypoint[0] + x, self.waypoint[1] + y)

    def __str__(self):
        return "x:%s, y:%s, manhattan:%s" % (self.location[0], self.location[1], abs(self.location[0]) + abs(self.location[1]))

def sail():
    s = ship(10, 1)
    with open('input.txt', 'r') as file:
        for line in file.readlines():
            line = line.strip("\n")
            s.move(line[0], int(line[1:]))
    return s

print(sail())
