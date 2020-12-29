import re

def birth_year(value):
    year = int(value)
    return 1920 <= year <= 2002


def issue_year(value):
    year = int(value)
    return 2010 <= year <= 2020


def expr_year(value):
    year = int(value)
    return 2020 <= year <= 2030


def height(value):
    if value.endswith("cm"):
        h = int(value.strip("cm"))
        return 150 <= h <= 193
    if value.endswith("in"):
        h = int(value.strip("in"))
        return 59 <= h <= 76
    return False


hair_regex = re.compile("#[0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f]")


def hair(value):
    if len(value) != 7:
        return False
    return hair_regex.fullmatch(value) is not None


eyes = {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}


def eye(value):
    return value in eyes


passport_regex = re.compile("[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]")


def passport_id(value):
    if len(value) != 9:
        return False
    return passport_regex.fullmatch(value) is not None


required_fields = {
    "byr": birth_year,
    "iyr": issue_year,
    "eyr": expr_year,
    "hgt": height,
    "hcl": hair,
    "ecl": eye,
    "pid": passport_id,
}

optional_fields = {
    "cid": "Country ID",
}


class passport:
    def __init__(self):
        self.fields = {}
        self.invalid = False

    def add_fields(self, fields):
        for field in fields:
            field_name = field[0]
            field_value = field[1]
            if field_name in self.fields:
                # probably not relevant
                self.invalid = True
            self.fields[field_name] = field_value

    def is_valid(self):
        if self.invalid:
            print("Special case invalid")
            return False
        for field in required_fields:
            if field not in self.fields:
                return False
            validation = required_fields[field]
            if not validation(self.fields[field]):
                return False
        return True

    def __str__(self):
        return str(self.fields)


def make_passports():
    passports = []
    with open('input.txt', 'r') as file:
        p = passport()
        for line in file.readlines():
            line = line.strip("\n")
            if line == "":
                passports.append(p)
                p = passport()
                continue
            sections = line.split(" ")
            fields = []
            for section in sections:
                fields.append(section.split(":", 2))
            p.add_fields(fields)
        passports.append(p)
    return passports


passports = make_passports()
valid = 0
for p in passports:
    valid += p.is_valid()

print(valid)