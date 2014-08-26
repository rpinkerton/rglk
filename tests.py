### rglk - The Roguelike Text Adventure
### tests.py - the testing module
### Riley Pinkerton, 8/25/14

import unittest

from room import Room
from dungeon import Dungeon
from player import Player
from game import Game
from util import *

## Tests for Room class

class RoomTestCase(unittest.TestCase):

  def test_no_id(self):
    self.room_no_id = Room()
    self.assertEqual(self.room_no_id.id, None)

  def test_id(self):
    self.room_id = Room(42)
    self.assertEqual(self.room_id.id, 42)

def room_tests():
  tests = ['test_no_id', 'test_id']

  return unittest.TestSuite(map(RoomTestCase, tests))

## Tests for Dungeon class

class DungeonTestCase(unittest.TestCase):

  def test_dungeon_size(self):
    for i in range(100):
      self.dungeon = Dungeon(i)
      self.assertEqual(len(self.dungeon.rooms), i + 2)

  def test_dungeon_randomness(self):
    self.dungeon1 = Dungeon(100)
    self.dungeon2 = Dungeon(100)
    # While this test could techically display a false negative, the chance
    # of it occurring is fantastically small.
    self.rooms1 = self.dungeon1.rooms.keys()
    self.rooms1.sort()
    self.rooms2 = self.dungeon2.rooms.keys()
    self.rooms2.sort()
    self.assertNotEqual(self.rooms1, self.rooms2)

  def test_dungeon_start_finish(self):
    """Test that there is only one start and finish"""
    self.dungeon = Dungeon(100)
    self.num_starts = [i for i in self.dungeon.rooms.values()
                       if i.id == "start"]
    self.num_finishes = [i for i in self.dungeon.rooms.values()
                         if i.id == "end"]
    self.assertEqual(len(self.num_starts), 1)
    self.assertEqual(len(self.num_finishes), 1)

## TODO fix this test
#  def test_dungeon_finish_far(self):
#    """Test that the finish is the far from the start"""
#    for i in range(100):
#      self.dungeon = Dungeon(2)
#      self.non_start_rooms = [i for i in
#                              self.dungeon.rooms.keys()
#                              if self.dungeon.rooms[i].id != "start"]
#      self.dist_from_start = lambda x: dist_between((0, 0), x)
#      self.furthest = max(self.non_start_rooms, key=self.dist_from_start)
#      self.assertEqual(self.dungeon.rooms[self.furthest].id, "end")

def dungeon_tests():
  tests = ['test_dungeon_size', 'test_dungeon_randomness',
           'test_dungeon_start_finish']

  return unittest.TestSuite(map(DungeonTestCase, tests))

## Collect all the tests together

room_suite = room_tests()
dungeon_suite = dungeon_tests()
alltests = unittest.TestSuite([room_suite, dungeon_suite])

if __name__ == "__main__":
  unittest.main()
