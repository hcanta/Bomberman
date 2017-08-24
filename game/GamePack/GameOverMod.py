#Imports
import pygame, sys, math
from pygame.locals import*
sys.path.append("..")
from ConfigPack.ConfigMod import AppConfigs, OtherConfigs, SubstateConfigs
from LobbyPack.MainMenuMod import MainMenu
from GamePack.SoundMod import Sound
from AppPack.SubstateMod import Substate

"""Game Over Substate"""
class GameOver(Substate):

	"""
		Authentication menu elements are built with this object.
	"""

	class MenuElement:
		text = ''
		surface = pygame.Surface
		element_rect = pygame.Rect
		selected_rect = pygame.Rect

	"""
		Calls the parent's constructor that builds up everything needed.
	"""

	def __init__(self, screen, fpsclock, sound):
		super(GameOver, self).__init__(screen, fpsclock, sound)


	"""
		Initialize Menu elements 
	"""	

	def _initObjects(self):

		#Create Menu List and Structure
		self._list = ['GAME OVER']
		self._list_length = len(self._list)
		self.position_selected = 0
		self.create_structure()

	"""
		Initializes all the images and fonts needed Game Over
	"""

	def _initImages(self):

		#Render Background
		self._background_file = "sprites/bg.jpg"
		self._background = pygame.image.load(self._background_file)

		#Render Logo
		self._logo_file = "sprites/logo.png"
		self._logo_image = pygame.image.load(self._logo_file)

		self._font = pygame.font.Font(OtherConfigs.FONT_PATH, OtherConfigs.SELECTED_FONT_SIZE)


	"""
		Is called every frame and is used to keep track of counters for error messages.
		Updates the menu if needed.
	"""

	def _ticked(self):

		#Return this if nothing changed
		self._substate = SubstateConfigs.SUBSTATE_GAMEOVER

	"""
		Main Event loop
		Switch to main menu
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
				if event.key == K_RETURN:
						self._substate = SubstateConfigs.SUBSTATE_BACK
						break

	"""
		Renders the Menu elements, background
	"""


	def _render(self):

		#Blit to screen
		self._screen.blit(self._background, (0, 0))
		self._screen.blit(self._logo_image, (100,214))

		#Blit Menu
		for i in xrange(self._list_length):
			if i != self.position_selected:
				self._screen.blit(self._menulist[i].surface,(self.menu_coordinates[0]+self._menulist[i].element_rect.x, self.menu_coordinates[1]+self._menulist[i].element_rect.y))
			else:
				self._screen.blit(self._menulist[i].surface,(self.menu_coordinates[0]+self._menulist[i].element_rect.x, self.menu_coordinates[1]+self._menulist[i].element_rect.y-6))

	"""
		This creates the menu, positions it and it initializes the whole menu logic.
	"""


	def create_structure(self):
		menu_width = 0
		menu_height = 0
		self._menulist=[]
		self.font = pygame.font.Font(OtherConfigs.FONT_PATH, OtherConfigs.FONT_SIZE)

		for i in xrange(self._list_length):
			self._menulist.append(self.MenuElement())
			self._menulist[i].text = self._list[i]
			self._menulist[i].surface = self.font.render(self._menulist[i].text, 1, OtherConfigs.COLOR_GRAY)
			self._menulist[i].element_rect = self._menulist[i].surface.get_rect()

			distance = OtherConfigs.FONT_SIZE * 0.15

			height = self._menulist[i].element_rect.height
			self._menulist[i].element_rect.left = distance
			self._menulist[i].element_rect.top = distance+(distance*2+30)*i

			width = self._menulist[i].element_rect.width+distance*2
			height = self._menulist[i].element_rect.height+distance*2            
			left = self._menulist[i].element_rect.left-distance
			top = self._menulist[i].element_rect.top-distance
            
			if width > menu_width:
				menu_width = width
			menu_height += height

		self.font = pygame.font.Font(OtherConfigs.FONT_PATH, OtherConfigs.SELECTED_FONT_SIZE)
		self._menulist[self.position_selected].surface = self.font.render(self._menulist[self.position_selected].text, 1, OtherConfigs.COLOR_RED)

		#center the text list on the screen
		x = self._screen.get_rect().centerx - menu_width / 2 
		y = self._screen.get_rect().centery - menu_height / 2

		self.menu_coordinates = (x,y)