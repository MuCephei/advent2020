import re

class pattern:

    def __init__(self, p):
        components = p.split("-", 2)
        self.min, self.max = int(components[0]), int(components[1])

    def valid(self, value):
        return self.min <= value <= self.max

    def __str__(self):
        return "Min: %d Max: %d" % (self.min, self.max)

    def __repr__(self):
        return str(self)

class field:

    def __init__(self, name, patterns):
        self.name = name
        self.patterns = [pattern(p) for p in patterns]

    def valid(self, value):
        for p in self.patterns:
            if p.valid(value):
                return True
        return False

    def __str__(self):
        return "Name:%s Patterns:%s" % (self.name, str(self.patterns))

    def __repr__(self):
        return str(self)


field_regex = re.compile("(?P<name>[a-z\s]*:\s)(?P<a>[0-9]*-[0-9]*)\sor\s(?P<b>[0-9]*-[0-9]*)")

def parse_input():
    fields = []
    nearby_tickets = []
    with open('input.txt', 'r') as file:
        line = file.readline().strip("\n")
        while line != "":
            m = field_regex.match(line)
            fields.append(field(m.group("name"), [m.group("a"), m.group("b")]))
            line = file.readline().strip("\n")
        # your ticket:
        file.readline()
        your_ticket = file.readline().strip("\n")
        # nearby tickets:
        file.readline()
        file.readline()
        nearby = file.readline().strip("\n")
        while nearby != "":
            nearby_tickets.append([int(x) for x in nearby.split(",")])
            nearby = file.readline().strip("\n")
    return fields, your_ticket, nearby_tickets

def error_rate(fields, tickets):
    total = 0
    for ticket in tickets:
        for value in ticket:
            valid = False
            for field in fields:
                if field.valid(value):
                    valid = True
            if not valid:
                total += value
    return total

fields, _, nearby_tickets = parse_input()
print(error_rate(fields, nearby_tickets))

