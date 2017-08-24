'''
Created on Apr 10, 2014

@author: Jeffrey
'''
import unittest
from FileManagementPack.FileManagementMod import UserFileManagement


class Test(unittest.TestCase):

    """
    Creates temporary objects for each test iteration, Python convention
    """
    def setUp(self):
        self.user_fm = UserFileManagement()

    """
    Removes temporary objects at end of each test iteration, Python convention
    """
    def tearDown(self):
        self.user_fm = None

    """
    Tests add and remove methods by calling them
    """
    def testAddRemoveUser(self):
        self.user_fm.addUser('test', 'test')
        self.user_fm.removeUser('test')

    """
    Tests getUsers method by creating 2 users and ensuring they're returned in proper order
    """
    def testGetUsers(self):
        self.user_fm.addUser('AUser', 'test')
        self.user_fm.addUser('BUser', 'test')
        users = self.user_fm.getUsers()
        self.assertEqual(users[0][0], 'AUser', 'getUsers failed')
        self.assertEqual(users[1][0], 'BUser', 'getUsers failed')
        self.user_fm.removeUser('AUser')
        self.user_fm.removeUser('BUser')

    """
    Tests addStatistics method by calling it
    """
    def testAddStatistics(self):
        self.user_fm.addUser('test', 'test')
        self.user_fm.addStatistics('test', 1, 2, 3, 4, 5, 6, 7)
        self.user_fm.removeUser('test')

    """
    Tests getStatistics method by creating a user with stats and ensuring they're returned properly
    """
    def testGetStatistics(self):
        self.user_fm.addUser('test', 'test')
        self.user_fm.addStatistics('test', 1, 2, 3, 4, 5, 6, 7)
        stats = self.user_fm.getStatistics()
        self.assertEqual(stats[0][0], 'test', 'getStatistics failed')
        self.assertEqual(stats[0][1], '1', 'getStatistics failed')
        self.assertEqual(stats[0][2], '2', 'getStatistics failed')
        self.assertEqual(stats[0][3], '3', 'getStatistics failed')
        self.assertEqual(stats[0][4], '4', 'getStatistics failed')
        self.assertEqual(stats[0][5], '5', 'getStatistics failed')
        self.assertEqual(stats[0][6], '7', 'getStatistics failed')
        self.assertEqual(stats[0][7], '7', 'getStatistics failed')
        self.user_fm.removeUser('test')

    """
    Tests _removeStatisticsOf method by creating user with stats then removing them and
    ensuring different stats are returned before and after removal
    """
    def testRemoveStatisticsOf(self):
        self.user_fm.addUser('test', 'test')
        self.user_fm.addStatistics('test', 1, 2, 3, 4, 5, 6, 7)
        stats1 = self.user_fm.getStatistics()
        self.user_fm._removeStatisticsOf('test')
        stats2 = self.user_fm.getStatistics()
        self.assertNotEqual(stats1, stats2, '_removeStatisticsOf failed')
        self.user_fm.removeUser('test')

    """
    Tests updateStatistics method by creating a user with stats and then updating them
    and ensuring different stats are returned before and after updating
    """
    def testUpdateStatistics(self):
        self.user_fm.addUser('test', 'test')
        self.user_fm.addStatistics('test', 1, 2, 3, 4, 5, 6, 7)
        stats1 = self.user_fm.getStatistics()
        self.user_fm.updateStatistics('test', 2, 3, 4, 5, 6, 7, 7)
        stats2 = self.user_fm.getStatistics()
        for i in range(1, 6):
            self.assertGreater(stats2[0][i], stats1[0][i], 'updateStatistics failed')
        #max num lives is 7 so check separately
        self.assertEqual(stats2[0][7], stats1[0][7], 'updateStatistics failed')
        self.user_fm.removeUser('test')



"""
Allows Test Runner, Python convention
"""
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()