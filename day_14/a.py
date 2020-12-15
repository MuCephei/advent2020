from collections import defaultdict
import re

class mask:

    def __init__(self, signature):
        self.bits = []
        for n in range(0, len(signature)):
            s = signature[n]
            if s != 'X':
                self.bits.append((n, s == '1'))

    def __str__(self):
        return str(self.bits)

    def apply(self, input):
        binary_string = str(bin(int(input))[2:]).zfill(36)
        for bit in self.bits:
            index = bit[0]
            binary_string = binary_string[:index] + str(int(bit[1])) + binary_string[index+1:]
        return int(binary_string, 2)

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
                contents[match.group('index')] = m.apply(match.group('input'))
    total = 0
    for v in contents.values():
        total += v
    return total

print(step_through())

