### rglk - The Roguelike Text Adventure
### util.py - the utility and debugging functions
### Riley Pinkerton, 8/29/14

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

def adjacent_locs(loc):
  """Return a list of cardinally adjacent locaitons to loc"""
  x = loc[0]
  y = loc[1]
  # Note that the order is important here, as we're zipping these with direction
  # names in the dungeon class
  return [(x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y)]

def opposite_direc(direc):
  """Returns the opposite cardinal direction"""
  if direc == 'n':
    return 's'
  elif direc == 's':
    return 'n'
  elif direc == 'w':
    return 'e'
  elif direc == 'e':
    return 'w'
