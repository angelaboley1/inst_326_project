"""Play a game of Uno."""

import cards
import random
import sys

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def player_turn(self, card, game):
        played_cards = [] 
        if card in self.hand:
            self.hand = [c for c in self.hand if c != card]
            played_cards.append(card)
            print(f"{self.name} played {card}.")
        else:
            print(f"{self.name} does not have a {card}.")
            
class Computer:
    def __init(self, computer):
        self.computer = computer

class Cards:
    def __init__(self, color, number, wild):
        self.color = color 
        self.number = number 
        self.wild = wild 
def deck_info(self):
    color = ["Red", "Yellow", "Blue", "Green"]
    type = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'Reverse', 'Draw Two', 'Skip']
    wild = ['Wild Card', 'Draw Four']
    deck = []

    for colors in color:
        for types in type:
            card_info = "{} {}".format(colors, types)
            deck.append(card_info)
        for i in range(4):
            deck.append([wild[0]]) 

        return deck

    def shuffle_deck(deck):
        random.shuffle_deck(deck)
   #i think this is how to shuffle the deck through the random function


#def discard_pile():
    #iscard_pile = [ ]
    #for #playerturn in #turn function:
        #discard_pile.append[#card]
    #if len(discard_pile) == 112:
        #reshuffle 