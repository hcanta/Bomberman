#Imports
import pygame
from pygame.locals import*
import os, sys, math
sys.path.append("..")
from ConfigPack.ConfigMod import AppConfigs, SubstateConfigs, OtherConfigs
from GamePack.GameMod import Game
from GamePack.SoundMod import Sound
from LobbyPack.LobbyMod import Lobby

"""
	Main Window App
	The application is created along with a pygame window and screen
"""
class App():

	"""
		App Constructor: initialization of pygame objects, window components and splash screen
	"""
	def __init__(self):

		os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (100, 100)

		#Initialize pygame
		pygame.init()

		#Window Configs
		self._screen = pygame.display.set_mode(AppConfigs.WINDOWSIZE, pygame.NOFRAME)
		pygame.display.set_caption(AppConfigs.WINDOWNAME)

		self._background_file = "sprites/bg.jpg"
		self._background = pygame.image.load(self._background_file)
		self._logo_file = "sprites/logo.png"
		self._logo_image = pygame.image.load(self._logo_file)
		self._loadfont = pygame.font.Font(OtherConfigs.FONT_PATH,OtherConfigs.FONT_SIZE)
		self._loadtext = self._loadfont.render("LOADING...", True, OtherConfigs.COLOR_GRAY)
		self._screen.blit(self._background, (0, 0))
		self._screen.blit(self._logo_image, (300,214))
		self._screen.blit(self._loadtext, (310, 400))
		pygame.display.update()

		#FPS Clock
		self._FPSClock = pygame.time.Clock()

		#Sound
		self._sound = Sound()

		#Initialize states
		self._lobby = Lobby(self._screen, self._FPSClock, self._sound)


	"""
		State Loop that allows branching from one State to another
	"""
	def run(self):

		#Initial state
		self._state = AppConfigs.STATE_LOBBY

		#State Loop
		while 1:

			#Lobby State
			if self._state == AppConfigs.STATE_LOBBY:
				self._state = self._lobby.run()

			#Game State
			if self._state == SubstateConfigs.SUBSTATE_INGAME:
				self._state = Game(self._screen, self._FPSClock, self._sound, SubstateConfigs.SUBSTATE_INGAME).run()

			if self._state == SubstateConfigs.SUBSTATE_INMULT:
				self._state = Game(self._screen, self._FPSClock, self._sound, SubstateConfigs.SUBSTATE_INMULT).run()

			if self._state == SubstateConfigs.SUBSTATE_INMULTALT:
				self._state = Game(self._screen, self._FPSClock, self._sound, SubstateConfigs.SUBSTATE_INMULTALT).run()