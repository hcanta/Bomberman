'''
Created on Apr 10, 2014

@author: Jeffrey
'''
import unittest
from FileManagementPack.DatabaseMod import UserDatabase, HighscoreDatabase


class Test(unittest.TestCase):

    """
    Creates temporary objects for each test iteration, Python convention
    """
    def setUp(self):
        self.user_database = UserDatabase()
        self.highscore_database = HighscoreDatabase()

    """
    Removes temporary objects at end of each test iteration, Python convention
    """
    def tearDown(self):
        self.user_database = None
        self.highscore_database = None

    """
    Tests addUser method by creating a user and checking for it in database
    """
    def testAddUser(self):
        self.user_database.addUser('test', 'test')
        user = ["test", "test"]
        self.assertEqual(self.user_database.getUser('test')[0], user[0], 'addUser failed')
        self.user_database.removeUser('test')


    """
    Ensures password encryption by checking encrypted string vs real string
    """
    def testEncryption(self):
        self.user_database.addUser('test', 'test')
        user = ['test', 'test']
        self.assertNotEqual(self.user_database.getUser('test')[1], user[1], 'Password Encryption Failed')
        self.user_database.removeUser('test')


    """
    Ensures user not in database after removeUser call
    """
    def testRemoveUser(self):
        self.user_database.addUser('test', 'test')
        user = ["test", "test"]
        self.assertEqual(self.user_database.getUser('test')[0], user[0], 'addUser failed')
        self.user_database.removeUser('test')
        self.assertEqual(self.user_database.getUser('test'), None, 'removeUser failed')

        """
    Verifies getUser returns valid users and nothing for invalid ones
    """
    def testGetUser(self):
        self.user_database.addUser('test', 'test')
        user = ['test', 'test']
        self.assertEqual(self.user_database.getUser('test')[0], user[0], 'getUser failed')
        self.assertEqual(self.user_database.getUser('nottest'), None, 'getUser failed')
        self.user_database.removeUser('test')

    """
    Tests verifyUsernameUnique method
    """
    def testVerifyUsernameUnique(self):
        self.user_database.addUser('test', 'test')

        #verifies that a non-unique username is rejected
        self.assertFalse(self.user_database.verifyUsernameUnique('test'), 'Non-Unique Username Allowed')

        #verifies that a unique username is accepted
        self.assertTrue(self.user_database.verifyUsernameUnique('nottest'), 'Unique username rejected')
        self.user_database.removeUser('test')

    """
    Tests getUsersAlphabetically class by creating an A User and B User and assuring they're returned in proper order
    """
    def testGetUsersAlphabetically(self):
        self.user_database.addUser('AUser', 'test')
        self.user_database.addUser('BUser', 'test')
        sorted_database = self.user_database.getUsersAlphabetically(False)
        self.assertEqual(sorted_database[0][0], 'AUser', 'First sorted user incorrect')
        self.assertEqual(sorted_database[1][0], 'BUser', 'Second sorted user incorrect')
        self.user_database.removeUser('AUser')
        self.user_database.removeUser('BUser')

    """
    Ensures valid passwords are confirmed and invalid passwords rejected
    """
    def testIsPasswordValidFor(self):
        self.user_database.addUser('test', 'test')
        self.assertTrue(self.user_database.isPasswordValidFor('test', 'test'), 'Valid Passord Rejected')
        self.assertFalse(self.user_database.isPasswordValidFor('test', 'not test'), 'Invalid Password Accepted')
        self.user_database.removeUser('test')

    """
    Ensures the addStatisticsFor method works by calling it, since no return there can be no assertion
    """
    def testAddStatisticsFor(self):
        number = 1
        self.user_database.addUser('test', 'test')
        self.highscore_database.addStatisticsFor('test', number, number, number, number, number, number, number)
        self.user_database.removeUser('test')

    """
    Tests addNumKillsFor method by calling it
    """
    def testAddNumKillsFor(self):
        self.user_database.addUser('test', 'test')
        self.highscore_database.addNumKillsFor('test', 1)
        self.user_database.removeUser('test')

    """
    Tests addNumDeathsFor method by calling it
    """
    def testAddNumDeathsFor(self):
        self.user_database.addUser('test', 'test')
        self.highscore_database.addNumDeathsFor('test', 1)
        self.user_database.removeUser('test')

    """
    Tests addLevelsCompletedFor method by calling it
    """
    def testAddLevelsCompletedFor(self):
        self.user_database.addUser('test', 'test')
        self.highscore_database.addLevelsCompletedFor('test', 1)
        self.user_database.removeUser('test')

    """
    Tests addNumRestartsFor method by calling it
    """
    def testNumRestartsFor(self):
        self.user_database.addUser('test', 'test')
        self.highscore_database.addNumRestartsFor('test', 1)
        self.user_database.removeUser('test')

    """
    Tests updateCurrentLevelFor method by calling it
    """
    def testUpdateCurrentLevelFor(self):
        self.user_database.addUser('test', 'test')
        self.highscore_database.updateCurrentLevelFor('test', 1)
        self.user_database.removeUser('test')

    """
    Tests updateMaxLevelAchievedFor method by calling it
    """
    def testUpdateMaxLevelAchievedFor(self):
        self.user_database.addUser('test', 'test')
        self.highscore_database.updateMaxLevelAchievedFor('test', 1)
        self.user_database.removeUser('test')

    """
    Tests updateCurrNumLivesFor method by calling it
    """
    def testUpdateCurrNumLivesFor(self):
        self.user_database.addUser('test', 'test')
        self.highscore_database.updateCurrNumLivesFor('test', 1)
        self.user_database.removeUser('test')

    """
    Tests getStatsByUsername by creating two users with clear alphabetic precedence
    and ensuring they are returned in the proper order
    """
    def testGetStatsByUsername(self):
        self.user_database.addUser('AUser', 'test')
        self.user_database.addUser('BUser', 'test')
        sorted_database = self.highscore_database.getStatsByUsername(False)
        self.assertEqual(sorted_database[0][0], 'AUser', 'getStatsByUsername failed')
        self.assertEqual(sorted_database[1][0], 'BUser', 'getStatsByUsername failed')
        self.user_database.removeUser('AUser')
        self.user_database.removeUser('BUser')

    """
    Tests getStatsByNumKills by creating two users with different number of kills and ensuring they are returned properly
    """
    def testGetStatsByNumKills(self):
        self.user_database.addUser('AUser', 'test')
        self.user_database.addUser('BUser', 'test')
        self.highscore_database.addNumKillsFor('AUser', 1)
        self.highscore_database.addNumKillsFor('BUser', 0)
        sorted_database = self.highscore_database.getStatsByNumKills(False)
        self.assertEqual(sorted_database[0][0], 'AUser', 'getStatsByNumKills failed')
        self.assertEqual(sorted_database[0][1], '1', 'getStatsByNumKills failed')
        self.assertEqual(sorted_database[1][0], 'BUser', 'getStatsByNumKills failed')
        self.assertEqual(sorted_database[1][1], '0', 'getStatsByNumKills failed')
        self.user_database.removeUser('A User')
        self.user_database.removeUser('B User')

    """
    Tests getStatsByNumDeaths by creating two users with different number of deaths and
    ensuring they are returned in proper order and stats match
    """
    def testGetStatsByNumDeaths(self):
        self.user_database.addUser('AUser', 'test')
        self.user_database.addUser('BUser', 'test')
        self.highscore_database.addNumDeathsFor('AUser', 1)
        self.highscore_database.addNumDeathsFor('BUser', 0)
        sorted_database = self.highscore_database.getStatsByNumDeaths(False)
        self.assertEqual(sorted_database[0][0], 'AUser', 'getStatsByNumDeaths failed')
        self.assertEqual(sorted_database[0][2], '1', 'getStatsByNumDeaths failed')
        self.assertEqual(sorted_database[1][0], 'BUser', 'getStatsByNumDeaths failed')
        self.assertEqual(sorted_database[1][2], '0', 'getStatsByNumDeaths failed')
        self.user_database.removeUser('AUser')
        self.user_database.removeUser('BUser')

    """
    Tests getStatsByKDR by creating two users with kills and deaths and ensuring they're
    returned in proper order and stats match
    """
    def testGetStatsByKDR(self):
        self.user_database.addUser('AUser', 'test')
        self.user_database.addUser('BUser', 'test')
        self.highscore_database.addNumKillsFor('AUser', 5)
        self.highscore_database.addNumKillsFor('BUser', 3)
        self.highscore_database.addNumDeathsFor('AUser', 1)
        self.highscore_database.addNumDeathsFor('BUser', 1)
        sorted_database=self.highscore_database.getStatsByKDR(False)
        self.assertEqual(sorted_database[0][0],'AUser', 'getStatsByKDR Failed')
        self.assertEqual(sorted_database[1][0],'BUser', 'getStatsByKDR Failed')
        self.user_database.removeUser('AUser')
        self.user_database.removeUser('BUser')

    """
    Tests getStatsByLevelsCompleted by creating two users with different number of levels
    and ensuring they're returned in the proper order stats match
    """
    def testGetStatsByLevelsCompleted(self):
        self.user_database.addUser('AUser', 'test')
        self.user_database.addUser('BUser', 'test')
        self.highscore_database.addLevelsCompletedFor('AUser', 2)
        self.highscore_database.addLevelsCompletedFor('BUser', 1)
        sorted_database=self.highscore_database.getStatsByLevelsCompleted(False)
        self.assertEqual(sorted_database[0][0], 'AUser', 'getStatsByLevelsCompleted failed')
        self.assertEqual(sorted_database[1][0], 'BUser', 'getStatsByLevelsCompleted failed')
        self.assertEqual(sorted_database[0][3], '2', 'getStatsByLevelsCompleted failed')
        self.assertEqual(sorted_database[1][3], '1', 'getStatsByLevelsCompleted failed')
        self.user_database.removeUser('AUser')
        self.user_database.removeUser('BUser')

    """
    Tests getStatsByNumRestarts by creating two users with different number of restarts
    and ensuring they're returned in the proper order and stats match
    """
    def getStatsByNumRestarts(self):
        self.user_database.addUser('AUser', 'test')
        self.user_database.addUser('BUser', 'test')
        self.highscore_database.addNumRestartsFor('AUser', 5)
        self.highscore_database.addNumRestartsFor('BUser', 1)
        sorted_database = self.highscore_database.getStatsByNumRestarts(False)
        self.assertEqual(sorted_database[0][0], 'AUser', 'getStatsByNumRestarts failed')
        self.assertEqual(sorted_database[1][0], 'BUser', 'getStatsByNumRestarts failed')
        self.assertEqual(sorted_database[0][4], '5', 'getStatsByNumRestarts failed')
        self.assertEqual(sorted_database[1][4], '1', 'getStatsByNumRestarts failed')
        self.user_database.removeUser('AUser')
        self.user_database.removeUser('BUser')

    """
    Tests getStatsByMaxLevelAchieved by creating 2 users with different max levels and
    ensuring they're returned in the proper order and stats match
    """
    def testGetStatsByMaxLevelAchieved(self):
        self.user_database.addUser('AUser', 'test')
        self.user_database.addUser('BUser', 'test')
        self.highscore_database.updateMaxLevelAchievedFor('AUser', 5)
        self.highscore_database.updateMaxLevelAchievedFor('BUser', 1)
        sorted_database = self.highscore_database.getStatsByMaxLevelAchieved(False)
        self.assertEqual(sorted_database[0][0], 'AUser', 'getStatsByMaxLevelAchieved failed')
        self.assertEqual(sorted_database[1][0], 'BUser', 'getStatsByMaxLevelAchieved failed')
        self.assertEqual(sorted_database[0][6], '5', 'getStatsByMaxLevelAchieved failed')
        self.assertEqual(sorted_database[1][6], '1', 'getStatsByMaxLevelAchieved failed')
        self.user_database.removeUser('AUser')
        self.user_database.removeUser('BUser')

    """
    Tests getStatsByCurrNumLives by creating 2 users with different number of lives and
    ensuring they're returned in the proper order and stats match
    """
    def testGetStatsByCurrNumLives(self):
        self.user_database.addUser('AUser', 'test')
        self.user_database.addUser('BUser', 'test')
        self.highscore_database.updateCurrNumLivesFor('AUser', 5)
        self.highscore_database.updateCurrNumLivesFor('BUser', 1)
        sorted_database = self.highscore_database.getStatsByCurrNumLives(False)
        self.assertEqual(sorted_database[0][0], 'AUser', 'getStatsByCurrNumLivesFailed')
        self.assertEqual(sorted_database[1][0], 'BUser', 'getStatsByCurrNumLivesFailed')
        self.assertEqual(sorted_database[0][7], '5', 'getStatsByCurrNumLivesFailed')
        self.assertEqual(sorted_database[1][7], '1', 'getStatsByCurrNumLivesFailed')
        self.user_database.removeUser('AUser')
        self.user_database.removeUser('BUser')

    """
    Tests getStatsOf method by creating a user with stats and verifying they're returned correctly
    """
    def testGetStatsOf(self):
        self.user_database.addUser('test', 'test')
        self.highscore_database.addStatisticsFor('test', 1, 2, 3, 4, 5, 6, 7)
        stats = self.highscore_database.getStatsOf('test')
        self.assertEqual(stats[0], 'test', 'getStatsOf failed')
        self.assertEqual(stats[1], '1', 'getStatsOf failed')
        self.assertEqual(stats[2], '2', 'getStatsOf failed')
        self.assertEqual(stats[3], '3', 'getStatsOf failed')
        self.assertEqual(stats[4], '4', 'getStatsOf failed')
        self.assertEqual(stats[5], '5', 'getStatsOf failed')
        self.assertEqual(stats[6], '7', 'getStatsOf failed')
        self.assertEqual(stats[7], '7', 'getStatsOf failed')
        self.user_database.removeUser('test')

    """
    This method tests all the getters, similar to the last test but individually now
    Getters: getNumKillsOf, getNumDeathsOf, getKDROf, getLevelsCompletedOf, getNumRestartsOf,
    getCurrentLevelOf, getMaxLevelAchievedOf, getCurrNumLives
    """
    def testGetters(self):
        self.user_database.addUser('test', 'test')
        self.highscore_database.addStatisticsFor('test', 1, 2, 3, 4, 5, 6, 7)
        self.assertEqual(self.highscore_database.getNumKillsOf('test'), 1, 'getNumKillsOf failed')
        self.assertEqual(self.highscore_database.getNumDeathsOf('test'), 2, 'getNumDeathsOf failed')
        self.assertEqual(self.highscore_database.getKDROf('test'), 0.5, 'getKDROf failed')
        self.assertEqual(self.highscore_database.getLevelsCompletedOf('test'), 3, 'getLevelsCompletedOf failed')
        self.assertEqual(self.highscore_database.getNumRestartsOf('test'), 4, 'getNumRestartsOf failed')
        self.assertEqual(self.highscore_database.getCurrentLevelOf('test'), 5, 'getCurrentLevelOf failed')
        self.assertEqual(self.highscore_database.getMaxLevelAchievedOf('test'),7, 'getMaxLevelAchievedOf failed')
        self.assertEqual(self.highscore_database.getCurrNumLives('test'), 7, 'getCurrNumLives failed')


"""
Allows Test Runner, Python convention
"""
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()