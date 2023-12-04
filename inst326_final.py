"""Play a game of Uno."""

import cards
import random
import sys

#Erin Nov.10th
class Cards:
    def __init__(self):
        self.deck = []

    def deck_info(self):
        color = ["Red", "Yellow", "Blue", "Green"]
        type = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'Reverse', 'Draw Two', 'Skip']
        wild = ['Wild Card', 'Wild Draw Four']
        for colors in color:
            for types in type:
                card_info = "{} {}".format(colors, types)
                self.deck.append(card_info)
                if type != 0:
                    self.deck.append(card_info)
        self.deck.extend(wild * 4)
        return self.deck

    def shuffle_deck(self):
        random.shuffle(self.deck)
        return self.deck
    
def deal(deck, num_cards=7):
    players_hand = [deck.pop(0) for i in range(num_cards)]
    return players_hand

#My 
def can_play_card(selected_card, top_of_discard):
    '''
    checks if any card in hand can be played given the card on top of the deck
    '''
    Tcolor, Trank = top_of_discard.split(" ")
    if "Wild" in selected_card:
        return True
    else:
        Scolor, Srank = selected_card.split(" ")
        if Scolor == Tcolor:
            return True
        elif Srank == Trank:
            return True
        else:
            return False

hands = {}
num_players = int(input("How many players? Please pick between 2-4."))
while num_players < 2 or num_players > 4:
    num_players = int(input("Invalid. Please enter a number between 2-4. How many players? "))

deck = Cards()
unshuffled_deck = deck.deck_info()
shuffled_deck = deck.shuffle_deck()
for player in range(num_players):
    hands[player]=deal(shuffled_deck)
    
discards = []
discards.append(shuffled_deck.pop(0))

turn= 0


#Katy Nov.10th
#end_game func used sample dict:
# player_hands = {
#     "player1": ["2", "3", "7"],
#     "player2": [],
#     "player3": ["5", "9", "Skip"]
#}

# def end_game(dict):
#     """Calculates each player's final score."""
#     final_scores = {}
#     score = 0
#     for player in dict:
#         if len(dict[player]) >= 1:
#             for card in dict[player]:
#                 score += int(cards.card_points[card])
#         else:
#             score = 0
#         final_scores[player] = score
#     ranks = sorted(final_scores.items(), key= lambda c: c[1])
#     return ranks


# def print_ranks(list): #should use list returned by end_game func
#     """Prints out player place and their final score."""
#     place = 0
#     for player in list:
#         place += 1
#         print(f"{place}. {player[0]} with {player[1]} points")


