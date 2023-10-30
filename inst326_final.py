
class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def player_turn(self, card, game):
        played_cards = []
        if card in self.hand:
            self.hand = [c for c in self.hand if c != card]
            game.played_cards.append(card)
            print(f"{self.name} played {card}.")
        else:
            print(f"{self.name} does not have a {card}.")
