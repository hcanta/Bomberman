#Imports
import pygame, sys, math
from pygame.locals import*
sys.path.append("..")
from FileManagementPack.DatabaseMod import UserDatabase, HighscoreDatabase, MapDatabase
from ConfigPack.ConfigMod import AppConfigs, SubstateConfigs, OtherConfigs
from AppPack.SubstateMod import Substate
from LobbyPack.AuthInfoMod import AuthInfo
from GamePack.SoundMod import Sound

"""
	Lobby AuthMenu Substate.
	This is where the whole login logic is implemented.
"""
class AuthMenu(Substate):

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
		super(AuthMenu, self).__init__(screen, fpsclock, sound)

	"""
		See SubstateMod for details about this method's meaning.
		Initializes important surfaces and variables used throughout the log in/out process.
		It also initializes error messages.
	"""
	def _initObjects(self):
		self._list =  ['Player1','Player2', 'Quit']
		self._list_length = len(self._list)
		self.position_selected = 0
		self.__create_structure()

		self.__userDB = UserDatabase()
		self.__hsDB = HighscoreDatabase()

		self.__shiftPressed = False
		self.__isNewUser = False

		self.__p1EnteringUsername = False
		self.__p1Username = ""

		self.__p1EnteringPassword = False	
		self.__p1Password = ""
		self.__p1DisplayPassword  = ""

		self.__p2EnteringUsername = False
		self.__p2Username = ""

		self.__p2EnteringPassword = False	
		self.__p2Password = ""
		self.__p2DisplayPassword = ""

		self.__errorMessage = ""		
		self.__errorMessageMaxCounterVal = 120
		self.__errorMessageCurrentCounterVal = 0

		self.__warningMessage = ""		
		self.__warningMessageMaxCounterVal = 120
		self.__warningMessageCurrentCounterVal = 0

		self.__successMessage = ""		
		self.__successMessageMaxCounterVal = 120
		self.__successMessageCurrentCounterVal = 0

		self.__p1LoggedIn = False
		self.__p2LoggedIn = False

	"""
		See SubstateMod for details about this method's meaning.
		Initializes all the images and fonts needed for the menu.
	"""
	def _initImages(self):

		#Render Background
		self._background_file = "sprites/bg.jpg"
		self._background = pygame.image.load(self._background_file)

		#Render Logo
		self._logo_file = "sprites/logo.png"
		self._logo_image = pygame.image.load(self._logo_file)

		#Render Text
		self._fontt = pygame.font.Font("Fonts/coders_crux.ttf", 40)
		#self._errorfontt = pygame.font.Font("Fonts/coders_crux.ttf", 25)
		self._p1Username = self._fontt.render("Username: " + self.__p1Username, True, OtherConfigs.COLOR_RED)
		self._p1Password = self._fontt.render("Password: " + self.__p1DisplayPassword , True, OtherConfigs.COLOR_RED)	
		self._p2Username = self._fontt.render("Username: " + self.__p2Username, True, OtherConfigs.COLOR_RED)
		self._p2Password = self._fontt.render("Password: " + self.__p2DisplayPassword, True, OtherConfigs.COLOR_RED)	
		self._errorMessageDisplay = self._fontt.render(self.__errorMessage, True, OtherConfigs.COLOR_RED)	
		self._warningMessageDisplay = self._fontt.render(self.__warningMessage, True, OtherConfigs.COLOR_YELLOW)
		self._successMessageDisplay = self._fontt.render(self.__successMessage, True, OtherConfigs.COLOR_GREEN)

	"""
		See SubstateMod for details about this method's meaning.
		Is called every frame and is used to keep track of counters for error messages.
		Updates the menu if needed.
	"""
	def _ticked(self):

		#Return this if nothing changed
		self._substate = SubstateConfigs.SUBSTATE_AUTHMENU

		if(self.__errorMessageCurrentCounterVal > 0):
			self.__errorMessageCurrentCounterVal = self.__errorMessageCurrentCounterVal - 1
		if(self.__warningMessageCurrentCounterVal > 0):
			self.__warningMessageCurrentCounterVal = self.__warningMessageCurrentCounterVal - 1
		if(self.__successMessageCurrentCounterVal > 0):
			self.__successMessageCurrentCounterVal = self.__successMessageCurrentCounterVal - 1

		if((AuthInfo.user_one.username != "" or AuthInfo.user_two.username != "") and self._list[2] == "Quit"):
			self.__modify_structure(2, "Next")
		if(AuthInfo.user_one.username == "" and AuthInfo.user_two.username == "" and self._list[2] == "Next"):
			self.__modify_structure(2, "Quit")

	"""
		See SubstateMod for details about this method's meaning.
		Main event loop.
		Entering username and password logic is implemented here.
	"""
	def _listen(self):

		#Event queue loop
		for event in pygame.event.get():

			#Quit event
			if event.type == QUIT:
				pygame.quit()
				sys.exit()

			if event.type == KEYUP:
				if(event.key == K_LSHIFT or event.key == K_RSHIFT):
					self.__shiftPressed = False

			#Key events
			if event.type == KEYDOWN:

				if(event.key == K_LSHIFT or event.key == K_RSHIFT):
					self.__shiftPressed = True

				#Check if entering username
				if (self.__p1EnteringUsername):
					#ENTERING USERNAME LOGIC HERE
					self.__enteringUsernameP1(event.key)
					break

				#check if entering pasword
				if (self.__p1EnteringPassword):
					#ENTERING PASSWORD AND LOGIN LOGIC HERE
					self.__enteringPasswordP1(event.key)
					break

				#Check if entering username
				if (self.__p2EnteringUsername):
					#ENTERING USERNAME LOGIC HERE
					self.__enteringUsernameP2(event.key)
					break

				#check if entering pasword
				if (self.__p2EnteringPassword):
					#ENTERING PASSWORD AND LOGIN LOGIC HERE
					self.__enteringPasswordP2(event.key)
					break


				if event.key  == K_UP:
					self.move(-1) 
				if event.key == K_DOWN:
					self.move(1)
				if event.key == K_RETURN:
					if self.position_selected == 0:
						if(not self.__p1LoggedIn):
							self.__p1EnteringUsername = True
						else:
							self.__p1LoggedIn = False
							self.__setSuccessMessage(AuthInfo.user_one.username + " succesfully logged out")
							AuthInfo.user_one.destroy()
							self.__modify_structure(0, "Player1")
						break
					if self.position_selected == 1:
						if(not self.__p2LoggedIn):
							self.__p2EnteringUsername = True
						else:
							self.__p2LoggedIn = False
							self.__setSuccessMessage(AuthInfo.user_two.username + " succesfully logged out")
							AuthInfo.user_two.destroy()
							self.__modify_structure(1, "Player2")
						break
					if self.position_selected == 2:
						if self._list[2] == "Quit":
							pygame.quit()
							sys.exit()
						elif self._list[2] == "Next":
							self._substate = SubstateConfigs.SUBSTATE_MAINMENU
						break 

	"""
		This method sets the success message to the string specified. 
		It also resets the success message display timer.

		@param message is the success message to be displayed.
	"""
	def __setSuccessMessage(self, message):
		self.__successMessageCurrentCounterVal = self.__successMessageMaxCounterVal
		self.__successMessage = message		
		self._successMessageDisplay = self._fontt.render(self.__successMessage, True, OtherConfigs.COLOR_GREEN)

	"""
		This method sets the error message to the string specified. 
		It also resets the error message display timer.

		@param message is the error message to be displayed.
	"""
	def __setErrorMessage(self, message):
		self.__errorMessageCurrentCounterVal = self.__errorMessageMaxCounterVal
		self.__errorMessage = message		
		self._errorMessageDisplay = self._fontt.render(self.__errorMessage, True, OtherConfigs.COLOR_RED)

	"""
		This method sets the warning message to the string specified. 
		It also resets the warning message display timer.

		@param message is the warning message to be displayed.
	"""
	def __setWarningMessage(self, message):
		self.__warningMessageCurrentCounterVal = self.__warningMessageMaxCounterVal
		self.__warningMessage = message		
		self._warningMessageDisplay = self._fontt.render(self.__warningMessage, True, OtherConfigs.COLOR_YELLOW)


	"""
		This method checks whether the entered key is valid.
		Valid keys are the numbers 0-9, and the letters a-z and A-Z.

		@param key is the ascii code value of the key that was pressed.
	"""
	def __checkIfValidKey(self, key):
		return ((key >= 48 and key <= 57) or (key >= 65 and key <= 90) or (key >= 97 and key <= 122))

	"""
		This methods is the logic to enter the username for player 1.

		@param key is the ascii code value of the key that was pressed.
	"""
	def __enteringUsernameP1(self, key):
		if (self.__checkIfValidKey(key)):
			if(self.__shiftPressed == True):
				if(not(key >= 48 and key <= 57)):
					self.__p1Username += chr(key - 32)
			else:
				self.__p1Username += chr(key)
			self._p1Username = self._fontt.render("Username: " + self.__p1Username, True, OtherConfigs.COLOR_RED)


		#check if backspace
		if(key == K_BACKSPACE):
			if(len(self.__p1Username) > 0):
				self.__p1Username = self.__p1Username[:-1]
				self._p1Username = self._fontt.render("Username: " + self.__p1Username, True, OtherConfigs.COLOR_RED)

		
		#check if pressed enter
		if key == K_RETURN or key == K_TAB:
			# Check if username is empty
			if(self.__p1Username == ""):
				self.__setErrorMessage("Empty Username")
				self.__p1EnteringUsername = False
				return
			elif(len(self.__p1Username) < 4):
				self.__setErrorMessage("Username must be at least 4 characters")
				self.__p1EnteringUsername = False
				self.__p1Username = ""
				self._p1Username = self._fontt.render("Username: " + self.__p1Username, True, OtherConfigs.COLOR_RED)
				return
			elif(len(self.__p1Username) > 14):
				self.__setErrorMessage("Username must be less than 15 characters")
				self.__p1EnteringUsername = False
				self.__p1Username = ""
				self._p1Username = self._fontt.render("Username: " + self.__p1Username, True, OtherConfigs.COLOR_RED)
				return
			
			elif(self.__p1Username == AuthInfo.user_two.username):
				self.__setErrorMessage("User already logged in")
				self.__p1EnteringUsername = False
				self.__p1Username = ""
				self._p1Username = self._fontt.render("Username: " + self.__p1Username, True, OtherConfigs.COLOR_RED)
				return
			if(self.__userDB.verifyUsernameUnique(self.__p1Username) == True):
				self.__setWarningMessage("Account creation!")
				self.__setErrorMessage("Press escape to restart log in.")
				self.__isNewUser = True

			self.__p1EnteringUsername = False
			self.__p1EnteringPassword = True

		if key == K_ESCAPE:
			# EMPTY USERNAME STRING AND PASSWORD STRING
			self.__p1Username = ""	
			self.__p1Password = ""
			self.__p1DisplayPassword  = ""
			self._p1Username = self._fontt.render("Username: " + self.__p1Username, True, OtherConfigs.COLOR_RED)
			self._p1Password = self._fontt.render("Password: " + self.__p1DisplayPassword , True, OtherConfigs.COLOR_RED)
			self.__p1EnteringUsername = False
			self.__isNewUser = False

	"""
		This methods is the logic to enter the username for player 2.

		@param key is the ascii code value of the key that was pressed.
	"""
	def __enteringUsernameP2(self, key):
		if (self.__checkIfValidKey(key)):
			if(self.__shiftPressed == True):
				if(not(key >= 48 and key <= 57)):
					self.__p2Username += chr(key - 32)
			else:
				self.__p2Username += chr(key)
			self._p2Username = self._fontt.render("Username: " + self.__p2Username, True, OtherConfigs.COLOR_RED)


		#check if backspace
		if(key == K_BACKSPACE):
			if(len(self.__p2Username) > 0):
				self.__p2Username = self.__p2Username[:-1]
				self._p2Username = self._fontt.render("Username: " + self.__p2Username, True, OtherConfigs.COLOR_RED)

		
		#check if pressed enter
		if key == K_RETURN or key == K_TAB:
			# Check if username is empty
			if(self.__p2Username == ""):
				self.__setErrorMessage("Empty Username")
				self.__p2EnteringUsername = False
				return
			elif(len(self.__p2Username) < 4):
				self.__setErrorMessage("Username must be at least 4 characters")
				self.__p2EnteringUsername = False
				self.__p2Username = ""
				self._p2Username = self._fontt.render("Username: " + self.__p2Username, True, OtherConfigs.COLOR_RED)
				return
			elif(len(self.__p2Username) > 14):
				self.__setErrorMessage("Username must be less than 15 characters")
				self.__p2EnteringUsername = False
				self.__p2Username = ""
				self._p2Username = self._fontt.render("Username: " + self.__p2Username, True, OtherConfigs.COLOR_RED)
				return
			elif(self.__p2Username == AuthInfo.user_one.username):
				self.__setErrorMessage("User already logged in")
				self.__p2EnteringUsername = False
				self.__p2Username = ""
				self._p2Username = self._fontt.render("Username: " + self.__p2Username, True, OtherConfigs.COLOR_RED)
				return
			if(self.__userDB.verifyUsernameUnique(self.__p2Username) == True):
				self.__setWarningMessage("Account creation!")
				self.__setErrorMessage("Press escape to restart log in.")
				self.__isNewUser = True

			self.__p2EnteringUsername = False
			self.__p2EnteringPassword = True

		if key == K_ESCAPE:
			self.__p2Username = ""	
			self.__p2Password = ""
			self.__p2DisplayPassword = ""
			self._p2Username = self._fontt.render("Username: " + self.__p2Username, True, OtherConfigs.COLOR_RED)
			self._p2Password = self._fontt.render("Password: " + self.__p2DisplayPassword, True, OtherConfigs.COLOR_RED)
			self.__p2EnteringUsername = False
			self.__isNewUser = False

	"""
		This methods is the logic to enter the password for player 1.
		It also does the logging in logic as well as creating an account id the username doesn't exist

		@param key is the ascii code value of the key that was pressed.
	"""
	def __enteringPasswordP1(self, key):
		#check inputs
		if (self.__checkIfValidKey(key)): 
			if(self.__shiftPressed == True):
				if(not(key >= 48 and key <= 57)):
					self.__p1Password += chr(key - 32)
					self.__p1DisplayPassword  += "*"
			else:
				self.__p1Password += chr(key)
				self.__p1DisplayPassword  += "*"

		#check if backspace
		if(key == K_BACKSPACE):
			if(len(self.__p1Password) > 0):
				self.__p1Password = self.__p1Password[:-1]
				self.__p1DisplayPassword  = self.__p1DisplayPassword [:-1]

		self._p1Password = self._fontt.render("Password: " + self.__p1DisplayPassword , True, OtherConfigs.COLOR_RED)

		# LOGIN VERIFICATION FOR PLAYER1
		if key == K_RETURN or key == K_TAB:
			if(self.__p1Password == ""):
				self.__setErrorMessage("Empty Password")
			elif(self.__isNewUser == True):
				self.__userDB.addUser(self.__p1Username, self.__p1Password)
				self.__p1LoggedIn = True
				AuthInfo.user_one.create(self.__p1Username)
				self.__setSuccessMessage(AuthInfo.user_one.username + "'s account was successfully created")
				self.__modify_structure(0, "Player1: " + AuthInfo.user_one.username)

			elif(self.__userDB.isPasswordValidFor(self.__p1Username, self.__p1Password) == False):
				self.__setErrorMessage("Invalid Password")
			else:
				self.__p1LoggedIn = True
				AuthInfo.user_one.create(self.__p1Username)
				self.__setSuccessMessage(AuthInfo.user_one.username + " successfully logged in")
				self.__modify_structure(0, "Player1: " + AuthInfo.user_one.username)

			# EMPTY USERNAME STRING AND PASSWORD STRING
			self.__p1Username = ""	
			self.__p1Password = ""
			self.__p1DisplayPassword  = ""
			self._p1Username = self._fontt.render("Username: " + self.__p1Username, True, OtherConfigs.COLOR_RED)
			self._p1Password = self._fontt.render("Password: " + self.__p1DisplayPassword , True, OtherConfigs.COLOR_RED)
			self.__p1EnteringPassword = False
			self.__isNewUser = False

		if key == K_ESCAPE:
			# EMPTY USERNAME STRING AND PASSWORD STRING
			self.__p1Username = ""	
			self.__p1Password = ""
			self.__p1DisplayPassword  = ""
			self._p1Username = self._fontt.render("Username: " + self.__p1Username, True, OtherConfigs.COLOR_RED)
			self._p1Password = self._fontt.render("Password: " + self.__p1DisplayPassword , True, OtherConfigs.COLOR_RED)
			self.__p1EnteringPassword = False
			self.__isNewUser = False

	"""
		This methods is the logic to enter the password for player 2.
		It also does the logging in logic as well as creating an account id the username doesn't exist

		@param key is the ascii code value of the key that was pressed.
	"""
	def __enteringPasswordP2(self, key):
		#check inputs
		if (self.__checkIfValidKey(key)): 
			if(self.__shiftPressed == True):
				if(not(key >= 48 and key <= 57)):
					self.__p2Password += chr(key - 32)
					self.__p2DisplayPassword += "*"
			else:
				self.__p2Password += chr(key)
				self.__p2DisplayPassword += "*"

		#check if backspace
		if(key == K_BACKSPACE):
			if(len(self.__p2Password) > 0):
				self.__p2Password = self.__p2Password[:-1]
				self.__p2DisplayPassword = self.__p2DisplayPassword[:-1]

		self._p2Password = self._fontt.render("Password: " + self.__p2DisplayPassword, True, OtherConfigs.COLOR_RED)

		# LOGIN VERIFICATION FOR PLAYER1
		if key == K_RETURN or key == K_TAB:
			if(self.__p2Password == ""):
				self.__setErrorMessage("Empty Password")
			elif(self.__isNewUser == True):
				self.__userDB.addUser(self.__p2Username, self.__p2Password)
				self.__p2LoggedIn = True
				AuthInfo.user_two.create(self.__p2Username)
				self.__setSuccessMessage(AuthInfo.user_two.username + "'s account was successfully created")
				self.__modify_structure(1, "Player2: " + AuthInfo.user_two.username)

			elif(self.__userDB.isPasswordValidFor(self.__p2Username, self.__p2Password) == False):
				self.__setErrorMessage("Invalid Password")
			else:
				self.__p2LoggedIn = True
				AuthInfo.user_two.create(self.__p2Username)
				self.__setSuccessMessage(AuthInfo.user_two.username + " successfully logged in")
				self.__modify_structure(1, "Player2: " + AuthInfo.user_two.username)

			# EMPTY USERNAME STRING AND PASSWORD STRING
			self.__p2Username = ""	
			self.__p2Password = ""
			self.__p2DisplayPassword = ""
			self._p2Username = self._fontt.render("Username: " + self.__p2Username, True, OtherConfigs.COLOR_RED)
			self._p2Password = self._fontt.render("Password: " + self.__p2DisplayPassword, True, OtherConfigs.COLOR_RED)
			self.__p2EnteringPassword = False
			self.__isNewUser = False

		if key == K_ESCAPE:
			# EMPTY USERNAME STRING AND PASSWORD STRING
			self.__p2Username = ""	
			self.__p2Password = ""
			self.__p2DisplayPassword = ""
			self._p2Username = self._fontt.render("Username: " + self.__p2Username, True, OtherConfigs.COLOR_RED)
			self._p2Password = self._fontt.render("Password: " + self.__p2DisplayPassword, True, OtherConfigs.COLOR_RED)
			self.__p2EnteringPassword = False
			self.__isNewUser = False			

	"""
		See SubstateMod for details about this method's meaning.
		Renders username, password, error messages and the menu.
	"""
	def _render(self):

		self._screen.blit(self._background, (0, 0))

		self._screen.blit(self._logo_image, (30,214))

		if(self.__p1EnteringUsername or self.__p1Username != ""):
			self._screen.blit(self._p1Username, (225,390))
		if(self.__p1EnteringPassword or self.__p1Password != ""):
			self._screen.blit(self._p1Password, (225,430))

		if(self.__p2EnteringUsername or self.__p2Username != ""):
			self._screen.blit(self._p2Username, (225,390))
		if(self.__p2EnteringPassword or self.__p2Password != ""):
			self._screen.blit(self._p2Password, (225,430))

		if(self.__errorMessageCurrentCounterVal > 0):
			self._screen.blit(self._errorMessageDisplay, (60, 110))

		if(self.__warningMessageCurrentCounterVal > 0):
			self._screen.blit(self._warningMessageDisplay, (60, 75))

		if(self.__successMessageCurrentCounterVal > 0):
			self._screen.blit(self._successMessageDisplay, (60, 40))

		#Blit Menu
		for i in xrange(self._list_length):
			if i != self.position_selected:
				self._screen.blit(self._menulist[i].surface,(self.menu_coordinates[0]+self._menulist[i].element_rect.x, self.menu_coordinates[1]+self._menulist[i].element_rect.y))
			else:
				self._screen.blit(self._menulist[i].surface,(self.menu_coordinates[0]+self._menulist[i].element_rect.x, self.menu_coordinates[1]+self._menulist[i].element_rect.y-6))
	 

	"""
		This method modifies the menu string at a given index.
		This is called when a player logs in or when both players are logged out.

		@param idx is the index at which you want to insert the value.
		@param value is the value to be inserted at the given index.
	"""
	def __modify_structure(self, idx, value):
		self.font = pygame.font.Font(OtherConfigs.FONT_PATH, OtherConfigs.FONT_SIZE) 
		self._menulist = []
		for i in xrange(self._list_length):
			if(i == idx):
				self._list[i] = value
				self._menulist.append(self.MenuElement())
				self._menulist[i].text = self._list[i]
				self._menulist[i].surface = self.font.render(self._menulist[i].text, 1, OtherConfigs.COLOR_GRAY)
				self._menulist[i].element_rect = self._menulist[i].surface.get_rect() 
			else:	
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

			self._menulist[i].selected_rect = (left, top, width, height)

		self.font = pygame.font.Font(OtherConfigs.FONT_PATH, OtherConfigs.SELECTED_FONT_SIZE-10)
		self._menulist[self.position_selected].surface = self.font.render(self._menulist[self.position_selected].text, 1, OtherConfigs.COLOR_RED)	

	"""
		This creates the menu, positions it and it initializes the whole menu logic.
	"""

	def __create_structure(self):
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

		self.font = pygame.font.Font(OtherConfigs.FONT_PATH, OtherConfigs.SELECTED_FONT_SIZE-10)
		self._menulist[self.position_selected].surface = self.font.render(self._menulist[self.position_selected].text, 1, OtherConfigs.COLOR_RED)

		#center the text list on the screen
		x = self._screen.get_rect().centerx - menu_width / 2 
		y = self._screen.get_rect().centery - menu_height / 2

		self.menu_coordinates = (x-100,y)
    
    
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

		self.font = pygame.font.Font(OtherConfigs.FONT_PATH, OtherConfigs.SELECTED_FONT_SIZE-10)
		self._menulist[self.position_selected].surface = self.font.render(self._menulist[self.position_selected].text, 1, OtherConfigs.COLOR_RED)