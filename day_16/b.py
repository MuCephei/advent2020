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


field_regex = re.compile("(?P<name>[a-z\s]*):\s(?P<a>[0-9]*-[0-9]*)\sor\s(?P<b>[0-9]*-[0-9]*)")


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
        your_ticket = [int(x) for x in file.readline().strip("\n").split(",")]
        # nearby tickets:
        file.readline()
        file.readline()
        nearby = file.readline().strip("\n")
        while nearby != "":
            nearby_tickets.append([int(x) for x in nearby.split(",")])
            nearby = file.readline().strip("\n")
    return fields, your_ticket, nearby_tickets

def valid_tickets(fields, tickets):
    result = []
    for ticket in tickets:
        valid_ticket = True
        for value in ticket:
            valid = False
            for field in fields:
                if field.valid(value):
                    valid = True
            if not valid:
                valid_ticket = False
        if valid_ticket:
            result.append(ticket)
    return result

def valid_for_all_tickets(field, n, tickets):
    for ticket in tickets:
        value = ticket[n]
        if not field.valid(value):
            return False
    return True

fields, your_ticket, nearby_tickets = parse_input()
valid = valid_tickets(fields, nearby_tickets)
mappings = {}
for m in range(len(fields)):
    field = fields[m]
    mapping = set(filter(lambda n: valid_for_all_tickets(field, n, valid), range(len(fields))))
    mappings[field] = mapping
final_mappings = {}
while len(mappings):
    for field in mappings:
        if len(mappings[field]) == 1:
            value = mappings[field].pop()
            final_mappings[field] = value
            for f in mappings:
                if value in mappings[f]:
                    mappings[f].remove(value)
    del mappings[field]
departure_product = 1
for n in range(len(your_ticket)):
    for mapping in final_mappings:
        if final_mappings[mapping] == n:
            # print("%s:%s" % (mapping.name, your_ticket[n]))
            if mapping.name.startswith("departure "):
                departure_product *= your_ticket[n]
print("Departure: %d" % departure_product)