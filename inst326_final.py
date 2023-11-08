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
    

#katy lamb nov. 10th update

#end_game func used sample dict:
player_hands = {
    "player1": ["2", "3", "7"],
    "player2": [],
    "player3": ["5", "9", "Skip"]
}

def end_game(dict):
    """Calculates each player's final score.
    
    Args:
        dict (dict): keys = players' names, 
            values = list of cards left in players' hands.
    
    Returns:
        list: list of tuples -- (player, final score), sorted by final score.
    """
    final_scores = {}
    score = 0
    for player in dict:
        if len(dict[player]) >= 1:
            for card in dict[player]:
                score += int(cards.card_points[card])
        else:
            score = 0
        final_scores[player] = score
    ranks = sorted(final_scores.items(), key= lambda c: c[1])
    return ranks


def print_ranks(list): #should use list returned by end_game func
    """Prints out player place and their final score.
    
    Args:
        list (list): list of tuples -- (player, final score), 
            sorted by final score.
    
    Side effects:
        prints to stdout.
    """
    place = 0
    for player in list:
        place += 1
        print(f"{place}. {player[0]} with {player[1]} points")