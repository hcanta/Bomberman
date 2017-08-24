#Imports
import pygame, sys, math
from pygame.locals import*
sys.path.append("..")
from ConfigPack.ConfigMod import SubstateConfigs, AppConfigs
from InGameMod import InGame
from InMenuMod import InMenu
from InMultMod import InMult
from GameOverMod import GameOver
from WinMod import Win


"""Game State"""
class Game():

	"""
		Game State Class Constructor used to inject objects into Substates
	"""
	def __init__(self, screen, fpsclock, sound, substate):

		#Initialize substates
		if substate == SubstateConfigs.SUBSTATE_INGAME:
			self._ingame = InGame(screen, fpsclock, sound)
		elif substate == SubstateConfigs.SUBSTATE_INMULT:
			self._ingame = InMult(screen, fpsclock, sound, False)
		elif substate == SubstateConfigs.SUBSTATE_INMULTALT:
			self._ingame = InMult(screen, fpsclock, sound, True)

		self._inmenu = InMenu(screen, fpsclock, sound)
		self._gameover = GameOver(screen, fpsclock, sound)
		self._win = Win(screen, fpsclock, sound)

		#FPS Clock
		self._FPS = AppConfigs.FPS
		self._fpsclock = fpsclock

	"""
		Game Loop for the Game State. Will listen/render selected Substate
	"""
	def run(self):

		#Initial Substate
		self._substate = self._ingame

		self._lobbymode = AppConfigs.STATE_LOBBY

		#Control Substates
		self._nextSubstate = SubstateConfigs.SUBSTATE_INGAME
		self._currentSubstate = SubstateConfigs.SUBSTATE_INGAME

		#Substate Loop
		while 1:

			#Check which substates to listen/render
			if self._nextSubstate != self._currentSubstate:
				if self._nextSubstate == SubstateConfigs.SUBSTATE_INGAME:
					self._substate = self._ingame
				elif self._nextSubstate == SubstateConfigs.SUBSTATE_INMENU:
					self._substate = self._inmenu
				elif self._nextSubstate == SubstateConfigs.SUBSTATE_INMULT:
					self._substate = self._ingame
				elif self._nextSubstate == SubstateConfigs.SUBSTATE_INMULTALT:
					self._substate = self._ingame
				elif self._nextSubstate == SubstateConfigs.SUBSTATE_BACK:
					break
				elif self._nextSubstate == SubstateConfigs.SUBSTATE_GAMEOVER:
					self._substate = self._gameover
				elif self._nextSubstate == SubstateConfigs.SUBSTATE_WIN:
					self._substate = self._win
				elif self._nextSubstate == SubstateConfigs.SUBSTATE_RESTART:
					self._lobbymode = SubstateConfigs.SUBSTATE_INGAME
					break
				self._currentSubstate = self._nextSubstate

			#Listen to Events/Render with a tick
			self._nextSubstate = self._substate.tick()

			#Update
			pygame.display.update()

			#FPS tick
			self._fpsclock.tick(self._FPS)

		#Back to Lobby State
		return self._lobbymode