import re

parenthesis_group = re.compile(r"(\([0-9+*\s]*\))+")

def evaluate(line):
    line = condense_parenthesis(line)
    components = line.split()
    a = int(components[0])
    for i in range(2, len(components), 2):
        if components[i-1] == "+":
            a += int(components[i])
        elif components[i-1] == "*":
            a *= int(components[i])
        else:
            print("error evaluating expression %s" % line)
    return str(a)

def condense_parenthesis(line):
    match = parenthesis_group.search(line)
    while match:
        first_match = match.group(0)
        line = line.replace(first_match, evaluate(first_match[1:-1]), 1)
        match = parenthesis_group.search(line)
    return line

def math_homework():
    total = 0
    with open('input.txt', 'r') as file:
        for line in file.readlines():
            line = line.strip("\n")
            total += int(evaluate(line))
    return total

print(math_homework())

