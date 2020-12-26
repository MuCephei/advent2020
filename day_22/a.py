class combat:

    def __init__(self, deck_a, deck_b):
        self.deck_a = deck_a
        self.deck_b = deck_b

    def play_round(self):
        a, b = self.deck_a.pop(0), self.deck_b.pop(0)
        if a > b:
            winner = self.deck_a
        else:
            winner = self.deck_b
        winner.append(a if a > b else b)
        winner.append(a if a < b else b)

    def over(self):
        return len(self.deck_a) == 0 or len(self.deck_b) == 0

    def score(self):
        winner = self.deck_a if len(self.deck_a) > len(self.deck_b) else self.deck_b
        multiplier = 1
        total = 0
        for x in winner[::-1]:
            total += x * multiplier
            multiplier += 1
        return total


    def __repr__(self):
        return "%s VS %s" % (self.deck_a, self.deck_b)

def deal_cards():
    with open('input.txt', 'r') as file:
        decks = [[], []]
        for x in range(2):
            _ = file.readline()
            line = file.readline().strip("\n")
            while line != "":
                decks[x].append(int(line))
                line = file.readline().strip("\n")
    return combat(decks[0], decks[1])

fight = deal_cards()
while not fight.over():
    fight.play_round()
print(fight.score())


