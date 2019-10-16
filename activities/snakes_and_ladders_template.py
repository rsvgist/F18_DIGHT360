"""Play Snakes and Ladders."""

import random

# Snakes and Ladders dictionary
SaLdic = {6: 17,
          14: 3,
          20: 15,
          24: 26,
          30: 44,
          39: 33,
          49: 62,
          66: 53,
          69: 58,
          79: 67,
          82: 86,
          84: 71,
          88: 36,
          }


# Make a class (object) called Player
class Player:
    def __init__(self, name, position):
        self.name = name
        self.position = position
        
# Each player begins at position 1
p1 = Player('p1',position = 1)
# First player to get to 90 newlines


# Ask for input: how many players?
num_players = int(input('How many players are playing today?'))
# At each player's turn, have the player press [return] to roll

build players

roll the dice

def roll_die():
    return random.randint(1,6)

print(roll)

while position < 10:


#check dict




# Everything else should run automatically
# When a player reaches 90, declare the winner
