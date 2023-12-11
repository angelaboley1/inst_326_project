


def __repr__(self):
       """Formal representation of the Deck.

       
       Returns:
           str: a string containing the current cards in the deck.
       """
       print(f"Deck: {self.deck}")




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
