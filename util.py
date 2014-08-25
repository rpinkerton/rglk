### rglk - The Roguelike Text Adventure
### util.py - the utility and debugging functions
### Riley Pinkerton, 8/22/14

import math

# Directional functions

def get_north(loc):
  return (loc[0], loc[1] + 1)

def get_south(loc):
  return (loc[0], loc[1] - 1)

def get_east(loc):
  return (loc[0] + 1, loc[1])

def get_west(loc):
  return (loc[0] - 1, loc[1])

def dist_between(loc1, loc2):
  """Get the distance between two points in the dungeon"""
  return math.sqrt((loc1[0] - loc2[0]) ** 2 + (loc1[1] - loc2[1]) ** 2)
