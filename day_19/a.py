import re

base_regex = re.compile(r"(?P<rule>[0-9]+):\s\"(?P<base>[a-z])\"")
list_regex = re.compile(r"(?P<rule>[0-9]+):\s(?P<list>[0-9\s]+)")
combo_regex = re.compile(r"(?P<rule>[0-9]+):\s(?P<combo>[0-9\s]*\|[0-9\s]*)")

rule_list = {}

class base_rule:

    def __init__(self, value):
        self.value = value

    def match(self, other):
        return self.value == other[0], other[1:]

    def __repr__(self):
        return "Base: %s" % self.value

class combo_rule:

    def __init__(self, rules):
        self.rules = rules

    def match(self, other):
        for rule in self.rules:
            match, new_other = rule.match(other)
            if match:
                return True, new_other
        return False, other

    def __repr__(self):
        return "Combo: %s" % self.rules

class list_rule:

    def __init__(self, indexes):
        self.indexes = indexes

    def match(self, other):
        for index in self.indexes:
            rule = rule_list[index]
            match, other = rule.match(other)
            if not match:
                return False, other
        return True, other

    def __repr__(self):
        return "List: %s" % self.indexes


def make_base_rule(match):
    return int(match.group("rule")), base_rule(match.group("base"))

def make_list_rule(match):
    rules = [int(x) for x in match.group("list").split()]
    return int(match.group("rule")), list_rule(rules)

def make_combo_rule(match):
    rule_groups = match.group("combo").split("|")
    rules = []
    for group in rule_groups:
        rules.append(list_rule([int(x) for x in group.split()]))
    return int(match.group("rule")), combo_rule(rules)

def make_rules():
    with open('input.txt', 'r') as file:
        line = file.readline().strip("\n")
        while line != "":
            base_match = base_regex.match(line)
            if base_match:
                n, rule = make_base_rule(base_match)
                rule_list[n] = rule
                line = file.readline().strip("\n")
                continue
            combo_match = combo_regex.match(line)
            if combo_match:
                n, rule = make_combo_rule(combo_match)
                rule_list[n] = rule
                line = file.readline().strip("\n")
                continue
            list_match = list_regex.match(line)
            if list_match:
                n, rule = make_list_rule(list_match)
                rule_list[n] = rule
                line = file.readline().strip("\n")
                continue
            print("error, gone too far for line %s" % line)

        total = 0
        for line in file.readlines():
            line = line.strip("\n")
            match, leftovers = rule_list[0].match(line)
            if match and len(leftovers) == 0:
                total += 1
        return total

print(make_rules())

