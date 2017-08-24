import random,sys,os,imghdr,pygame
from ConfigPack.ConfigMod import AppConfigs, GameConfigs, OtherConfigs
from pygame import*
sys.path.append("..")

class Monster():
	
	"""
	Constructor for the Monster object
	"""
	def __init__(self, typeId, tileID):
		self._lives = 1
		self._x = tileID % GameConfigs.BOARD_SIZE
		self._y =  tileID / GameConfigs.BOARD_SIZE
		self._movePulse = 12
		self._tileID = tileID
		self._typeID = typeId

	""" 
	returns the type of the monster, the type identify what color or shape the monster is.
	"""
	def _getTypeID(self):
		return self._typeID
	"""
		Indicates if the Monster is allowed to move
	"""
	def _canMove(self):
		return self._movePulse == 12
	def _Moving(self):
		array = ["left","right","up","down"]
		return array[int(random.randrange(0,4))]

	def _getTileID(self):
		return self._tileID

	def _setTileID(self,tile):
		self._tileID = tile
	def _getX(self):
		return self._x

	def _getY(self):
		return self._y

	def _setX(self,x):
		self._x = x

	def _setY(self,y):
		self._y = y
	def _isDead(self):
		return self._lives<1

	def _decreaseLives(self):
		self._lives-=1

	def _resetMovePulse(self):
		self._movePulse = 0

	def _increaseMovePulse(self):
		if self._movePulse< 12:
			self._movePulse +=1
