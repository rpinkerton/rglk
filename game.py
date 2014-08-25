### rglk - The Roguelike Text Adventure
### game.py - the main game class
### Riley Pinkerton, 8/22/14

from player import Player
from dungeon import Dungeon


# Number of additional rooms besides the first and last rooms
NUM_ROOMS = 10

class Game:

  def __init__(self):
    # The dungeon is a map from cartesian locations to rooms
    self.dungeon = Dungeon(NUM_ROOMS)

  def play(self):
    """Actually play the game"""
    print "Game running!"
