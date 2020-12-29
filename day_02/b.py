import re

line_regex = re.compile(r'(?P<a>[0-9]*)-(?P<b>[0-9]*) (?P<character>.): (?P<password>.*)')


def parse_passwords():
    valid_passwords = 0
    with open('input.txt', 'r') as file:
        for line in file.readlines():
            m = line_regex.match(line)
            valid_passwords += parse(int(m.group('a')), int(m.group('b')), m.group('character'), m.group('password'))
    return valid_passwords


def parse(a, b, character, password):
    first = password[a-1] == character
    second = password[b-1] == character
    return first != second


print(parse_passwords())
