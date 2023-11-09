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