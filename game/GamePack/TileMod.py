import random,sys,os,imghdr,pygame
from ConfigPack.ConfigMod import AppConfigs, GameConfigs, OtherConfigs
from pygame import*
sys.path.append("..")

class Tile():
	def __init__(self, tileId, content):
		self._id = tileId
		self._content = content
		self._nextContent = GameConfigs.EMPTY
		if self._content != GameConfigs.EMPTY and self._content != "B0"and self._content != "B1"and self._content != "B2" and self._content != "B3":
			self._Walkable = False
		else :
			self._Walkable = True
		

	def _setNextContent(self, nContent):
		self._nextContent = nContent

	def _getNextContent(self):
		return self._nextContent
	def _setWalkable(self, w):
		self._Walkable = w

	def _isWalkable(self):
		return self._Walkable

	def _getContent (self):
		return self._content

	def _setContent(self, c):
		self._content = c

	def _getId(self):
		return self._id
				