#Imports
import pygame, sys, math
from pygame.locals import*
sys.path.append("..")
from ConfigPack.ConfigMod import AppConfigs, SubstateConfigs, OtherConfigs, FMConfigs
from AppPack.SubstateMod import Substate
from FileManagementPack.DatabaseMod import HighscoreDatabase

"""
	This is the highscores substate. It handles how the data is displayed.
	It is only available from the main menu substate.
"""
class StatsMenu(Substate):

	"""
		Calls the parent's constructor that builds up everything needed.
	"""
	def __init__(self, screen, fpsclock, sound):
		super(StatsMenu, self).__init__(screen, fpsclock, sound)

	"""	
		This method initializes the objects used in this substate.
	"""
	def _initObjects(self):
		
		#Initialize
		self.__hs = HighscoreDatabase()
		self.__loadScoreData()
		self.__initRange = 0
		self.__categories = ["Users", "Kills", "Deaths", "KDR", "Levels"]
		self.__sortindex = 1

	"""	
		This method initializes the images used in this substate.
	"""
	def _initImages(self):

		self.clearBackground()

		#Render Background
		self._background_file = "sprites/bg.jpg"
		self._background = pygame.image.load(self._background_file)

	"""
		Ticks every frame. Has to be implemented in order to avoir the NotImplementedError exception,
		nothing special happens here for this particular substate.
	"""
	def _ticked(self):

		#Return this if nothing changed
		self._substate = SubstateConfigs.SUBSTATE_STATSMENU

	"""
		This method listens to user inputs and sets the right variable so that the
		render method displays whatever the user has input.
	"""
	def _listen(self):

		#Event queue loop
		for event in pygame.event.get():

			#Quit event
			if event.type == QUIT:
				pygame.quit()
				sys.exit()

			#Key events
			if event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					
					self._substate = SubstateConfigs.SUBSTATE_MAINMENU
					break

				# Get highscores
				if event.key == K_k:
					self.__sortedByString = "Number of Kills"
					self.__sortedBy = self.__scoresByKills
					self.__initRange = 0
					self.__sortindex = 1
					break
				elif event.key == K_d:
					self.__sortedByString = "Number of Deaths"
					self.__sortedBy = self.__scoresByDeaths
					self.__initRange = 0
					self.__sortindex = 2
					break
				elif event.key == K_r:
					self.__sortedByString = "KDR"
					self.__sortedBy = self.__scoresByKDR
					self.__initRange = 0
					self.__sortindex = 3
					break
				elif event.key == K_l:
					self.__sortedByString = "Levels Completed"
					self.__sortedBy = self.__scoresByLevelsCompleted
					self.__initRange = 0
					self.__sortindex = 4
					break
				elif event.key == K_u:
					self.__sortedByString = "Username"
					self.__sortedBy = self.__scoresByUsername
					self.__initRange = 0
					self.__sortindex = 0
					break
				
				#Navigate through highscores	
				elif event.key == K_UP:
					self.__initRange = 0
					break
				elif event.key == K_DOWN:
					self.__initRange = len(self.__sortedBy) - 10
					if(self.__initRange < 0):
						self.__initRange = 0
					break
				elif event.key == K_LEFT:
					self.__initRange = self.__initRange - 10
					if(self.__initRange < 0):
						self.__initRange = 0
					break
				elif event.key == K_RIGHT:
					self.__initRange = self.__initRange + 10
					if(self.__initRange >= len(self.__sortedBy)):
						self.__initRange = len(self.__sortedBy) - 10
					break
				
	"""
		This method renders the menu according to the user input. It displays sorted data
		in accordance to kills, deaths, levels completed or KDR.
	"""
	def _render(self):

		#Blit to screen
		self._screen.blit(self._background, (0,0))
		self.__printTitle("Highscores",(270,40))
		self.__printText("Sort by:  U => Users, K => Kills, D => Deaths, R => KDR, L => Levels",(10,580))

		self._userfont= pygame.font.Font(OtherConfigs.FONT_PATH,OtherConfigs.USER_FONT_SIZE)

		self._sortlist = [None, None, None, None, None]

		for i in range(5):
			self._sortlist[i] = self._userfont.render(self.__categories[i], True, OtherConfigs.COLOR_GRAY)

		self._sortlist[self.__sortindex] = self._userfont.render(self.__categories[self.__sortindex], True, OtherConfigs.COLOR_RED)

		for i in range(5):
			self._screen.blit(self._sortlist[i], (115+120*i, 120))

		self.__printTextRed("ESC - Back to Main Menu", (10, 550))

		maxRange = 10 + self.__initRange

		# self.__printText("Sorted by " + self.__sortedByString, (40, 100))

		__drawIdx = 1

		for idx, score in enumerate(self.__sortedBy):
			__realIndex = idx + 1
			if(__realIndex > self.__initRange):
				__scoreString = str(__realIndex) + ".       " + score[0]

				spaces1 = ""
				for i in xrange(0, 15-len(score[0])):
					spaces1 += " "

				__scoreString += spaces1 + score[1]

				spaces2 = ""
				for i in xrange(0, 15-len(score[1])):
					spaces2 += " "

				__scoreString += spaces2 + score[2]

				spaces3 = ""
				for i in xrange(0, 15-len(score[2])):
					spaces3 += " "

				kdr = str(self.__hs.getKDROf(score[0]))

				__scoreString += spaces3 + kdr

				spaces4 = ""
				for i in xrange(0, 15-len(kdr)):
					spaces4 += " "

				__scoreString += spaces4 + score[3]

				self.__printText(__scoreString, (50,110+35*__drawIdx))
				__drawIdx = __drawIdx + 1
				if(__realIndex == maxRange):
					break

	"""
		This method loads the data from the database and stores it here in memory
		so we can display it appropriatly.
	"""
	def __loadScoreData(self):		
		self.__scoresByKills = self.__hs.getStatsByNumKills(False)
		self.__scoresByDeaths = self.__hs.getStatsByNumDeaths(False)
		self.__scoresByKDR = self.__hs.getStatsByKDR(False)
		self.__scoresByLevelsCompleted = self.__hs.getStatsByLevelsCompleted(False)
		self.__scoresByUsername = self.__hs.getStatsByUsername(False)
		self.__sortedByString = "Number of Kills"
		self.__sortedBy = self.__scoresByKills # Default

	"""
		This method prints text black using usual font and SELECTED_FONT_SIZE.

		@param text is the text to be displayed.
		@param point is the point where the text should be rendered.
	"""
	def __printTitle(self,text,point):
	#	font = pygame.font.SysFont("resources/fonts/Lucida Console",26)
		font = pygame.font.Font(OtherConfigs.FONT_PATH,OtherConfigs.SELECTED_FONT_SIZE)
	#	font = pygame.font.SysFont(pygame.font.get_default_font(),26)
		#font = pygame.font.Font(None,24)
		label = font.render(str(text)+'  ', True, OtherConfigs.COLOR_BLACK)
		textRect = label.get_rect()
		textRect.x = point[0]
		textRect.y = point[1]
		self._screen.blit(label, textRect)
	"""
		This method prints text black using usual font and USER_FONT_SIZE.

		@param text is the text to be displayed.
		@param point is the point where the text should be rendered.
	"""
	def __printText(self,text,point):
	#	font = pygame.font.SysFont("resources/fonts/Lucida Console",26)
		font = pygame.font.Font(OtherConfigs.FONT_PATH,OtherConfigs.USER_FONT_SIZE)
	#	font = pygame.font.SysFont(pygame.font.get_default_font(),26)
		#font = pygame.font.Font(None,24)
		label = font.render(str(text)+'  ', True, OtherConfigs.COLOR_BLACK)
		textRect = label.get_rect()
		textRect.x = point[0]
		textRect.y = point[1]
		self._screen.blit(label, textRect)

	"""
		This method prints text red using usual font and USER_FONT_SIZE.

		@param text is the text to be displayed.
		@param point is the point where the text should be rendered.
	"""
	def __printTextRed(self,text,point):
	#	font = pygame.font.SysFont("resources/fonts/Lucida Console",26)
		font = pygame.font.Font(OtherConfigs.FONT_PATH,OtherConfigs.USER_FONT_SIZE)
	#	font = pygame.font.SysFont(pygame.font.get_default_font(),26)
		#font = pygame.font.Font(None,24)
		label = font.render(str(text)+'  ', True, OtherConfigs.COLOR_RED)
		textRect = label.get_rect()
		textRect.x = point[0]
		textRect.y = point[1]
		self._screen.blit(label, textRect)

	"""
		This method clears the background.
	"""
	def clearBackground(self):
		bg = pygame.Surface(self._screen.get_size())
		bg = bg.convert()
		bg.fill((0,0,0))
		self._screen.blit(bg,(0,0))