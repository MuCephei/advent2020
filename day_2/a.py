import re

line_regex = re.compile(r'(?P<min>[0-9]*)-(?P<max>[0-9]*) (?P<character>.): (?P<password>.*)')


def parse_passwords():
    valid_passwords = 0
    with open('input.txt', 'r') as file:
        for line in file.readlines():
            m = line_regex.match(line)
            valid_passwords += parse(int(m.group('min')), int(m.group('max')), m.group('character'), m.group('password'))
    return valid_passwords


def parse(min, max, character, password):
    num = password.count(character)
    return min <= num <= max


print(parse_passwords())
