from collections import defaultdict

class form:
    def __init__(self):
        self.people = 0
        self.fields = defaultdict(int)
        self.invalid = False

    def add_fields(self, fields):
        self.people += 1
        for field in fields:
            self.fields[field] += 1

    def total(self):
        total = 0
        for f in self.fields:
            if self.fields[f] == self.people:
                total += 1
        return total

    def __str__(self):
        return str(self.fields)

def make_forms():
    forms = []
    with open('input.txt', 'r') as file:
        f = form()
        for line in file.readlines():
            line = line.strip("\n")
            if line == "":
                forms.append(f)
                f = form()
                continue
            f.add_fields(line)
        forms.append(f)
    return forms

forms = make_forms()
total = 0
for f in forms:
    total += f.total()
print(total)
