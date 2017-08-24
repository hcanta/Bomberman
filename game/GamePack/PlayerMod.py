import random,sys,os,imghdr,pygame
from ConfigPack.ConfigMod import AppConfigs, GameConfigs, OtherConfigs
from FileManagementPack.DatabaseMod import HighscoreDatabase
from pygame import*
sys.path.append("..")

class Player ():
	
	"""
	Constructor for the player opject, takes the player name and ID as well as it s starting tile ID on the BOARD
	"""
	def __init__(self, playerId, name, tileID):
		self._Id = playerId
		self._name = name
		self._highScoreDB = HighscoreDatabase()
		self._livesMax = 5
		self._lives = 3
		self._nbDeath = 0
		self._bombRange = 1
		self._nbKills = 0
		self._x = tileID % GameConfigs.BOARD_SIZE
		self._y =  tileID / GameConfigs.BOARD_SIZE
		self._nbBombPlaced = 0
		self._nbBombMax = 1
		self._tileID =  tileID
		self._state ="U1"
		self._invulnerablePulse = 45

	def _setLives(self, l):
		self._lives = l

	def _reset(self):
		self._bombRange = 1
		self._nbBombMax = 1
		
	""" 
		Can the player be affected my monster or explosion blast
	"""
	def _isVulnerable(self):
		return self._invulnerablePulse == 45

	def _getInvulnerablePulse(self):
		return self._invulnerablePulse

	def _pulseInvulnerable(self):
		if self._invulnerablePulse < 45:
			self._invulnerablePulse+=1

	def _resetInvulnerablePulse(self):
		self._invulnerablePulse = 0

	def _setTileID(self, tID):
		self._tileID = tID
		self._x = tID % GameConfigs.BOARD_SIZE
		self._y =  tID / GameConfigs.BOARD_SIZE

	def _getTileID(self):
		return self._tileID

	def _getLives(self):
		return self._lives

	def _getState(self):
		return self._state

	def _goLeft(self):
		if self._state != "L1" and self._state != "L2":
			self._state = "L1"
		else:
			self._getNextState()

	def _goRight(self):
		if self._state != "R1" and self._state != "R2":
			self._state = "R1"
		else:
			self._getNextState()

	def _goUp(self):
		if self._state != "U1" and self._state != "U2":
			self._state = "U1"
		else:
			self._getNextState()

	def _goDown(self):
		if self._state != "D1" and self._state != "D2":
			self._state = "D1"
		else:
			self._getNextState()

	""" 
	This method is used to determined which image should be used for the current state given the previous state of the player
	"""
	def _getNextState(self):
		if self._state[1]=="1":
			self._state = self._state[0]+"2"
		else:
			self._state = self._state[0]+"1"

	def _getID(self):
		return self._Id

	def _getNbBombMax(self):
		return self._nbBombMax

	def _getNbBombPlaced(self):
		return self._nbBombPlaced

	def _canPlaceBomb(self):
		return self._nbBombPlaced < self._nbBombMax

	def _increaseBombPlaced(self):
		self._nbBombPlaced+=1

	def _increaseBombMax(self):
		if self._nbBombMax <= 9:
			self._nbBombMax+=1

	def _decreaseBombMax (self):	
		if  self._nbBombMax >1:
			self._nbBombMax-=1

	# Call to can place bomb must be called before calling this function 
	def _increaseBombPlaced(self):
		self._nbBombPlaced+= 1

	def _decreaseBombPlaced(self):
		self._nbBombPlaced-= 1	

	def _getX(self):
		return self._x

	def _getY(self):
		return self._y

	def _setX(self,x):
		self._x = x

	def _setY(self,y):
		self._y = y

	def _getNbDeath(self):
		return self._nbDeath

	def _addToKills(self):
		self._nbKills +=1

	def _getNbKills(self):
		return self._nbKills

	def _increaseRange(self):
		if self._bombRange +1 <= 12:
			self._bombRange+=1

	def _decreaseRange(self):
		if(self._bombRange -1 >= 1) :
			self._bombRange -=1

	def _getBombRange(self):
		return self._bombRange	
	
	def _getName(self):
		return self._name


	def _increaseLivesMax(self):
		if self._livesMax < 6 :
			self._livesMax += 1


	def _increaseLives(self):
		if (self._lives +1)<= self._livesMax:
			self._lives+=1
			self._highScoreDB.updateCurrNumLivesFor	(self._name,self._lives)

	def _isDeadGameOver(self):
		 return self._lives < 1
		

	def _decreaseLives(self):
		if self._lives -1 >= 0:
			self._lives-=1
			self._nbDeath+=1
			self._highScoreDB.addNumDeathsFor(self._name,1)	
			self._highScoreDB.updateCurrNumLivesFor	(self._name,self._lives)

	def _decreaseLivesMax(self):
		if (self._livesMax -1 >= 2) :
			self._livesMax -= 1
			if self._lives -1>= 2:
				self._lives-=1





