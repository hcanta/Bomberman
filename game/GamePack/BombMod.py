import random,sys,os,imghdr,pygame

from pygame import*
sys.path.append("..")

class Bomb ():
	def __init__(self, tileID, ownerID,tick,_range):

		self._tileID = tileID
		self._owner = ownerID
		self._tick = tick
		self._range = _range
		self._explodeTick = 45
		self._played = False


	def _getSound(self):
		return self._played	
		
	def _setPlayed(self):
			self._played = True

	""" Bomb timer tick"""
	def _explodePulse(self):
		self._explodeTick-=1

	def _pulse(self):
		self._tick-=1

	def _getTileID(self):
		return self._tileID

	def  _getOwner(self):
		return self._owner

	def _getRange(self):
		return self._range 

	"""
	returns a boolean Is the bomb ready to explode
	"""
	def _explosion(self):
		return self._tick<=0

	"""
	Used to determined if the explosion is done and the bomb can be removed from the map
	"""
	def _doneExplosion(self):
		return self._explodeTick<0

	def _getBombID(self):
		return self._bombID

	def _getTick(self):
		return self._explodeTick
		


