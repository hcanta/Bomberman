'''
Created on Apr 10, 2014

@author: Jeffrey
'''
import unittest
from GamePack.PlayerMod import Player
from FileManagementPack.DatabaseMod import UserDatabase


class Test(unittest.TestCase):


    """
    Creates temporary objects for each test iteration, Python convention
    """
    def setUp(self):
        self.player = Player(1, 'test', 0)

    """
    Removes temporary objects at end of each test iteration, Python convention
    """
    def tearDown(self):
        self.player = None

    """
    Tests get and set lives methods
    """
    def testGetSetLives(self):
        self.assertEqual(self.player._getLives(), 3, '_getLives failed')
        self.player._setLives(1)
        self.assertEqual(self.player._getLives(), 1, '_setLives failed')

    """
    Tests _isVulnerable method by ensuring it returns the proper type/value
    """
    def testIsVulnerable(self):
        self.assertEqual(self.player._isVulnerable(), self.player._invulnerablePulse == 45, '_isVulnerable failed')

    """
    Tests _getInvulnerablePulse method by ensuring it returns proper value
    """
    def testGetInvulnerablePulse(self):
        self.assertEqual(self.player._getInvulnerablePulse(), 45, '_getInvulnerablePulse failes')

    """
    Tests the resetInvulnerablePulse and getInvulnerable pulse methods
    """
    def testResetPulseInvulnerable(self):
        self.player._resetInvulnerablePulse()
        self.assertEqual(self.player._getInvulnerablePulse(), 0, '_resetInvulnerablePulse failed')
        self.player._pulseInvulnerable()
        self.assertEqual(self.player._getInvulnerablePulse(), 1, '_pulseInvulnerablePulse failed')

    """
    Tests the getter and setter for tile ID
    """
    def testGetSetTileID(self):
        self.assertEqual(self.player._getTileID(), 0, '_getTileID failed')
        self.player._setTileID(7)
        self.assertEqual(self.player._getTileID(), 7, "_setTileId failed")

    """
    Tests getter for state by calling it
    """
    def testGetState(self):
        self.assertEqual(self.player._getState(), 'U1', '_getState failed')

    """
    Tests goLeft method by ensuring it works for all cases
    """
    def testGoLeft(self):
        self.player._goLeft()
        self.assertEqual(self.player._getState(), 'L1', '_goLeft failed')
        self.player._goLeft()
        self.assertEqual(self.player._getState(), 'L2', '_goLeft failed')
        self.player._goLeft()
        self.assertEqual(self.player._getState(), 'L1', '_goLeft failed')

    """
    Tests goRight method by ensuring it works for all cases
    """
    def testGoRight(self):
        self.player._goRight()
        self.assertEqual(self.player._getState(), 'R1', '_goRight failed')
        self.player._goRight()
        self.assertEqual(self.player._getState(), 'R2', '_goRight failed')
        self.player._goRight()
        self.assertEqual(self.player._getState(), 'R1', '_goRight failed')

    """
    Tests goUp method by ensuring it works for all cases
    """
    def testGoUp(self):
        self.player._goRight()
        self.player._goUp()
        self.assertEqual(self.player._getState(), 'U1', '_goUp failed')
        self.player._goUp()
        self.assertEqual(self.player._getState(), 'U2', '_goUp failed')
        self.player._goUp()
        self.assertEqual(self.player._getState(), 'U1', '_goUp failed')

    """
    Tests goUp method by ensuring it works for all cases
    """
    def testGoDown(self):
        self.player._goDown()
        self.assertEqual(self.player._getState(), 'D1', '_goDown failed')
        self.player._goDown()
        self.assertEqual(self.player._getState(), 'D2', '_goDown failed')
        self.player._goDown()
        self.assertEqual(self.player._getState(), 'D1', '_goDown failed')

    """
    Tests getNextState method
    """
    def testGetNextState(self):
        self.player._getNextState()
        self.assertEqual(self.player._getState(), 'U2', '_getNextState failed' )

    """
    Tests getter for Player ID
    """
    def testGetID(self):
        self.assertEqual(self.player._getID(), 1, '_getID failed')

    """
    Tests getter for max # of bombs
    """
    def testGetNbBombMax(self):
        self.assertEqual(self.player._getNbBombMax(), 1, '_getNbBombMax failed')

    """
    Tests getter for # of bombs placed
    """
    def testGetNbBombPlaced(self):
        self.assertEqual(self.player._getNbBombPlaced(), 0, '_getNbBombsPlaced failed')

    """
    Tests canPlaceBomb method
    """
    def testCanPlaceBomb(self):
        self.assertTrue(self.player._canPlaceBomb(), '_canPlaceBomb failed')

    """
    Tests increase and decrease BombMax methods
    """
    def testIncreaseDecreaseBombMax(self):
        self.player._increaseBombMax()
        self.assertEqual(self.player._getNbBombMax(), 2, '_increaseBombMax failed')
        self.player._decreaseBombMax()
        self.assertEqual(self.player._getNbBombMax(), 1, '_decreaseBombMax failed')

    """
    Tests increase and decrease BombPlaced methods
    """
    def testIncreaseDecreaseBombPlaced(self):
        self.player._increaseBombPlaced()
        self.assertEqual(self.player._getNbBombPlaced(), 1, '_increaseBombPlaced failed')
        self.player._decreaseBombPlaced()
        self.assertEqual(self.player._getNbBombPlaced(), 0, '_decreaseBombPlaced failed')

    """
    Tests getters and setters for X and Y coordinates
    """
    def testGetSetXY(self):
        self.assertEqual(self.player._getX(), 0, '_getX failed')
        self.assertEqual(self.player._getY(), 0, '_getY failed')
        self.player._setX(10)
        self.player._setY(5)
        self.assertEqual(self.player._getX(), 10, '_setX failed')
        self.assertEqual(self.player._getY(), 5, '_setY failed')

    """
    Tests getter for number of deats
    """
    def testGetNbDeath(self):
        self.assertEqual(self.player._getNbDeath(), 0, '_getNbDeath failed')

    """
    Tests kills getter and addKill methods
    """
    def testGetAddKills(self):
        self.assertEqual(self.player._getNbKills(), 0, '_getNbKills failed')
        self.player._addToKills()
        self.assertEqual(self.player._getNbKills(), 1, '_addToKills failed')

    """
    Tests bomb range getter and increase and decrease methods
    """
    def testGetIncreaseDecreaseBombRange(self):
        self.assertEqual(self.player._getBombRange(), 1, '_getBombRange failed')
        self.player._increaseRange()
        self.assertEqual(self.player._getBombRange(), 2, '_increaseRange failed')
        self.player._decreaseRange()
        self.assertEqual(self.player._getBombRange(), 1, '_decreaseRange failed')

    """
    Tests increase and decrease LivesMax methods
    """
    def testIncreaseDecreaseLivesMax(self):
        self.user_database = UserDatabase()
        self.user_database.addUser('test', 'test')
        self.player._increaseLives()
        self.assertEqual(self.player._getLives(), 4, '_increaseLives failed')
        self.player._decreaseLives()
        self.assertEqual(self.player._getLives(), 3, '_decreaseLives failed')
        self.user_database.removeUser('test')

    """
    Tests isDeadGameOver to ensure it only returns true if the user has 0 lives
    """
    def testIsDeadGameOver(self):
        self.assertFalse(self.player._isDeadGameOver(), '_isDeadGameOver failed')
        self.player._setLives(0)
        self.assertTrue(self.player._isDeadGameOver(), '_isDeadGameOver failed')



"""
Allows Test Runner, Python convention
"""
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()