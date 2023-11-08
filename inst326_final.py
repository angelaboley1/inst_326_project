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
        
#My Tran Nov 10 Update


def can_play_card(hand, top_of_deck):
    '''
    checks if any card in hand can be played given the card on top of the deck
    '''
    for card in hand:
        if card.color == top_of_deck.color:
            return True
        if card.rank == top_of_deck.rank:
            return True
        if "Wild" in card.rank:
            return True
        else:
            return False
        
#a function about playing card
    if can_play_card(hand, top_of_deck):
    else:
        raise ValueError("Player must draw a card")
    
    
# Angela Nov. 10th
class GameState:
    def __init__(self, players_name, players_cards, top_card, ):
        self.players_names = players_name
        self.players_card = players_cards
        self.top_card = top_card
    def __str__(self):
        return f"{self.players_name} cards: {self.players_cards} \n
                The top card is {self.top_card} \n 
                {self.players_name}, it's your turn! What do you want to play?"