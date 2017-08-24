#Imports
import pygame, sys, math
from pygame.locals import*
sys.path.append("..")
from ConfigPack.ConfigMod import AppConfigs, SubstateConfigs
from AuthMenuMod import AuthMenu
from MainMenuMod import MainMenu
from OptionsMenuMod import OptionsMenu
from StatsMenuMod import StatsMenu

"""Lobby State"""
class Lobby():

	"""
		Lobby State Class Constructor used to inject objects into Substates
	"""
	def __init__(self, screen, fpsclock, sound):

		#Initialize Auth Menu
		self._authmenu = AuthMenu(screen, fpsclock, sound)
		self._mainmenu = MainMenu(screen, fpsclock, sound)
		self._optionsmenu = OptionsMenu(screen, fpsclock, sound)
		self._statsmenu = StatsMenu(screen, fpsclock, sound)
		self._sound = sound
		self._screen = screen
		#FPS Clock
		self._FPS = AppConfigs.FPS
		self._fpsclock = fpsclock

	"""
		Game Loop for the Lobby State. Will listen/render selected Substate
	"""
	def run(self):

		#Initial Substate
		self._substate = self._authmenu

		#Control Substates
		self._nextSubstate = SubstateConfigs.SUBSTATE_AUTHMENU
		self._currentSubstate = SubstateConfigs.SUBSTATE_AUTHMENU

		self._gamemode = SubstateConfigs.SUBSTATE_UNDEFINED

		#Substate Loop
		while 1:

			#Check which substates to listen/render
			if self._nextSubstate != self._currentSubstate:
				if self._nextSubstate == SubstateConfigs.SUBSTATE_AUTHMENU:
					self._substate = self._authmenu
				elif self._nextSubstate == SubstateConfigs.SUBSTATE_MAINMENU:
					self._substate = self._mainmenu
				elif self._nextSubstate == SubstateConfigs.SUBSTATE_OPTIONSMENU:
					self._substate = self._optionsmenu
				elif self._nextSubstate == SubstateConfigs.SUBSTATE_STATSMENU:
					self._substate = StatsMenu(self._screen, self._fpsclock, self._sound)
				elif self._nextSubstate == SubstateConfigs.SUBSTATE_INGAME:
					self._gamemode = SubstateConfigs.SUBSTATE_INGAME
					break
				elif self._nextSubstate == SubstateConfigs.SUBSTATE_INMULT:
					self._gamemode = SubstateConfigs.SUBSTATE_INMULT
					break
				elif self._nextSubstate == SubstateConfigs.SUBSTATE_INMULTALT:
					self._gamemode = SubstateConfigs.SUBSTATE_INMULTALT
					break
				self._currentSubstate = self._nextSubstate

			#Listen to Events/Render with a tick
			self._nextSubstate = self._substate.tick()

			#Update
			pygame.display.update()

			#FPS tick
			self._fpsclock.tick(self._FPS)

		#Back to Game State
		return self._gamemode