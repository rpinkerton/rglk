### rglk - The Roguelike Text Adventure
### dungeon.py - the dungeon class
### Riley Pinkerton, 8/22/14

import random

from room import Room
from util import *

class Dungeon:

  def __init__(self, num_rooms):
    self.rooms = {}

    # Set the initial room at (0, 0)
    self.rooms[(0, 0)] = Room("start")

    # Now keep picking random rooms and branching off them with new rooms.
    for i in range(num_rooms):
      curr_room_loc = random.choice(list(self.rooms))
      self.add_random_room(curr_room_loc)

    # Make the finishing room far away from the starting room
    max_dist_room = max(list(self.rooms),
                        key=(lambda x: dist_between(x, (0, 0))))
    self.add_random_room(max_dist_room, "end")

  def add_random_room(self, loc, _id=None):
    """Adds a randomly adjacent room to a given location, with a given id if
       supplied.
    """
    possible_direcs = []
    direc_funcs = [get_north, get_south, get_east, get_west]
    for direc in direc_funcs:
      if direc(loc) not in self.rooms:
        possible_direcs.append(direc)
    if possible_direcs != []:
      new_direc = random.choice(possible_direcs)
      self.rooms[new_direc(loc)] = Room(_id)
    # Otherwise go in a random direction and try again
    else:
      random_direc = random.choice(direc_funcs)
      add_random_room(self, random_direc(loc), _id)
