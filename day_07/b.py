import re

content_regex = re.compile("\s*(?P<n>[0-9]+) (?P<name>[\w\s]*) bags?")

bags = {}

class bag:

    def __init__(self, name, contents):
        self.name = name
        self.contents = contents

    def __str__(self):
        return "%s contains: %s" % (self.name, self.contents)

    def contains_x_bag(self, x, already_looked_at=None):
        if already_looked_at is None:
            already_looked_at = {}

        if self.name == x:
            return True
        if self.name in already_looked_at:
            return False

        already_looked_at[self.name] = True
        for c in self.contents:
            if bags[c].contains_x_bag(x, already_looked_at):
                return True
        return False

    def bags(self):
        total_bags = 1
        for c in self.contents:
            inside = bags[c].bags()
            total_bags += int(self.contents[c]) * inside
        return total_bags

def populate_bags():
    with open('input.txt', 'r') as file:
        for line in file.readlines():
            line = line.strip("\n")
            bag = parse_line(line)
            bags[bag.name] = bag
    return bags

def parse_line(line):
    name, contents = line.split(" bags contain ", 2)
    content = {}
    for c in parse_contents(contents):
        content[c['name']] = c['n']

    return bag(name, content)

def parse_contents(contents):
    contents = contents.strip(".")
    if contents == "no other bags":
        return []
    return [parse_content(c) for c in contents.split(",")]

def parse_content(content):
    m = content_regex.match(content)
    return m.groupdict()

populate_bags()
total = 0
print(bags["shiny gold"].bags() - 1)
