"""Play a game of Uno."""
import random
import argparse
import sys


class Cards:
    """A class for making a deck of cards. """
    def __init__(self):
        """Initializes a Cards object.
       
        Side effects:
            Creates a 'deck' attribute.
        """
        self.deck = []


    def deck_info(self):
        """Creates an Uno deck.
       
        Side effects:
            Changes the value of the 'deck' attribute.
       
        Returns:
            list: a list of the Uno cards.
        """

        color = ["Red", "Yellow", "Blue", "Green"]
        type = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'Reverse', 'Draw2', 'Skip']
        #type = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        wild = ['Wild Card', 'Wild Draw4']
        for colors in color:
            for types in type:
                card_info = "{} {}".format(colors, types)
                self.deck.append(card_info)
                if type != 0:
                    self.deck.append(card_info)
        self.deck.extend(wild * 4)
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
        """ Formal representation of the Deck.


       Returns:
           str: A string containing the current order of cards in the deck.
       """
        print(f"Deck: {self.deck}")




    
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
    final_scores = {player:len(players[player]) for player in players}
    ranks = sorted(final_scores.items(), key= lambda c: c[1])
    return ranks


def print_ranks():
    """Prints out player place and their final score."""
    final_ranks = end_game(hands)
    place = 0
    for player in final_ranks:
        place += 1
        print(f"{place}. {player[0]} with {player[1]} points")


#Josie Nov.10th        
class PlayerTurn:
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand

    def player_turn(self, state):
        hand = [card for card in self.hand]
        print(f"{self.name}, these are the cards in your hand: {hand}")
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