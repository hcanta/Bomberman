import sys

from FileManagementMod import UserFileManagement
from operator import lt, le, gt, ge, eq, ne

sys.path.append("..")
from ConfigPack.ConfigMod import FMConfigs

""" 
	API to add, get, remove users and statistics. This API also sorts the data with
	the option of reversing the lists. THIS IS THE API to use, never
	use methods directly in FileManagementMod because the goal
	here is to decouple file management from user management. This module
	acts just like a very simple database.
"""

"""
	This is the class to handle users and passwords. You can add and remove users
	from here as well as verify passwords and username uniqueness.
"""
class UserDatabase:

	"""
		This method adds a user to our "database".

		@param username is the username to be added.
		@param password is the password to be encrypted and added.
		@return True or False depending on if the username was unique and/or was 
				of acceptable length(3 < length < 25).
	"""
	def addUser(self, username, password):
		if(username != "" and len(username) < 25 and len(username) > 3):
			if(self.verifyUsernameUnique(username)):
				userFileManagement = UserFileManagement().addUser(username, password)				
				return True
		return False

	"""
		This method removes a user from our "database" as well as its statistics.

		@param username is the username to be removed.
		@return True or False depending on if the user was successfully removed.
	"""
	def removeUser(self, username):
		if(username != ""):
			userFileManagement = UserFileManagement().removeUser(username)
			return True
		return False

	""" 
		This method gets a user [username, encrypted password] from the specified username.

		@param username is the user's username to look for
		@return the user if it exists otherwise return None
	"""
	def getUser(self, username):
		if(username != ""):
			listOfUser = UserFileManagement().getUsers()
			user = filter(lambda x: x[0] == username, listOfUser)
			if(user):
				return user[0]
		return None

	""" 
		This method verifies that the username is unique. 

		@param username is the username to check for.
		@return True iff the username is unique.
	"""
	def verifyUsernameUnique(self, username):
		if(self.getUser(username) == None):
			return True
		return False

	""" 
		This method gets all users as a list of lists and sorts it alphabetically 
		with the option of reversing it.

		@param inverse is a boolean specifying if the usernames should be in alphabetical
			   order or reversed.
		@return the list of all users.
	"""
	def getUsersAlphabetically(self, inverse):
		listOfUser = UserFileManagement().getUsers()
		sortedUsers = sorted(listOfUser, key=lambda x:x[0].lower())
		if(inverse == True):
			return sortedUsers[::-1]
		return sortedUsers

	""" 
		Verify that password is valid for a given username. 

		@param username is the user's username to verify password validity.
		@param password is the input password to verify if valid.
		@return True iff the password is valid.
	"""
	def isPasswordValidFor(self, username, password):
		user = self.getUser(username)
		if(user != None):
			a = "".join([chr(ord(c) + FMConfigs.CAESARCONSTANT) for c in password])
			if(user[1] == a):
				return True
		return False

class MapDatabase:

	"""
		Gets all maps.

		@return all maps.
	"""
	def getMaps(self):
		return UserFileManagement().getMaps()

	"""
		Gets a specific map depending on the value entered.
		Value Entered is a level number (1-x)

		@param number is the map number.

		@return the map.
	"""
	def getMapNo(self, number):
		return self.getMaps()[number-1];

	"""
		Adds a map to the map file, MUST have length 196

		@param map is the map list.
	"""	
	def addMap(self, map):
		if(len(map) == 196):
			UserFileManagement().addMap(map)

"""	
	Highscore API
	Stats are always in the following format
	(username, numKills, numDeaths, levelsCompleted, numRestarts, currentLevel, maxLevelAchieved, currNumLives)
	 0		   1		 2 			3 				 4			  5				6				  7
	
	Can get list of all users based on one stat.
	Can get stat(s) of any user.
	Can filter all users based on one stat condition.

"""

