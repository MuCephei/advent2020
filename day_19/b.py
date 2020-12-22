import re

base_regex = re.compile(r"(?P<rule>[0-9]+):\s\"(?P<base>[a-z])\"")
list_regex = re.compile(r"(?P<rule>[0-9]+):\s(?P<list>[0-9\s]+)")
combo_regex = re.compile(r"(?P<rule>[0-9]+):\s(?P<combo>[0-9\s]*\|[0-9\s]*)")

rule_list = {}

class base_rule:

    def __init__(self, value):
        self.value = value

    def match(self, other):
        if other == "":
            return False, other
        return self.value == other[0], [other[1:]]

    def __repr__(self):
        return "Base: %s" % self.value

    def deterministic(self):
        return True

    def deterministic_value(self):
        return self.value

class combo_rule:

    def __init__(self, rules):
        self.rules = rules

    def match(self, other):
        if other == "":
            return False, other
        possible_matches = []
        for rule in self.rules:
            match, new_other = rule.match(other)
            if match:
                for o in new_other:
                    possible_matches.append(o)
        if len(possible_matches):
            return True, possible_matches
        return False, other

    def __repr__(self):
        return "Combo: %s" % self.rules

class list_rule:

    def __init__(self, indexes):
        self.indexes = indexes

    def match(self, other):
        if other == "":
            return False, other
        inputs = [other]
        for index in self.indexes:
            rule = rule_list[index]
            new_inputs = []
            for input in inputs:
                match, possible_matches = rule.match(input)
                if match:
                    for m in possible_matches:
                        new_inputs.append(m)
            inputs = new_inputs
            if len(inputs) == 0:
                return False, other
        return True, inputs

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

def match_8(other):
    rule_42 = rule_list[42]
    match, possible_matches = rule_42.match(other)
    if not match:
        return False, other
    repeat_match, repeat_possible_matches = match_8(possible_matches[0])
    if repeat_match:
        for m in repeat_possible_matches:
            possible_matches.append(m)
    return True, possible_matches

def match_11(other):
    rule_42 = rule_list[42]
    rule_31 = rule_list[31]
    matched_42, possible_matches = rule_42.match(other)
    if not matched_42:
        return False, other
    matched_11, possible_matches_11 = match_11(possible_matches[0])
    if match_11:
        for m in possible_matches_11:
            possible_matches.append(m)
    possible_matches_final = []
    for possible_match in possible_matches:
        matched_31, possible_matches_31 = rule_31.match(possible_match)
        if matched_31:
            for m in possible_matches_31:
                possible_matches_final.append(m)
    return len(possible_matches_final) > 0, possible_matches_final


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

        rule_list[8].match = match_8
        rule_list[11].match = match_11

        total = 0
        for line in file.readlines():
            line = line.strip("\n")
            match, leftovers = rule_list[0].match(line)
            if match and "" in leftovers:
                total += 1
        return total

print(make_rules())

