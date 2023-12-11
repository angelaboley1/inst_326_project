"""Play a game of Uno."""

import random
import argparse
import sys
import re


class Cards:
   """A class of Uno cards."""
   def __init__(self):
       """Initializes a Cards object.
       
       Side effects:
            Sets the 'colors', 'types', and 'wild' attributes.
       """
       self.colors = ["Red", "Yellow", "Blue", "Green"]
       self.types = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'Reverse', 'Draw2', 'Skip']
       self.wild = ['Wild Card', 'Wild Draw4']
       

class Deck(Cards):
    """A class to make the deck of Uno cards."""
    def __init__(self):
       """Initializes a Deck object.
       
       Side effects:
            Inherits the 'colors', 'types', and 'wild' attributes from the Card class 
                using super() and sets the 'deck' attribute.
        """
       self.deck = []
       super().__init__()
    
    def deck_info(self):
       """Creates an Uno deck.

       Side effects:
           Changes the value of the 'deck' attribute.

       Returns:
           list: a list of the Uno cards.
       """
       for color in self.colors:
           for types in self.types:
               card_info = "{} {}".format(color, types)
               self.deck.append(card_info)
               if types != 0:
                   self.deck.append(card_info)
       self.deck.extend(self.wild * 4)
       return self.deck
   
    def shuffle_deck(self):
        """Shuffles the deck of cards.

        Side effects:
            Changes the value of the 'deck' attribute.

        Returns:
            list: a list of the shuffled cards.
        """
        random.shuffle(self.deck)
        return self.deck
    
    def __repr__(self):
        """Formal representation of the Deck.
        
        Returns:
            str: a string containing the current cards in the deck.
        """
        print(f"Deck: {self.deck}")


def end_game(hands):
   """Calculates each player's final score.
 
   Args:
       hands (dict): a dictionary containing the players' number (key) and
           their hand of cards (value, a list).
 
   Returns:
       list: list of tuples (player number, final score).
   """
   final_scores = {player:len(hands[player]) for player in hands}
   ranks = sorted(final_scores.items(), key= lambda c: c[1])
   return ranks


def print_ranks(hands):
   """Prints out player place and their final score.
 
   Side effects:
       Prints to stdout -- the players in rank order, based on their final scores.
   """
   final_ranks = end_game(hands)
   place = 0
   for player in final_ranks:
       place += 1
       print(f"{place}. Player {player[0] + 1} with {player[1]} points")
