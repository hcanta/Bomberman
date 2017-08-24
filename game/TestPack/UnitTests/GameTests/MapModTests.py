'''
Created on Apr 12, 2014

@author: Jeffrey
'''
import unittest
from GamePack.MapMod import Map

class Test(unittest.TestCase):

    """
    Creates temporary objects for each test iteration, Python convention
    """
    def setUp(self):
        self.map = Map()

    """
    Removes temporary objects at end of each test iteration, Python convention
    """
    def tearDown(self):
        self.map = None

    """
    Tests getBombList and add and remove bomb methods
    """
    def testGetBombListAddRemoveBomb(self):
        self.assertEqual(self.map._getBombList(), [], '_getBombList failed')
        self.map._addBomb('test')
        self.bomb_list = self.map._getBombList()
        self.assertEqual(self.bomb_list[0], 'test', '_addBomb failed')
        self.map._removeBomb('test')
        self.assertEqual(self.map._getBombList(), [], '_removeBomb failed')

    """
    Tests canMoveLeft method for both possible cases
    """
    def testCanMoveLeft(self):
        self.assertFalse(self.map._canMoveLeft(0, 0), '_canMoveLeft failed')
        self.assertTrue(self.map._canMoveLeft(1, 0), '_canMoveLeft failed')

    """
    Tests canMoveRight method for both possible cases
    """
    def testCanMoveRight(self):
        self.assertFalse(self.map._canMoveRight(13, 13), '_canMoveRight failed')
        self.assertTrue(self.map._canMoveRight(0, 0), '_canMoveRight failed')

    """
    Tests canPlaceBomb method
    """
    def testCanPlaceBomb(self):
        self.assertTrue(self.map._canPlaceBomb(0, 0), '_canPlaceBomb failed')

    """
    Tests canMoveUp method for both possible cases
    """
    def testCanMoveUp(self):
        self.assertFalse(self.map._canMoveUp(0, 0), '_canMoveUp failed')
        self.assertTrue(self.map._canMoveUp(13, 13), '_canMoveUp failed')

    """
    Test canMoveDown method for both possible cases
    """
    def testCanMoveDown(self):
        self.assertFalse(self.map._canMoveDown(13, 13), '_canMoveDown failed')
        self.assertTrue(self.map._canMoveDown(0, 0), '_canMoveDown failed')

"""
Allows Test Runner, Python convention
"""
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()