import sys
sys.path.append("..")
from ConfigPack.ConfigMod import AppConfigs, SubstateConfigs

"""
	Parent class for all Substate objects
"""
class Substate(object):

	"""
		Constructor that handles all injections and initialization of substate parameters
	"""
	def __init__(self, screen, fpsclock, sound):
		
		#Screen
		self._screen = screen

		#FPS Clock
		self._FPS = AppConfigs.FPS
		self._fpsclock = fpsclock

		#Sound
		self._sound = sound

		#Initialize substate to undefined
		self._substate = SubstateConfigs.SUBSTATE_UNDEFINED

		#Initialize objects
		self._initObjects()

		#Initialize images
		self._initImages()

	"""
		Method to allow initialization of substate objects
	"""
	def _initObjects(self):
		raise NotImplementedError

	"""
		Method to allow initialization of substate images
	"""
	def _initImages(self):
		raise NotImplementedError

	"""
		Method called by State loop when current substate is selected (This method is called each frame)
	"""
	def tick(self):
		self._ticked()
		self._listen()
		self._render()
		return self._substate

	"""
		Method to allow handling of frame-dependent functions for a substate (This method is called each frame)
	"""
	def _ticked(self):
		raise NotImplementedError

	"""
		Method to allow listeners for a substate (This method is called each frame)
	"""
	def _listen(self):
		raise NotImplementedError

	"""
		Method to allow rendering for a substate (This method is called each frame)
	"""
	def _render(self):
		raise NotImplementedError