'''
Created on Apr 11, 2014

@author: Jeffrey
'''
import unittest
from GamePack.TileMod import Tile
from ConfigPack.ConfigMod import GameConfigs


class Test(unittest.TestCase):

    """
    Creates temporary objects for each test iteration, Python convention
    """
    def setUp(self):
        self.tile = Tile(0, "B0")
    """
    Removes temporary objects at end of each test iteration, Python convention
    """
    def tearDown(self):
        self.tile = None

    """
    Tests getter and setter for next content on tile
    """
    def testGetSetNextContent(self):
        self.assertEqual(self.tile._getContent(), "B0", '_getContent failed')
        self.assertEqual(self.tile._getNextContent(), GameConfigs.EMPTY, '_getNextContent failed')
        self.tile._setNextContent("B3")
        self.assertEqual(self.tile._getNextContent(), "B3", '_setNextContent failed')

    """
    Tests setter and isWalkable methods
    """
    def testIsSetWalkable(self):
        self.assertTrue(self.tile._isWalkable(), '_isWalkable failed')
        self.tile._setWalkable(False)
        self.assertFalse(self.tile._isWalkable(), '_setWalkable failed')

    """
    Tests getter for tile ID
    """
    def testGetID(self):
        self.assertEqual(self.tile._getId(), 0, '_getID failed')


"""
Allows Test Runner, Python convention
"""
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()