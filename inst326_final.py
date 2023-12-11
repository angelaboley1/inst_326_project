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



def play(turn, hands, discards, direction, shuffled_deck, num_players):
   """Player taking a turn.
 
   Args:
       turn (int):
       shuffled_deck (list): a shuffled deck of Uno cards.
       hands (dict): a dictionary containing the players' number (key) and
           their hand of cards (value, a list).
       discards (list): list of cards in the discard pile.
       direction (int): defines the direction the game moves among players.
       num_players (int): the number of players.
     
   Side effects:
       Prints to stdout.
   """
   while True:
     
       if len(hands[turn]) == 0:
           print(f"Player {turn + 1} won!")
           print_ranks(hands)
           break
       else:
           print(f"It's now Player {turn + 1}'s turn!")
           print(f"These are your cards:")
           i = 1
           for card in hands[turn]:
               print(f"{i}. {card}")
               i += 1
           print("\n")
           print(f"Top Card: {discards[-1]}")
         
           x = choice(len(hands[turn]))
           if x == "draw":
               draw(shuffled_deck,discards,hands,turn,num_players)
           else:
               selected_card = (hands[turn])[x-1]
               print(selected_card)
               if can_play_card(selected_card, discards[-1]) is True:
                   if "Reverse" in selected_card:
                       direction *= -1
                       discards.append((hands[turn]).pop(int(x) -1))
                   elif "Skip" in selected_card:
                       discards.append((hands[turn]).pop(int(x) -1))
                       turn = (turn + 2*direction) % num_players
                   elif "Draw2" in selected_card:
                       next_player = (turn + 1) % num_players
                       hands[next_player].extend(deal(shuffled_deck, 2))
                       discards.append((hands[turn]).pop(int(x) -1))
                   elif "Wild Card" in selected_card:
                       colors = {1:"Blue Wild", 2:"Red Wild", 3:"Green Wild", 4:"Yellow Wild"}
                       for i in colors:
                           print(f"{i}. {colors[i]}")
                           i += 1
                       t= wildChoice(colors)
                       (hands[turn]).pop(int(x) -1)
                       discards.append(colors[int(t)])


                   elif "Wild Draw4" in selected_card:
                       colors = {1:"Blue Wild", 2:"Red Wild", 3:"Green Wild", 4:"Yellow Wild"}
                       for i in colors:
                           print(f"{i}. {colors[i]}")
                           i += 1
                       t = wildChoice(colors)
                       (hands[turn]).pop(int(x) -1)
                       discards.append(colors[int(t)])
                       next_player = (turn + 1) % num_players
                       hands[next_player].extend(deal(shuffled_deck, 4))
                   else:
                       discards.append((hands[turn]).pop(int(x) -1))
                 
                   print("Uno" if len(hands[turn]) == 1 else "The game continues...")
                     
                   if "Skip" not in selected_card:
                       turn = (turn + direction) % num_players
               else:
                   print("You can't play that card. Please pick another card or draw.")
  
def main(num_players):
   """Runs the Uno game.
 
   Args:
       num_players (int): the number of players for the Uno game.
 
   Side effects:
       Writes to stdout (see play() function).
   """
   while num_players < 2 or num_players > 4:
       num_players = int(input("Invalid. Please enter a number between 2-4. How many players? "))


   turn= 0
   direction = 1
   cards = Cards()
   deck = Deck()
   unshuffled_deck = deck.deck_info()
   shuffled_deck = deck.shuffle_deck()
   hands = {}
 
   for player in range(num_players):
       hands[player]=deal(shuffled_deck, num_cards=5)
     
   discards = []
   discards.append(shuffled_deck.pop(0))
 
   if "Wild" in discards[0]:
       discards[0] = "Blue 4"
     
   play(turn, hands, discards, direction, shuffled_deck, num_players)


def parse_args(arglist):
   """Parse and validate command-line arguments for Uno game.
  Args:
      arglist (list of str): list of command-line arguments.
  Returns:
      namespace: parsed arguments.
  """
   parser = argparse.ArgumentParser(description='Play a game of Uno.')
   parser.add_argument('num_players', type=int, choices=range(2, 5),
                       help='Number of players (between 2 and 4)')
   return parser.parse_args(arglist)


if __name__ == "__main__":
   args = parse_args(sys.argv[1:])
   main(args.num_players)
