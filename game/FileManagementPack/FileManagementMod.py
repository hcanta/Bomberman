import sys, os

sys.path.append("..")
from ConfigPack.ConfigMod import FMConfigs

""" UserFileManagement class handles all file manipulation. """

class UserFileManagement:

	""" 
		Gets all users from the credential.txt file.

		@return all users.
	"""
	def getUsers(self):
		return self.readFileAsListOfLists(FMConfigs.CREDENTIALS)

	""" 
		Gets all the statistics of all users from the statistics.txt file.

		@return all statistics.
	"""
	def getStatistics(self):
		return self.readFileAsListOfLists(FMConfigs.STATISTICS)

	""" 
		Gets all the maps maps.txt file.

		@return all statistics.
	"""
	def getMaps(self):
		return self.readFileAsListOfLists(FMConfigs.MAPS)

	""" 
		Reads any file given its name as a list of lists(lines) [[]]

		@param fileName is the name of the file to be read.
		@return the file in the format of a list of lists or None if fileName is empty.
	"""
	def readFileAsListOfLists(self, fileName):
		if(fileName != ""):
			with open(fileName) as inputFile:
				listofTuples = [list(line.rstrip('\n').rstrip('\r').split(',')) for line in inputFile.readlines()]
			return listofTuples
		else:
			return None

	"""
		Adds a user to the credential.txt file as well as initiates 
		a line in the statistics.txt so it can be modified later on.

		@param username is the username to be added.
		@param password is the password to be encrypted and added.
	"""
	def addUser(self, username, password):
		if(username != "" and password != ""):
			with open(FMConfigs.CREDENTIALS, "a") as inputFile:
				inputFile.write(username + "," + "".join([chr(ord(c) + FMConfigs.CAESARCONSTANT) for c in password]) + "\n")
			# Create stats entry
			with open(FMConfigs.STATISTICS, "a") as inputFile:
				# TODO initialize with proper values
				inputFile.write(username + ",0,0,0,0,0,1,3\n")

	"""
		Removes a user from credentials.txt as well as from statistics.txt.

		@param username is the user's username to be deleted.
	"""
	def removeUser(self, username):
		if(username != ""):
			content = self.getUsers()
			newFile = filter(lambda x: x[0] != username, content)
			with open(FMConfigs.CREDENTIALS, "w") as f:
				[f.write(",".join(x) + "\n") for x in newFile]
			self._removeStatisticsOf(username)

	"""
		Helper method of removeUser that removes the statistics part of the user.

		@param username is the user's username to be deleted.
	"""
	def _removeStatisticsOf(self, username):
		content = self.getStatistics()
		newFile = filter(lambda x: x[0] != username, content)
		with open(FMConfigs.STATISTICS, "w") as f:
			[f.write(",".join(x) + "\n") for x in newFile]

	"""
		Adds all new statistics to the given username. It does not take an absolute value,
		this method should be called at the end of a level with the level's statistics and
		it will be properly added here. DO NOT give the user's total statistics, simply
		current level score to be added.

		@param username is the username who's statistics should be modified.
		@param numKills is the number of kills to be added to the user.
		@param numDeaths is the number of deaths to be added to the user.
		@param levelsCompleted is the number of levels the user has completed in total.
		@param numRestarts is the number of time a user has restarted all the levels.
		@param currentLevel is the current level the user is at without losing all its lives.
		@param maxLevelAchieved is the max level the user has ever achieved.
		@param currNumLives is the number of lives th user has left in order to beat all levels.
	"""
	def addStatistics(self, username, numKills, numDeaths, levelsCompleted, numRestarts, currentLevel, maxLevelAchieved, currNumLives):
		if(username != ""):
			stats = self.getStatistics()
			user = filter(lambda x: x[0] == username, stats)
			restOfFile = filter(lambda x: x[0] != username, stats)
			if user:
				userlist = user[0]
				userlist[1] = str(int(userlist[1]) + numKills)
				userlist[2] = str(int(userlist[2]) + numDeaths)
				userlist[3] = str(int(userlist[3]) + levelsCompleted)
				userlist[4] = str(int(userlist[4]) + numRestarts)
				userlist[5] = str(int(userlist[5]) + currentLevel)
				userlist[6] = str(int(userlist[6]) + maxLevelAchieved)
				userlist[7] = str(int(userlist[7]) + currNumLives)
				with open(FMConfigs.STATISTICS, "w") as f:
					if restOfFile:
						[f.write(",".join(x) + "\n") for x in restOfFile]
					[f.write(",".join(x) + "\n") for x in [userlist]]
	"""
		Updates(READ OVERWRITES) all new statistics to the given username. It does not take an absolute value,
		this method should be called at the end of a level with the level's statistics and
		it will be properly added here. DO NOT give the user's total statistics, simply
		current level score to be added.

		@param username is the username who's statistics should be modified.
		@param numKills is the number of kills to be added to the user.
		@param numDeaths is the number of deaths to be added to the user.
		@param levelsCompleted is the number of levels the user has completed in total.
		@param numRestarts is the number of time a user has restarted all the levels.
		@param currentLevel is the current level the user is at without losing all its lives.
		@param maxLevelAchieved is the max level the user has ever achieved.
		@param currNumLives is the number of lives th user has left in order to beat all levels.
	"""
	def updateStatistics(self, username, numKills, numDeaths, levelsCompleted, numRestarts, currentLevel, maxLevelAchieved, currNumLives):
		if(username != ""):
			stats = self.getStatistics()
			user = filter(lambda x: x[0] == username, stats)
			restOfFile = filter(lambda x: x[0] != username, stats)
			if user:
				userlist = user[0]
				userlist[1] = str(numKills)
				userlist[2] = str(numDeaths)
				userlist[3] = str(levelsCompleted)
				userlist[4] = str(numRestarts)
				userlist[5] = str(currentLevel)
				userlist[6] = str(maxLevelAchieved)
				userlist[7] = str(currNumLives)
				with open(FMConfigs.STATISTICS, "w") as f:
					if restOfFile:
						[f.write(",".join(x) + "\n") for x in restOfFile]
					[f.write(",".join(x) + "\n") for x in [userlist]]

	# TODO NOT DONE, GOTTA VERIFY ELEMENT TYPES
	"""
		Adds a new map to the map pool.

		@param newMap is the new map to be added
	"""
	def addMap(self, newMap):
		if(newMap):
			with open(FMConfigs.MAPS, "a") as f:
				newNewMap = [str(x) for x in newMap]
				[f.write(",".join(x) + "\n") for x in [newNewMap]]
