import sys
sys.path.append("..")

from ConfigPack.ConfigMod import FMConfigs
from FileManagementPack.DatabaseMod import HighscoreDatabase

"""
	User object created when user is logged in, it allows substates to track the logged in users
"""
class User:

	"""
		Constructor that resets all user parameters
	"""
	def __init__(self):
		self.destroy()

	"""
		Method used to set user parameters for targetted user
	"""
	def create(self, username):
		user = HighscoreDatabase().getStatsOf(username)
		self.username = username
		self.numKills = user[1]
		self.numDeaths = user[2]
		self.levelsCompleted = user[3]
		self.numRestarts = user[4]
		self.currentLevel = user[5]
		self.maxLevelAchieved = user[6]
		self.currNumLives = user[7]

	"""
		Method that resets/overwrites all user parameters to empty strings
	"""
	def destroy(self):
		self.username = ""
		self.numKills = ""
		self.numDeaths = ""
		self.levelsCompleted = ""
		self.numRestarts = ""
		self.currentLevel = ""
		self.maxLevelAchieved = ""
		self.currNumLives = ""

"""
	Class to get logged in users
"""
class AuthInfo:
	user_one = User()
	user_two = User()
