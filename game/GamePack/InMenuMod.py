#Imports
import pygame, sys, math
from pygame.locals import*
sys.path.append("..")
from ConfigPack.ConfigMod import AppConfigs, OtherConfigs, SubstateConfigs
from LobbyPack.MainMenuMod import MainMenu
from GamePack.SoundMod import Sound
from AppPack.SubstateMod import Substate

"""Game InMenu Substate"""
class InMenu(Substate):

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
		super(InMenu, self).__init__(screen, fpsclock, sound)

	"""
		Initialize Menu elements
	"""

	def _initObjects(self):

		#Create Menu List and Structure
		self._list = ['Resume','Restart','Music', 'Quit']
		self._list_length = len(self._list)
		self.position_selected = 0
		self.create_structure()

	"""
		Initializes all the images and fonts needed for the menu.
	"""
	def _initImages(self):

		#Render Background
		self._background_file = "sprites/bg.jpg"
		self._background = pygame.image.load(self._background_file)

		#Render Logo
		self._logo_file = "sprites/logo.png"
		self._logo_image = pygame.image.load(self._logo_file)

		self._font = pygame.font.Font(OtherConfigs.FONT_PATH, OtherConfigs.SELECTED_FONT_SIZE)

		if self._sound.musicPlaying:
			self._music =self._font.render("ON", True, OtherConfigs.COLOR_RED)
		else:
			self._music =self._font.render("OFF", True, OtherConfigs.COLOR_GRAY)

	"""
		Is called every frame and is used to keep track of counters for error messages.
		Updates the menu if needed.
	"""

	def _ticked(self):

		#Return this if nothing changed
		self._substate = SubstateConfigs.SUBSTATE_INMENU


	"""
		Main Event loop
		Can switch between different substates
		and turn off Sound
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
				if event.key  == K_UP:
					self.move(-1) 
					#self._inmenu.draw(-1)
				if event.key == K_DOWN:
					self.move(1)
					#self._inmenu.draw(1)
				if event.key == K_RETURN:
					if self.position_selected==0:
						
						self._substate = SubstateConfigs.SUBSTATE_INGAME
						break
					if self.position_selected==1:
						
						self._substate = SubstateConfigs.SUBSTATE_RESTART
						break
					if self.position_selected==2:
						if self._sound.musicPlaying:
							
							self._sound.playmusic("Stop")
							self._music = self._font.render("OFF", True, OtherConfigs.COLOR_GRAY)

						else:
							
							self._sound.playmusic("Play")
							self._music = self._font.render("ON", True, OtherConfigs.COLOR_RED)

						self._sound.musicPlaying = not self._sound.musicPlaying
						break 
					if self.position_selected==3:
						
						self._substate = SubstateConfigs.SUBSTATE_BACK
						break 

	"""
		Renders the Menu elements, background and logo
	"""


	def _render(self):

		#Blit to screen
		self._screen.blit(self._background, (0, 0))
		self._screen.blit(self._logo_image, (100,214))
		self._screen.blit(self._music,(500,305))

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
			self._menulist[i].element_rect.top = distance+(distance*2+height)*i

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

	"""
		This is the method that draws the menu every frame. It takes a move argument
		to ensure that the menu logic is respected. If move is -1, it moves up, if it is
		1, it moves down. If it is 0, it stays the same.

		@param move defines if the menu requires to change position.
	"""

	def move(self, move):

		self.position_before = self.position_selected

		#if a directional key is pressed
		self.position_selected += move 
		if self.position_selected == -1:
			self.position_selected = self._list_length-1
		self.position_selected %= self._list_length

		self.font = pygame.font.Font(OtherConfigs.FONT_PATH, OtherConfigs.FONT_SIZE)
		for i in xrange(self._list_length):
			self._menulist[i].surface = self.font.render(self._menulist[i].text, 1, OtherConfigs.COLOR_GRAY)

		self.font = pygame.font.Font(OtherConfigs.FONT_PATH, OtherConfigs.SELECTED_FONT_SIZE)
		self._menulist[self.position_selected].surface = self.font.render(self._menulist[self.position_selected].text, 1, OtherConfigs.COLOR_RED)