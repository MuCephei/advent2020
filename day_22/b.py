class combat:

    def __init__(self, deck_a, deck_b):
        self.decks = [deck_a.copy(), deck_b.copy()]
        self.winner = None
        self.previously_played = set()

    def play_round(self):
        configuration = (".".join([str(x) for x in self.decks[0]]), ".".join([str(x) for x in self.decks[1]]))
        if configuration in self.previously_played:
            self.winner = 0
            return self.winner
        self.previously_played.add(configuration)
        a, b = self.decks[0].pop(0), self.decks[1].pop(0)
        if len(self.decks[0]) >= a and len(self.decks[1]) >= b:
            fight = combat(self.decks[0][:a], self.decks[1][:b])
            while not fight.over():
                fight.play_round()
            winner = fight.winner
        else:
            if a > b:
                winner = 0
            else:
                winner = 1
        self.decks[winner].append(a if winner == 0 else b)
        self.decks[winner].append(a if winner == 1 else b)
        if len(self.decks[self.other_player(winner)]) == 0:
            self.winner = winner
        return winner

    def other_player(self, me):
        return 0 if me else 1

    def over(self):
        return self.winner is not None

    def score(self):
        winning_deck = self.decks[self.winner]
        multiplier = 1
        total = 0
        for x in winning_deck[::-1]:
            total += x * multiplier
            multiplier += 1
        return total


    def __repr__(self):
        return "%s VS %s" % (self.decks[0], self.decks[1])

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