class HighscoreDatabase:

	""" Global users statistics """
	
	"""
		This method adds all statistics to a given username using the filemanagement API.

		@param username is the username who's statistics should be modified.
		@param numKills is the number of kills to be added to the user.
		@param numDeaths is the number of deaths to be added to the user.
		@param levelsCompleted is the number of levels the user has completed in total.
		@param numRestarts is the number of time a user has restarted all the levels.
		@param currentLevel is the current level the user is at without losing all its lives.
		@param maxLevelAchieved is the max level the user has ever achieved.
		@param currNumLives is the number of lives th user has left in order to beat all levels.
	"""
	def addStatisticsFor(self, username, numKills, numDeaths, levelsCompleted, numRestarts, currentLevel, maxLevelAchieved, currNumLives):
		UserFileManagement().addStatistics(username, numKills, numDeaths, levelsCompleted, numRestarts, currentLevel, maxLevelAchieved, currNumLives)

	"""
		This method adds the number of kills to a given username using the filemanagement API.

		@param username is the username who's statistic should be modified.
		@param numKills is the number of kills to be added to the user.
	"""
	def addNumKillsFor(self, username, numKills):
		UserFileManagement().addStatistics(username, numKills, 0, 0, 0, 0, 0, 0)

	"""
		This method adds the number of deaths to a given username using the filemanagement API.

		@param username is the username who's statistic should be modified.
		@param numDeaths is the number of deaths to be added to the user.
	"""
	def addNumDeathsFor(self, username, numDeaths):
		UserFileManagement().addStatistics(username, 0, numDeaths, 0, 0, 0, 0, 0)

	"""
		This method adds the number of levels completed to a given username 
		using the filemanagement API. Usually used to add 1 every level.

		@param username is the username who's statistic should be modified.
		@param levelsCompleted is number of levels completed to be added to the user.
	"""
	def addLevelsCompletedFor(self, username, levelsCompleted):
		UserFileManagement().addStatistics(username, 0, 0, levelsCompleted, 0, 0, 0, 0)

	"""
		This method adds the number of restarts to a given username 
		using the filemanagement API. Usually used to add 1 every restart.

		@param username is the username who's statistic should be modified.
		@param numRestarts is the number of restarts to be added to the user.
	"""
	def addNumRestartsFor(self, username, numRestarts):
		UserFileManagement().addStatistics(username, 0, 0, 0, numRestarts, 0, 0, 0)

	"""
		This method updates the current level to a given username 
		using the filemanagement API. Usually used to add 1 every restart.

		@param username is the username who's statistic should be modified.
		@param currentLevel is the current level to be updated to the user.
	"""
	def updateCurrentLevelFor(self, username, currentLevel):
		user = self.getStatsOf(username)
		UserFileManagement().updateStatistics(username, user[1], user[2], user[3], user[4], currentLevel, user[6], user[7])

	"""
		This method updates the maximum level achieved to a given username 
		using the filemanagement API.

		@param username is the username who's statistic should be modified.
		@param maxLevelAchieved is the current level to be updated to the user.
	"""
	def updateMaxLevelAchievedFor(self, username, maxLevelAchieved):
		user = self.getStatsOf(username)
		UserFileManagement().updateStatistics(username, user[1], user[2], user[3], user[4], user[5], maxLevelAchieved, user[7])

	"""
		This method updates the current number of lives of a given username 
		using the filemanagement API.

		@param username is the username who's statistic should be modified.
		@param currNumLives is the current number of lives to be updated to the user.
	"""
	def updateCurrNumLivesFor(self, username, currNumLives):
		user = self.getStatsOf(username)
		UserFileManagement().updateStatistics(username, user[1], user[2], user[3], user[4], user[5], user[6], currNumLives)
	
	"""
		Gets all user statistics sorted by username.

		@param inverse is an option to reverse the list.
		@return the list of all user statistics ordered by username.
	"""
	def getStatsByUsername(self, inverse):
		stats = UserFileManagement().getStatistics()		
		sortedStats = sorted(stats, key=lambda x:x[0].lower())
		if(inverse == True):
			return sortedStats[::-1]
		return sortedStats

	"""
		Gets all user statistics sorted by number of kills.

		@param inverse is an option to reverse the list.
		@return the list of all user statistics ordered by number of kills.
	"""
	def getStatsByNumKills(self, inverse):
		stats = UserFileManagement().getStatistics()		
		sortedStats = sorted(stats, key=lambda x:int(x[1]))
		if(inverse == False):
			return sortedStats[::-1]
		return sortedStats

	"""
		Gets all user statistics sorted by number of deaths.

		@param inverse is an option to reverse the list.
		@return the list of all user statistics ordered by number of deaths.
	"""
	def getStatsByNumDeaths(self, inverse):
		stats = UserFileManagement().getStatistics()		
		sortedStats = sorted(stats, key=lambda x:int(x[2]))
		if(inverse == False):
			return sortedStats[::-1]
		return sortedStats

	"""
		Gets all user statistics sorted by KDR(Kill/Death ratio).
		Doesn't return the KDR, calculates it while filtering.
		If no deaths, they go first of KDR(becauseit would be infinity) 
		unless the user has zero kills, in that case it goes last

		@param inverse is an option to reverse the list.
		@return the list of all user statistics ordered by KDR.
	"""
	def getStatsByKDR(self, inverse):
		def _sorting(x):
			if(int(x[2]) != 0):
				return round(float(x[1])/float(x[2]), 2)  
			elif(x[1] == 0):
				return round(float(x[2]), 2)
			else:
				# x 1,000,000 to ensure zero deaths come on top
				return float(x[1])*1000000.0
		stats = UserFileManagement().getStatistics()		
		sortedStats = sorted(stats, key=lambda x: _sorting(x))
		if(inverse == False):
			return sortedStats[::-1]
		return sortedStats

	"""
		Gets all user statistics sorted by number of levels completed.

		@param inverse is an option to reverse the list.
		@return the list of all user statistics ordered by levels completed.
	"""
	def getStatsByLevelsCompleted(self, inverse):
		stats = UserFileManagement().getStatistics()		
		sortedStats = sorted(stats, key=lambda x:int(x[3]))
		if(inverse == False):
			return sortedStats[::-1]
		return sortedStats

	"""
		Gets all user statistics sorted by number of restarts.

		@param inverse is an option to reverse the list.
		@return the list of all user statistics ordered by number of restarts.
	"""
	def getStatsByNumRestarts(self, inverse):
		stats = UserFileManagement().getStatistics()		
		sortedStats = sorted(stats, key=lambda x:int(x[4]))
		if(inverse == False):
			return sortedStats[::-1]
		return sortedStats

	"""
		Gets all user statistics sorted by max level achieved.

		@param inverse is an option to reverse the list.
		@return the list of all user statistics ordered by max level achieved.
	"""
	def getStatsByMaxLevelAchieved(self, inverse):
		stats = UserFileManagement().getStatistics()		
		sortedStats = sorted(stats, key=lambda x:int(x[6]))
		if(inverse == False):
			return sortedStats[::-1]
		return sortedStats

	"""
		Gets all user statistics sorted by number of current lives.

		@param inverse is an option to reverse the list.
		@return the list of all user statistics ordered by number of current lives.
	"""
	def getStatsByCurrNumLives(self, inverse):
		stats = UserFileManagement().getStatistics()		
		sortedStats = sorted(stats, key=lambda x:int(x[7]))
		if(inverse == False):
			return sortedStats[::-1]
		return sortedStats

	""" Single user statistics """

	"""
		Gets all statistics of a given username.

		@param username is the username to look for.
		@return user if found, otherwise return None.
	"""
	def getStatsOf(self, username):
		if(username != ""):
			stats = UserFileManagement().getStatistics()
			user = filter(lambda x: x[0] == username, stats)
			return user[0]
		return None

	"""
		Gets number of kills of a specified username.

		@param username is the username we are looking for.
		@return the user's number of kills, otherwise return None.
	"""
	def getNumKillsOf(self, username):
		if(username != ""):
			stats = UserFileManagement().getStatistics()
			user = filter(lambda x: x[0] == username, stats)[0]
			return int(user[1])
		return None

	"""
		Gets number of deaths of a specified username.

		@param username is the username we are looking for.
		@return the user's number of deaths, otherwise return None.
	"""
	def getNumDeathsOf(self, username):
		if(username != ""):
			stats = UserFileManagement().getStatistics()
			user = filter(lambda x: x[0] == username, stats)[0]
			return int(user[2])
		return None

	"""
		Gets KDR of a specified username. 
		KDR is numKills/numDeaths.
		if numDeaths is zero then we return numKills * 1000000

		@param username is the username we are looking for.
		@return the user's KDR, otherwise return None.
	"""
	def getKDROf(self, username):
		if(username != ""):
			stats = UserFileManagement().getStatistics()
			user = filter(lambda x: x[0] == username, stats)[0]
			if(int(user[2]) == 0):
				if(int(user[1]) == 0):
					return 0.0
				return float(1000000*user[1])
			return round(float(user[1])/float(user[2]),2)
		return None

	"""
		Gets number of levels completed of a specified username.

		@param username is the username we are looking for.
		@return the user's number of levels completed, otherwise return None.
	"""
	def getLevelsCompletedOf(self, username):
		if(username != ""):
			stats = UserFileManagement().getStatistics()
			user = filter(lambda x: x[0] == username, stats)[0]
			return int(user[3])
		return None
	
	"""
		Gets number of restarts of a specified username.

		@param username is the username we are looking for.
		@return the user's number of restarts, otherwise return None.
	"""
	def getNumRestartsOf(self, username):
		if(username != ""):
			stats = UserFileManagement().getStatistics()
			user = filter(lambda x: x[0] == username, stats)[0]
			return int(user[4])
		return None

	"""
		Gets current level of a specified username.

		@param username is the username we are looking for.
		@return the user's current level, otherwise return None.
	"""
	def getCurrentLevelOf(self, username):
		if(username != ""):
			stats = UserFileManagement().getStatistics()
			user = filter(lambda x: x[0] == username, stats)[0]
			return int(user[5])
		return None

	"""
		Gets max level achieved of a specified username.

		@param username is the username we are looking for.
		@return the user's max level achieved, otherwise return None.
	"""
	def getMaxLevelAchievedOf(self, username):
		if(username != ""):
			stats = UserFileManagement().getStatistics()
			user = filter(lambda x: x[0] == username, stats)[0]
			return int(user[6])
		return None

	"""
		Gets current number of lives of a specified username.

		@param username is the username we are looking for.
		@return the user's current number of lives, otherwise return None.
	"""
	def getCurrNumLives(self, username):
		if(username != ""):
			stats = UserFileManagement().getStatistics()
			user = filter(lambda x: x[0] == username, stats)[0]
			return int(user[7])
		return None

	"""
		Get users with specific conditions.
		Condition HAS to be from operator module as shown below.
		from operator import lt, le, gt, ge, eq, ne 
	"""
	
	"""
		Helper method to check if the input condition is supported.

		@param condition is the condition to test.
		@return True iff the condition is valid (from operator module).
	"""
	def _checkValidCondition(self, condition):
		return {
	        le: True,
	        lt: True,
	        gt: True,
	        ge: True,
	        ne: True,
	        eq: True,
	        }.get(condition, False)
	
	"""
		Gets all users whose number of kills satisfy the condition 
		with regards to the value.

		@param condition is the condition.
		@param value is the value to be applied to the condition.
		@return the list that fits the given condition.
	"""
	def getUsersWithKills(self, condition, value):
		if(self._checkValidCondition(condition)):
			users = UserFileManagement().getStatistics()
			return filter(lambda x: condition(int(x[1]), value), users)

	"""
		Gets all users whose number of deaths satisfy the condition 
		with regards to the value.

		@param condition is the condition.
		@param value is the value to be applied to the condition.
		@return the list that fits the given condition.
	"""
	def getUsersWithDeaths(self, condition, value):	
		if(self._checkValidCondition(condition)):
			users = UserFileManagement().getStatistics()
			return filter(lambda x: condition(int(x[2]), value), users)

	"""
		Gets all users whose KDR satisfy the condition 
		with regards to the value.

		@param condition is the condition.
		@param value is the value to be applied to the condition.
		@return the list that fits the given condition.
	"""
	def getUsersWithKDR(self, condition, value):
		def _sorting(x):
			if(int(x[2]) != 0):
				return round(float(x[1])/float(x[2]), 2)  
			elif(x[1] == 0):
				return float(x[2])
			else:
				# x 1,000,000 to ensure zero deaths come on top
				return float(x[1])*1000000.0

		if(self._checkValidCondition(condition)):
			users = UserFileManagement().getStatistics()		
			return filter(lambda x: condition(_sorting(x), value), users)

	"""
		Gets all users whose levels completed satisfy the condition 
		with regards to the value.

		@param condition is the condition.
		@param value is the value to be applied to the condition
		@return the list that fits the given condition
	"""
	def getUsersWithLevelsCompleted(self, condition, value):	
		if(self._checkValidCondition(condition)):
			users = UserFileManagement().getStatistics()
			return filter(lambda x: condition(int(x[3]), value), users)

	"""
		Gets all users whose number of restarts satisfy the condition 
		with regards to the value.

		@param condition is the condition.
		@param value is the value to be applied to the condition.
		@return the list that fits the given condition.
	"""
	def getUsersWithNumRestarts(self, condition, value):	
		if(self._checkValidCondition(condition)):
			users = UserFileManagement().getStatistics()
			return filter(lambda x: condition(int(x[4]), value), users)

	"""
		Gets all users whose max level achieved satisfy the condition 
		with regards to the value.

		@param condition is the condition.
		@param value is the value to be applied to the condition.
		@return the list that fits the given condition.
	"""
	def getUsersWithMaxLevelAchieved(self, condition, value):	
		if(self._checkValidCondition(condition)):
			users = UserFileManagement().getStatistics()
			return filter(lambda x: condition(int(x[6]), value), users)

	"""
		Gets all users whose current number of lives satisfy the condition 
		with regards to the value.

		@param condition is the condition.
		@param value is the value to be applied to the condition.
		@return the list that fits the given condition.
	"""
	def getUsersWithCurrNumLives(self, condition, value):	
		if(self._checkValidCondition(condition)):
			users = UserFileManagement().getStatistics()
			return filter(lambda x: condition(int(x[7]), value), users)

"""
	This class is used to get all the maps or a specific map number
"""
