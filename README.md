# **INST326 Final Project**
## Purpose of each file in the repository:
1. inst326_final.py: file needed to run/play a game of Uno
2. README.md: documentation of the code

## Instructions on how to run:
1. Open up a new VS code or Python terminal
    - Make sure your terminal is opened in the directory where your Python file is located
2. In the command line, type in Python (Windows) or Python3 (Mac)
3. Type in the file name ("inst326_final.py) and how many players you want to play with (2-4)
    - Example: python inst326_final.py 3

## Instructions on how to use the program and interpret the output of the program:
1. Uno rules: 
    - Match and play cards based on number or color
    - Keep drawing until you get a card that you can play
    - Player who runs out of cards first wins! The players are ranked based on their number of cards at game end – lowest wins.
    - Default number of cards dealt to each person is 7
2. Follow the instructions in the terminal
    - Choose the card that you want to play based on your hand of cards
    - If you don’t have a card that you can play, draw a card until you get one you can play
3. Keep playing until someone runs out of cards!

## Attribution
| Method/Function | Primary Author | Techniques Demonstrated |
| --------------- | -------------- | ----------------------- |
| Deck.__init__ method| Katy Lamb     | Inheritance   |
| Deck.__repr__ method    | Erin Keane     | Magic Method(formal rep.)|
|deal  |  My Tran | List Comprehension |
|can_play_card  | My Tran | Sequence Unpacking |
| end_game | Katy Lamb | Key Function with sorted() |
| print_ranks | Erin Keane | f-string |
|draw | Angela Boley | Optional Parameter |
| choice | Angela Boley |                  |
| wildChoice | Angela Boley | Regular Expression |
| play | Josie Whittington | Conditional Expression |
| main | Josie Whittington |                        |
| parse_args | Josie Whittington | ArgumentParser |

## Annotated Bibliography
“UNO! Rules.” Official Game Rules, https://www.officialgamerules.org/uno. Accessed 11 December 2023.
	This source provided us with rules for the game Uno. We did adapt some of our own house rules. However, we used a lot of these rules to develop our code and create a working game. 
