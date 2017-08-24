'''
Created on Apr 11, 2014

@author: Jeffrey
'''
import unittest
from GamePack.BombMod import Bomb


class Test(unittest.TestCase):


    """
    Creates temporary objects for each test iteration, Python convention
    """
    def setUp(self):
        self.bomb = Bomb(0, 'test', 1, 1)


    """
    Removes temporary objects at end of each test iteration, Python convention
    """
    def tearDown(self):
        self.bomb = None

    """
    Tests getter and setter for soundPlayed
    """
    def testGetSoundSetPlayed(self):
        self.assertFalse(self.bomb._getSound(), '_getSound failed')
        self.bomb._setPlayed()
        self.assertTrue(self.bomb._getSound(), '_setPlayed failed')

    """
    Tests getter for tile ID
    """
    def testGetTileID(self):
        self.assertEqual(self.bomb._getTileID(), 0, '_getTileID failed')

    """
    Tests getter for bomb owner
    """
    def testGetOwner(self):
        self.assertEqual(self.bomb._getOwner(), 'test', '_getOwner failed')

    """
    Tests getter for bomb range
    """
    def testGetRange(self):
        self.assertEqual(self.bomb._getRange(), 1, '_getRange failed')

    """
    Tests _explosion and _pulse method
    """
    def testExplosion(self):
        self.assertFalse(self.bomb._explosion(), '_explosion failed')
        self.bomb._pulse()
        self.assertTrue(self.bomb._explosion(), '_pulse failed')

    """
    Tests _doneExlosion and _exploduePulse methods
    """
    def testDoneExplosion(self):
        self.assertFalse(self.bomb._doneExplosion(), '_doneExplosion failed')
        self.bomb._pulse()
        for i in range(0,46):
            self.bomb._explodePulse()
            i+=1
        self.assertTrue(self.bomb._doneExplosion(), '_explodePulse failed')

    """
    Tests getter for bomb tick
    """
    def testGetTick(self):
        self.assertEqual(self.bomb._getTick(), 45, '_getTick failed')


"""
Allows Test Runner, Python convention
"""
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()