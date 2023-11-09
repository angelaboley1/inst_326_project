"""Play a game of Uno."""

import cards
import random
import sys

class GameState:
    def __init__(self):
        self.number = None
        self.color = None

class Player_turn:
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand

    def player_turn(self, state):
        hand = [card for card in self.hand]
        print(f"{self.name}, these are the cards in your hand: {hand}")
        
        # create a gamestate class
        print(f"Gamestate: {state.card}")

        play_color = input("What color card do you want to play: ")
        play_num = input("What number card do you want to play: ")
        
        played_card = f'{play_color} {play_num}'

        if played_card in self.hand:
            self.hand.remove(played_card)
            state.card = played_card
            return f"{self.name} played a {played_card}."
        else:
            raise ValueError("You can't play this card.")
            
class Computer:
    def __init(self, computer):
        self.computer = computer

#Erin Nov.10th
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
    #discard_pile = [ ]
    #for #playerturn in #turn function:
        #discard_pile.append[#card]
    #if len(discard_pile) == 112:
        #shuffle_deck(discard_pile)


#My Nov.10th
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
        ...
    else:
        raise ValueError("Player must draw a card")


#Angela Nov.10th
class GameState:
    def __init__(self, players_name, players_cards, top_card, ):
        self.players_names = players_name
        self.players_card = players_cards
        self.top_card = top_card
    def __str__(self):
        return f"{self.players_name} cards: {self.players_cards} \n
                The top card is {self.top_card} \n 
                {self.players_name}, it's your turn! What do you want to play?"


#Katy Nov.10th
#end_game func used sample dict:
player_hands = {
    "player1": ["2", "3", "7"],
    "player2": [],
    "player3": ["5", "9", "Skip"]
}

def end_game(dict):
    """Calculates each player's final score."""
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
    """Prints out player place and their final score."""
    place = 0
    for player in list:
        place += 1
        print(f"{place}. {player[0]} with {player[1]} points")