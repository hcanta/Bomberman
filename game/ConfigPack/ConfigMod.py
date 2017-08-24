import os

class AppConfigs:

	#Window Configs
	WINDOWNAME = "Hai Bomb"
	WINDOWSIZE = WINDOWX, WINDOWY = 800,600

	#Render Configs
	FPS = 30

	#State Configs
	STATE_LOBBY = 40
	STATE_GAME = 50

class SubstateConfigs:

	#Substate Configs
	SUBSTATE_INGAME = 0
	SUBSTATE_INMENU = 1
	SUBSTATE_INMULT = 2
	SUBSTATE_INMULTALT = 3
	SUBSTATE_AUTHMENU = 4
	SUBSTATE_MAINMENU = 5
	SUBSTATE_OPTIONSMENU = 6
	SUBSTATE_STATSMENU = 7
	SUBSTATE_RESTART = 8
	SUBSTATE_BACK = -1
	SUBSTATE_GAMEOVER = 20
	SUBSTATE_WIN = 60
	SUBSTATE_UNDEFINED = -10 #For initialization problems

class GameConfigs:
	EMPTY ="0"
	EMPTY_CRATE ="E"
	WALL ="W"
	BOMB = "B"
	BONUS0 ="B0"
	BONUS1 ="B1"
	BONUS2 ="B2"
	EXIT = "Ex"
	MONSTER0 = "M0"
	MONSTER1= "M1"
	MONSTER2 = "M2"
	MONSTER3 = "M3"
	TILE_RESOLUTION = 40
	BOARD_SIZE = 14

class FMConfigs:

	#Crypto	
	CAESARCONSTANT = 5
	#file path
	PATH = "Data"
	CREDENTIALS = os.path.abspath(os.path.join(PATH, "credentials.txt"))
	STATISTICS = os.path.abspath(os.path.join(PATH, "statistics.txt"))
	MAPS = os.path.abspath(os.path.join(PATH, "maps.txt"))

class OtherConfigs:

	#Color Configs
	COLOR_GRAY     = (100, 100, 100)
	COLOR_NAVYBLUE = ( 60,  60, 100)
	COLOR_WHITE    = (255, 255, 255)
	COLOR_RED      = (255,   0,   0)
	COLOR_GREEN    = (	0, 255,   0)
	COLOR_BLUE     = (  0,   0, 255)
	COLOR_YELLOW   = (255, 255,   0)
	COLOR_ORANGE   = (255, 128,   0)
	COLOR_PURPLE   = (255,   0, 255)
	COLOR_CYAN     = (  0, 255, 255)
	COLOR_BLACK    = (  0,   0,   0)

	#Font Configs
	FONT_SIZE = 50
	SELECTED_FONT_SIZE = 70
	USER_FONT_SIZE = 20
	STATS_FONT_SIZE = 30
	FONT_PATH = 'Fonts/coders_crux.ttf'



