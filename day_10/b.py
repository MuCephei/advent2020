import math

def get_adapters():
    adapters = [0]
    with open('input.txt', 'r') as file:
        for line in file.readlines():
            line = line.strip("\n")
            adapters.append(int(line))
    adapters.sort()
    adapters.append(adapters[-1] + 3)
    return adapters


def classify_adapters(adapters):
    sections = []
    section = []
    for n in range(1, len(adapters)):
        section.append(adapters[n-1])
        difference = adapters[n] - adapters[n-1]
        if difference == 3:
            sections.append(section)
            section = []
    section.append(adapters[-1])
    sections.append(section)
    return sections


# it just so happens that all the inputs go up by 1 or 3, never 2
def options_in_section(section):
    if len(section) <= 2:
        return 1
    n = len(section) - 2
    total_options_in_section = 2 ** n
    if n < 3:
        return total_options_in_section
    invalid = invalid_options_in_section(n - 3)
    return total_options_in_section - invalid


# calculate the number of values that have three sequential 0s
def invalid_options_in_section(n):
    total = 0
    total += 2 ** n
    for x in range(1, n + 1):
        total += 2 ** (n - x) * 2 ** (x - 1)
    return total


adapters = get_adapters()
classification = classify_adapters(adapters)
total = 1
for section in classification:
    options = options_in_section(section)
    total *= options
print(total)

