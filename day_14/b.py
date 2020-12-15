from collections import defaultdict
import re

class mask:

    def __init__(self, signature):
        self.base = signature

    def __str__(self):
        return str(self.base)

    def apply(self, input):
        binary_input = str(bin(int(input))[2:]).zfill(36)
        values = [""]
        for n in range(len(binary_input)):
            new_values = []
            bit = self.base[n]
            if bit == "0":
                for value in values:
                    new_values.append(value + binary_input[n])
            elif bit == "1":
                for value in values:
                    new_values.append(value + "1")
            elif bit == "X":
                for value in values:
                    new_values.append(value + "0")
                    new_values.append(value + "1")
            values = new_values

        result = []
        for value in values:
            result.append(int(value, 2))
        return result

mask_set_regex = re.compile("mem\[(?P<index>[0-9]*)\] = (?P<input>[0-9]*)")

def step_through():
    contents = defaultdict(int)
    with open('input.txt', 'r') as file:
        for line in file.readlines():
            line = line.strip("\n")
            if line.startswith("mask = "):
                m = mask(line.strip("mask = "))
            else:
                match = mask_set_regex.match(line)
                indexes = m.apply(match.group('index'))
                for index in indexes:
                    contents[index] = int(match.group('input'))
    total = 0
    for v in contents.values():
        total += v
    return total

print(step_through())

