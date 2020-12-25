contains_str = " (contains "

class food:

    def __init__(self, i, a):
        self.allergens = set(a)
        self.ingredients = set(i)

    def copy_allergens(self):
        return self.allergens.copy()

    def copy_ingredients(self):
        return self.ingredients.copy()

    def __repr__(self):
        return str(self.ingredients)

def parse_line(line):
    bracket = line.index(contains_str)
    i = line[:bracket].split()
    a = line[bracket + len(contains_str):-1].split(", ")
    return i, a

def identify(foods, allergens):
    known_allergen_ingredients = {}
    changed = True
    while changed:
        changed = False
        for a in allergens:
            possible_ingredients = None
            for food in foods:
                if a in food.allergens:
                    if not possible_ingredients:
                        possible_ingredients = food.copy_ingredients()
                    possible_ingredients = possible_ingredients.intersection(food.copy_ingredients())
            possible_ingredients = possible_ingredients.difference(set(known_allergen_ingredients.values()))
            if len(possible_ingredients) == 1:
                changed = True
                known_allergen_ingredients[a] = possible_ingredients.pop()
        for a in known_allergen_ingredients.keys():
            if a in allergens:
                allergens.remove(a)
    return known_allergen_ingredients


def shop():
    foods = []
    allergens = set()
    with open('input.txt', 'r') as file:
        for line in file.readlines():
            line = line.strip("\n")
            i, a = parse_line(line)
            foods.append(food(i, a))
            for allergen in a:
                allergens.add(allergen)
    return foods, allergens

foods, allergens = shop()
known_allergen_ingredients = identify(foods, allergens)
allergy_ingredients = set(known_allergen_ingredients.values())
total = 0
for food in foods:
    for i in food.ingredients:
        if i not in allergy_ingredients:
            total += 1
print(total)