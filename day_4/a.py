required_fields = {
    "byr": "Birth Year",
    "iyr": "Issue Year",
    "eyr": "Expiration Year",
    "hgt": "Height",
    "hcl": "Hair Color",
    "ecl": "Eye Color",
    "pid": "Passport ID",
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