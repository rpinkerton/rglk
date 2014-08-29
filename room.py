### rglk - The Roguelike Text Adventure
### room.py - the main room class
### Riley Pinkerton, 8/29/14

class Room:

  def __init__(self, _id=None):
    self.id = _id
    self.doors = {'n':None, 's':None, 'e':None, 'w':None}

  def add_door(self, door, direc):
    """Adds a door at direction direc"""
    self.doors[direc] = door
