"""Play a game of Uno."""

import random
import sys

card_points = {
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'Draw 2': 20,
    'Reverse': 20,
    'Skip': 20,
    'Wild': 50,
    'Wild Draw 4': 50
}

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


def end_game(dict):
    """Calculates each player's final score."""
    final_scores = {}
    score = 0
    for player in dict:
        if len(dict[player]) >= 1:
            for card in dict[player]:
                color, value = card.split(" ")
                score += int(card_points[value])
        else:
            score = 0
        final_scores[player] = score
    ranks = sorted(final_scores.items(), key= lambda c: c[1])
    return ranks


def print_ranks():
    """Prints out player place and their final score."""
    final_ranks = end_game(hands)
    place = 0
    for player in final_ranks:
        place += 1
        print(f"{place}. {player[0]} with {player[1]} points")


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

def play(turn, hands, discards):
    while True:


        if len(hands[turn]) == 0:
            print(f"Player {turn + 1} won!")
            print_ranks()
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
           
            try:
                card_number = int(input("What card would you like to play? Select the card number."))
            except:
                print("Pick a number in the specified range.")
           
            selected_card = (hands[turn])[card_number - 1]
            print(selected_card)
            if can_play_card(selected_card, discards[-1]) is True:
                discards.append((hands[turn]).pop(card_number -1))
               
                if len(hands[turn]) == 1:
                    print("Uno!")
                turn = (turn + 1) % num_players
               
            else:
                print("Card cannot be played. Draw a card from the deck")
                print(f"Drew a {shuffled_deck[0]}")
                hands[turn].append(shuffled_deck.pop(0))
                turn = (turn + 1) % num_players


	            
play(turn, hands, discards)


       
#def special_cards(card):
    #if "Reverse" in card:
   
    #elif "Skip" in card:
       
    #elif "Draw Two" in card:
       
    #elif "Wild Card" in card:
       
    #elif "Wild Draw Four" in card: