#Imports
import random,pygame, sys, math
from pygame.locals import*
sys.path.append("..")
from ConfigPack.ConfigMod import AppConfigs, GameConfigs, OtherConfigs, SubstateConfigs
from AppPack.SubstateMod import Substate
from GamePack.MapMod import Map 
from GamePack.TileMod import Tile
from GamePack.PlayerMod import Player
from GamePack.MonsterMod import Monster
from GamePack.BombMod import Bomb
from LobbyPack.AuthInfoMod import AuthInfo
from LobbyPack.AuthInfoMod import User
from GamePack.SoundMod import Sound
from FileManagementPack.DatabaseMod import HighscoreDatabase
"""Game InGame Substate"""
class InGame(Substate):

	""" Initiates a single player game"""
	def __init__(self, screen, fpsclock, sound):
		super(InGame, self).__init__(screen, fpsclock, sound)

	""" initiates all object for the game to run map, monsters and players"""
	def _initObjects(self):
		self._map = Map()

		self._player =  AuthInfo.user_one

		if self._player.username == "":
			self._player =  AuthInfo.user_two
		self._highScoreDB = HighscoreDatabase()

		self._level = self._highScoreDB.getCurrentLevelOf(self._player.username)

		if self._level == 0:
			self._map._levelOne()
			self._level = 1
		elif self._level == 1:
			self._map._levelOne()

		elif self._level == 2:
			self._map._levelTwo()
		elif self._level == 3:
			self._map._levelThree()
		elif self._level == 4:
			self._map._levelFour()
		elif self._level == 5:
			self._map._levelFive()
		elif self._level == 6:
			self._map._levelSix()
		elif self._level == 7:
			self._map._levelSeven()
		elif self._level == 8:
			self._map._levelEight()


		self._startIdx = self._map._getStartPosition()
		self._exitIdx = self._map._getExitIdx()	



		self._maxLevelCompleted =  self._player.maxLevelAchieved

		self._player1 = Player(0, AuthInfo.user_one.username,0)
		self._player1._setLives(self._highScoreDB.getCurrNumLives(self._player.username))
		monsters = self._map._getMonsters()
		monsterType = monsters[0]
		monsterIdx = monsters[1]
		self._monsters = []
		for m in range(len(monsterType)):
			self._monsters.append( Monster(monsterType[m],monsterIdx[m]))


		self._Counter = 0
		self._Timer = 300
		self._random = False # for the demo
	"""Initiates all images for the game """
	def _initImages(self):

		#Render Background
		self._background_file = "sprites/sample.jpg"
		self._background = pygame.image.load(self._background_file)

		#Render Logo
		self._ground_file = "sprites/grey2.jpg"
		self._crate_file = "sprites/crates2.png"
		self._wall_file = "sprites/wall2.png"

		self._p1d1_file = "sprites/p1d1.gif"
		self._p1d2_file = "sprites/p1d2.gif"
		self._bomb_file = "sprites/bomb.gif"

		self._expc1_file ="sprites/bomb1/middle1.gif"
		self._expc2_file ="sprites/bomb2/middle2.gif"
		self._expc3_file ="sprites/bomb3/middle3.gif"
		self._expc4_file ="sprites/bomb4/middle4.gif"




		self._expdm1_file ="sprites/bomb1/down-middle1.gif"
		self._expdm2_file ="sprites/bomb2/down-middle2.gif"
		self._expdm3_file ="sprites/bomb3/down-middle3.gif"
		self._expdm4_file ="sprites/bomb4/down-middle4.gif"

		self._expdd1_file ="sprites/bomb1/down-down1.gif"
		self._expdd2_file ="sprites/bomb2/down-down2.gif"
		self._expdd3_file ="sprites/bomb3/down-down3.gif"
		self._expdd4_file ="sprites/bomb4/down-down4.gif"

		self._expum1_file ="sprites/bomb1/up-middle1.gif"
		self._expum2_file ="sprites/bomb2/up-middle2.gif"
		self._expum3_file ="sprites/bomb3/up-middle3.gif"
		self._expum4_file ="sprites/bomb4/up-middle4.gif"

		self._expuu1_file ="sprites/bomb1/up-up1.gif"
		self._expuu2_file ="sprites/bomb2/up-up2.gif"
		self._expuu3_file ="sprites/bomb3/up-up3.gif"
		self._expuu4_file ="sprites/bomb4/up-up4.gif"


		self._explm1_file ="sprites/bomb1/left-middle1.gif"
		self._explm2_file ="sprites/bomb2/left-middle2.gif"
		self._explm3_file ="sprites/bomb3/left-middle3.gif"
		self._explm4_file ="sprites/bomb4/left-middle4.gif"

		self._expll1_file ="sprites/bomb1/left-left1.gif"
		self._expll2_file ="sprites/bomb2/left-left2.gif"
		self._expll3_file ="sprites/bomb3/left-left3.gif"
		self._expll4_file ="sprites/bomb4/left-left4.gif"

		self._exprm1_file ="sprites/bomb1/right-middle1.gif"
		self._exprm2_file ="sprites/bomb2/right-middle2.gif"
		self._exprm3_file ="sprites/bomb3/right-middle3.gif"
		self._exprm4_file ="sprites/bomb4/right-middle4.gif"

		self._exprr1_file ="sprites/bomb1/right-right1.gif"
		self._exprr2_file ="sprites/bomb2/right-right2.gif"
		self._exprr3_file ="sprites/bomb3/right-right3.gif"
		self._exprr4_file ="sprites/bomb4/right-right4.gif"


		self._p1u1_file = "sprites/p1u1.gif"
		self._p1u2_file = "sprites/p1u2.gif"
		self._p1l1_file = "sprites/p1l1.gif"
		self._p1l2_file = "sprites/p1l2.gif"
		self._p1r1_file = "sprites/p1r1.gif"
		self._p1r2_file = "sprites/p1r2.gif"
		self._bonus0_file = "sprites/health.png"
		self._bonus1_file = "sprites/extra_bomb.gif"
		self._bonus2_file = "sprites/range.png"
		self._exit_file = "sprites/exit.png"
		self._lives_file = "sprites/heart.png"

		self._monster_file = "sprites/M0.gif"
		self._monster1_file = "sprites/M1.gif"
		self._monster2_file = "sprites/M2.gif"


		self._ground_image = pygame.image.load(self._ground_file)
		self._crate_image = pygame.image.load(self._crate_file)
		self._wall_image = pygame.image.load(self._wall_file)
		self._p1d1_image = pygame.image.load(self._p1d1_file)		
		self._p1d2_image = pygame.image.load(self._p1d2_file)
		self._bomb_image = pygame.image.load(self._bomb_file)

		self._expc1_image = pygame.image.load(self._expc1_file)
		self._expc2_image = pygame.image.load(self._expc2_file)
		self._expc3_image = pygame.image.load(self._expc3_file)
		self._expc4_image = pygame.image.load(self._expc4_file)



		self._expdm1_image = pygame.image.load(self._expdm1_file)
		self._expdm2_image = pygame.image.load(self._expdm2_file)
		self._expdm3_image = pygame.image.load(self._expdm3_file)
		self._expdm4_image = pygame.image.load(self._expdm4_file)

		self._expdd1_image = pygame.image.load(self._expdd1_file)
		self._expdd2_image = pygame.image.load(self._expdd2_file)
		self._expdd3_image = pygame.image.load(self._expdd3_file)
		self._expdd4_image = pygame.image.load(self._expdd4_file)

		self._expum1_image = pygame.image.load(self._expum1_file)
		self._expum2_image = pygame.image.load(self._expum2_file)
		self._expum3_image = pygame.image.load(self._expum3_file)
		self._expum4_image = pygame.image.load(self._expum4_file)

		self._expuu1_image = pygame.image.load(self._expuu1_file)
		self._expuu2_image = pygame.image.load(self._expuu2_file)
		self._expuu3_image = pygame.image.load(self._expuu3_file)
		self._expuu4_image = pygame.image.load(self._expuu4_file)


		self._explm1_image = pygame.image.load(self._explm1_file)
		self._explm2_image = pygame.image.load(self._explm2_file)
		self._explm3_image = pygame.image.load(self._explm3_file)
		self._explm4_image = pygame.image.load(self._explm4_file)

		self._expll1_image = pygame.image.load(self._expll1_file)
		self._expll2_image = pygame.image.load(self._expll2_file)
		self._expll3_image = pygame.image.load(self._expll3_file)
		self._expll4_image = pygame.image.load(self._expll4_file)

		self._exprm1_image = pygame.image.load(self._exprm1_file)
		self._exprm2_image = pygame.image.load(self._exprm2_file)
		self._exprm3_image = pygame.image.load(self._exprm3_file)
		self._exprm4_image = pygame.image.load(self._exprm4_file)

		self._exprr1_image = pygame.image.load(self._exprr1_file)
		self._exprr2_image = pygame.image.load(self._exprr2_file)
		self._exprr3_image = pygame.image.load(self._exprr3_file)
		self._exprr4_image = pygame.image.load(self._exprr4_file)


		self._p1u1_image = pygame.image.load(self._p1u1_file)
		self._p1u2_image = pygame.image.load(self._p1u2_file)

		self._p1l1_image = pygame.image.load(self._p1l1_file)
		self._p1l2_image = pygame.image.load(self._p1l2_file)

		self._p1r1_image = pygame.image.load(self._p1r1_file)
		self._p1r2_image = pygame.image.load(self._p1r2_file)

		self._bonus0_image = pygame.image.load(self._bonus0_file)
		self._bonus1_image = pygame.image.load(self._bonus1_file)
		self._bonus2_image = pygame.image.load(self._bonus2_file)

		self._exit_image = pygame.image.load(self._exit_file)

		self._lives_image = pygame.image.load(self._lives_file)
		self._monster_image = pygame.image.load(self._monster_file)
		self._monster1_image = pygame.image.load(self._monster1_file)
		self._monster2_image = pygame.image.load(self._monster2_file)

		#Render Text
		self._fontt = pygame.font.Font("freesansbold.ttf", 20)


		self._playerName = self._fontt.render(self._player1._getName()[:15]+'..' if len( self._player1._getName())>15 else  self._player1._getName(), True, OtherConfigs.COLOR_BLACK)
		self._playerStats = self._fontt.render("Current Stats", True, OtherConfigs.COLOR_BLACK)

		self._playerOStats = self._fontt.render("Overall Stats", True, OtherConfigs.COLOR_BLACK)

	"""Once a level is completed this method is called to load the new level"""
	def _nextLevel(self):
		_timer = pygame.time.Clock()
		self._level+=1
		self._Timer = 300
		if self._level > self._highScoreDB.getMaxLevelAchievedOf((self._player.username)):
			self._highScoreDB.updateMaxLevelAchievedFor(self._player.username,self._level)
		self._highScoreDB.addLevelsCompletedFor(self._player.username,1)
		self._highScoreDB.updateCurrentLevelFor(self._player.username,(self._level))

		self._map._clear()
		self._player1._reset()
		if self._random or self._level>5:
			self._highScoreDB.updateCurrentLevelFor(self._player.username,(1))
 			self._highScoreDB.updateCurrNumLivesFor(self._player.username,3)
			self._substate = SubstateConfigs.SUBSTATE_WIN						
			self._map._random()
			self._player1._setTileID(0)

		elif self._level == 2:
			self._map._levelTwo()
		elif self._level == 3:
			self._map._levelThree()
		elif self._level == 4:
			self._map._levelFour()
		elif self._level == 5:
			self._map._levelFive()
		elif self._level == 6:
			self._map._levelSix()
		elif self._level == 7:
			self._map._levelSeven()
		elif self._level == 8:
			self._map._levelEight()
		self._startIdx = self._map._getStartPosition()
		self._exitIdx = self._map._getExitIdx()	
		self._player1._setTileID(self._startIdx)
		monsters = self._map._getMonsters()
		monsterType = monsters[0]
		monsterIdx = monsters[1]
		del(self._monsters)
		self._monsters = []
		for m in range(len(monsterType)):
			self._monsters.append( Monster(monsterType[m],monsterIdx[m]))

	def _ticked(self):

		#Return this if nothing changed
		self._substate = SubstateConfigs.SUBSTATE_INGAME

		if self._isTimeOver():
			pass
			#self._substate = SubstateConfigs.SUBSTATE_INMENU
		self._player1._pulseInvulnerable()
		for m in range(len(self._monsters)):
			self._monsters[m]._increaseMovePulse()

		for b_idx in range(len(self._map._getBombList())):
			self._map._getBombList()[b_idx]._pulse()
			if self._map._getBombList()[b_idx]._explosion():
				self._map._getBombList()[b_idx]._explodePulse()
				self._map._getBombList()[b_idx]._pulse()
				if  not self._map._getBombList()[b_idx]._getSound() :
					self._sound.playsound('Bomb')
					self._map._getBombList()[b_idx]._setPlayed()
		self._Counter += 1
		if self._Counter == 35:
			self._Counter = 0
			self._Timer -= 1

		if self._map._getBoard()[self._exitIdx]._getContent==GameConfigs.EMPTY:
			self._map._getBoard()[self._exitIdx]._setContent(GameConfigs.EXIT)

	""" Check for game over, player is dead or time ran out """
	def _isTimeOver(self):		 		
 		
 		done = False
 		if (self._Timer <1) or (self._player1._isDeadGameOver()):
 			done = True 
 		if done: 
 			self._highScoreDB.updateCurrentLevelFor(self._player.username,(1))
 			self._highScoreDB.updateCurrNumLivesFor(self._player.username,3)
 			self._substate = SubstateConfigs.SUBSTATE_GAMEOVER
 		return done

 	""" Check the player next move and load the next frame accordingly"""
	def _player1Move(self,boardIndex, x_offset, y_offset, playerObject):
		if not self._isTimeOver():

			if self._map._getBoard()[boardIndex]._getContent() !=GameConfigs.BOMB and self._map._getBoard()[boardIndex]._getContent() !=GameConfigs.MONSTER0:
				self._map._getBoard()[boardIndex]._setContent(GameConfigs.EMPTY)
				self._map._getBoard()[boardIndex]._setWalkable(True)
			playerObject._setX(playerObject._getX()+x_offset)
			playerObject._setY(playerObject._getY()+y_offset)
			idx = playerObject._getY() * GameConfigs.BOARD_SIZE + playerObject._getX()

			if self._map._getBoard()[idx]._getContent() == GameConfigs.EXIT:
				bombToRemove = []				
				for b_idx in range(len(self._map._getBombList())):
					bombToRemove.append(self._map._getBombList()[b_idx])

				for br_idx in range(len(bombToRemove)):
					if bombToRemove[br_idx]._getOwner() == playerObject._getID():
						playerObject._decreaseBombPlaced(); 
					self._map._removeBomb(bombToRemove[br_idx])
				del(bombToRemove)


				self._nextLevel()
			elif (self._map._getBoard()[idx]._getContent() == GameConfigs.MONSTER0) or  (self._map._getBoard()[idx]._getContent() == GameConfigs.MONSTER1 ) or  (self._map._getBoard()[idx]._getContent() == GameConfigs.MONSTER2)   or  (self._map._getBoard()[idx]._getContent() == GameConfigs.MONSTER3):
					playerObject._decreaseLives()
					playerObject._resetInvulnerablePulse()
					playerObject._setTileID(idx)
					self._map._getBoard()[self._startIdx]._setContent("P1")
					self._player1._setTileID(self._startIdx)

			else:
				if self._map._getBoard()[idx]._getContent() == GameConfigs.BONUS0:
					self._sound.playsound('Powerup')
					playerObject._increaseLives()
				elif self._map._getBoard()[idx]._getContent() == GameConfigs.BONUS1:
					self._sound.playsound('Powerup')
					playerObject._increaseBombMax()
				elif self._map._getBoard()[idx]._getContent() == GameConfigs.BONUS2:
					self._sound.playsound('Powerup')
					playerObject._increaseRange()


				self._map._getBoard()[idx]._setContent("P1")
				self._map._getBoard()[idx]._setWalkable(True)
				playerObject._setTileID(idx)


	def _monsterAction(self,move, monsterObject):

		if move== "left":
			if self._map._canMoveLeft(monsterObject._getX(),monsterObject._getY()) :
				self._map._getBoard()[monsterObject._getTileID()]._setContent(self._map._getBoard()[monsterObject._getTileID()]._getNextContent())
				self._map._getBoard()[monsterObject._getTileID()]._setNextContent(GameConfigs.EMPTY)
				self._map._getBoard()[monsterObject._getTileID()]._setWalkable(True)
				monsterObject._setX(monsterObject._getX()-1)

				idx = monsterObject._getY() * GameConfigs.BOARD_SIZE + monsterObject._getX()
				if self._map._getBoard()[idx]._getContent() == "P1":
					self._player1._decreaseLives()

					self._player1._resetInvulnerablePulse()
					self._map._getBoard()[self._startIdx]._setContent("P1")
					self._player1._setTileID(self._startIdx)
				if self._map._getBoard()[idx]._getContent() == GameConfigs.EXIT:
					self._map._getBoard()[idx]._setNextContent(GameConfigs.EXIT)

				self._map._getBoard()[idx]._setContent(monsterObject._getTypeID())
				#self._map._getBoard()[idx]._setWalkable(False)
				monsterObject._setTileID(idx)
		elif move =="right":
			if self._map._canMoveRight(monsterObject._getX(),monsterObject._getY()) :
				self._map._getBoard()[monsterObject._getTileID()]._setContent(self._map._getBoard()[monsterObject._getTileID()]._getNextContent())
				self._map._getBoard()[monsterObject._getTileID()]._setNextContent(GameConfigs.EMPTY)
				self._map._getBoard()[monsterObject._getTileID()]._setWalkable(True)
				monsterObject._setX(monsterObject._getX()+1)

				idx = monsterObject._getY() * GameConfigs.BOARD_SIZE + monsterObject._getX()
				if self._map._getBoard()[idx]._getContent() == "P1":
					self._player1._decreaseLives()
					self._player1._resetInvulnerablePulse()

					self._map._getBoard()[self._startIdx]._setContent("P1")
					self._player1._setTileID(self._startIdx)
				if self._map._getBoard()[idx]._getContent() == GameConfigs.EXIT:
					self._map._getBoard()[idx]._setNextContent(GameConfigs.EXIT)

				self._map._getBoard()[idx]._setContent(monsterObject._getTypeID())
				#self._map._getBoard()[idx]._setWalkable(False)
				monsterObject._setTileID(idx)
		elif move =="up":
			if self._map._canMoveUp(monsterObject._getX(),monsterObject._getY()) :
				self._map._getBoard()[monsterObject._getTileID()]._setContent(self._map._getBoard()[monsterObject._getTileID()]._getNextContent())
				self._map._getBoard()[monsterObject._getTileID()]._setNextContent(GameConfigs.EMPTY)
				self._map._getBoard()[monsterObject._getTileID()]._setWalkable(True)
				monsterObject._setY(monsterObject._getY()-1)

				idx = monsterObject._getY() * GameConfigs.BOARD_SIZE + monsterObject._getX()
				if self._map._getBoard()[idx]._getContent() == "P1":
					self._player1._decreaseLives()
					self._player1._resetInvulnerablePulse()

					self._map._getBoard()[self._startIdx]._setContent("P1")
					self._player1._setTileID(self._startIdx)
				if self._map._getBoard()[idx]._getContent() == GameConfigs.EXIT:
					self._map._getBoard()[idx]._setNextContent(GameConfigs.EXIT)

				self._map._getBoard()[idx]._setContent(monsterObject._getTypeID())
				#self._map._getBoard()[idx]._setWalkable(False)
				monsterObject._setTileID(idx)
		else:
			if self._map._canMoveDown(monsterObject._getX(),monsterObject._getY()) :
				self._map._getBoard()[monsterObject._getTileID()]._setContent(self._map._getBoard()[monsterObject._getTileID()]._getNextContent())
				self._map._getBoard()[monsterObject._getTileID()]._setNextContent(GameConfigs.EMPTY)
				self._map._getBoard()[monsterObject._getTileID()]._setWalkable(True)
				monsterObject._setY(monsterObject._getY()+1)

				idx = monsterObject._getY() * GameConfigs.BOARD_SIZE + monsterObject._getX()
				if self._map._getBoard()[idx]._getContent() == "P1":
					self._player1._decreaseLives()
					self._player1._resetInvulnerablePulse()
					self._map._getBoard()[self._startIdx]._setContent("P1")
					self._player1._setTileID(self._startIdx)
				if self._map._getBoard()[idx]._getContent() == GameConfigs.EXIT:
					self._map._getBoard()[idx]._setNextContent(GameConfigs.EXIT)

				self._map._getBoard()[idx]._setContent(monsterObject._getTypeID())
				#self._map._getBoard()[idx]._setWalkable(False)
				monsterObject._setTileID(idx)		
	#Dumb AI
	def _monsterMove(self,monsterObject):
		if not monsterObject._isDead() and monsterObject._canMove():
			move = monsterObject._Moving()
			monsterObject._resetMovePulse()
			self._monsterAction(move,monsterObject)

		#Slighly smarter AI
	def _monsterMove2(self,monsterObject):
		if not monsterObject._isDead() and monsterObject._canMove():
			possibleDirection = []
			if self._map._canMoveLeft(monsterObject._getX(),monsterObject._getY()):
				possibleDirection.append("left")
			if self._map._canMoveRight(monsterObject._getX(),monsterObject._getY()):
				possibleDirection.append("right")
			if self._map._canMoveUp(monsterObject._getX(),monsterObject._getY()):
				possibleDirection.append("up")
			if self._map._canMoveDown(monsterObject._getX(),monsterObject._getY()):
				possibleDirection.append("down")

			if len(possibleDirection)>0:
				monsterObject._resetMovePulse()
				move = possibleDirection[int(random.randrange(0,len(possibleDirection)))]
				self._monsterAction(move,monsterObject)



	def _listen(self):

		#Event queue loop
		for m in range (len(self._monsters)):

			self._monsterMove2(self._monsters[m])
		for event in pygame.event.get():

			#Quit event
			if event.type == QUIT:
				pygame.quit()
				sys.exit()

			#Key events
			if event.type == KEYDOWN:
				if event.key == K_p:

					self._substate = SubstateConfigs.SUBSTATE_INMENU
					break
				if event.key == K_DOWN:

					if self._map._canMoveDown(self._player1._getX(),self._player1._getY()):

						self._player1._goDown()
						if self._map._getBoard()[self._player1._getTileID()]._getContent() == GameConfigs.BOMB:
							self._map._getBoard()[self._player1._getTileID()]._setNextContent(GameConfigs.EMPTY)
						idx = self._player1._getY() * GameConfigs.BOARD_SIZE + self._player1._getX()
						self._player1Move(idx, 0, 1,self._player1)
					break
				if event.key == K_UP:



					if self._map._canMoveUp(self._player1._getX(),self._player1._getY()):

						self._player1._goUp()
						if self._map._getBoard()[self._player1._getTileID()]._getContent() == GameConfigs.BOMB:
							self._map._getBoard()[self._player1._getTileID()]._setNextContent(GameConfigs.EMPTY)
						idx = self._player1._getY() * GameConfigs.BOARD_SIZE + self._player1._getX()
						self._player1Move(idx, 0, -1,self._player1)


					break
				if event.key == K_RIGHT:

					if self._map._canMoveRight(self._player1._getX(),self._player1._getY()):

						self._player1._goRight()
						if self._map._getBoard()[self._player1._getTileID()]._getContent() == GameConfigs.BOMB:
							self._map._getBoard()[self._player1._getTileID()]._setNextContent(GameConfigs.EMPTY)
						idx = self._player1._getY() * GameConfigs.BOARD_SIZE + self._player1._getX()
						self._player1Move(idx, 1, 0,self._player1)

					break
				if event.key == K_LEFT:

					if self._map._canMoveLeft(self._player1._getX(),self._player1._getY()):

						self._player1._goLeft()
						if self._map._getBoard()[self._player1._getTileID()]._getContent() == GameConfigs.BOMB:
							self._map._getBoard()[self._player1._getTileID()]._setNextContent(GameConfigs.EMPTY)
						idx = self._player1._getY() * GameConfigs.BOARD_SIZE + self._player1._getX()
						self._player1Move(idx, -1, 0,self._player1)
					break

				if event.key == K_SPACE:
					if self._map._canPlaceBomb(self._player1._getX(),self._player1._getY()) and (self._player1._isDeadGameOver()==False):
						if self._player1._canPlaceBomb():

							self._player1._increaseBombPlaced()
							idx = self._player1._getY() * GameConfigs.BOARD_SIZE + self._player1._getX()
							self._map._getBoard()[idx]._setContent(GameConfigs.BOMB)
							self._map._getBoard()[idx]._setNextContent("P1")
							b = Bomb(idx,self._player1._getID(), 80,self._player1._getBombRange())##
							self._map._getBoard()[idx]._setWalkable(False)
							self._map._addBomb(b)


	""" redner all frames"""
	def _render(self):

		#ALL BLITS MUST BE IN HERE
		self._screen.blit(self._background, (0, 0))
		self._screen.blit(self._ground_image, (0,0))


		self._screen.blit(self._playerName, ((GameConfigs.BOARD_SIZE)*GameConfigs.TILE_RESOLUTION+25, 10))
		self._screen.blit(self._playerStats, ((GameConfigs.BOARD_SIZE)*GameConfigs.TILE_RESOLUTION+25, 35))
		self._screen.blit(self._playerOStats, ((GameConfigs.BOARD_SIZE)*GameConfigs.TILE_RESOLUTION+25, GameConfigs.TILE_RESOLUTION*4+30))
		
		#Blits for the board



		for idx in range(GameConfigs.BOARD_SIZE*GameConfigs.BOARD_SIZE):
			cont  = self._map._getBoard()[idx]._getContent()
			cont2 = self._map._getBoard()[idx]._getNextContent()
			x = (idx%GameConfigs.BOARD_SIZE)*GameConfigs.TILE_RESOLUTION
			y = (idx/GameConfigs.BOARD_SIZE)*GameConfigs.TILE_RESOLUTION
			if cont == GameConfigs.EMPTY_CRATE or (cont == GameConfigs.BONUS1 and not self._map._getBoard()[idx]._isWalkable())or (cont == GameConfigs.BONUS0 and not self._map._getBoard()[idx]._isWalkable()) or (cont == GameConfigs.BONUS2 and not self._map._getBoard()[idx]._isWalkable()):
				self._screen.blit(self._crate_image, (x,y))
			if cont ==GameConfigs.WALL :
				self._screen.blit(self._wall_image, (x,y))
			if cont == "P1":
				if self._player1._getState() =="D1":
					self._screen.blit(self._p1d1_image, (x,y))				
				if self._player1._getState() =="D2":
					self._screen.blit(self._p1d2_image, (x,y))
				if self._player1._getState() =="U1":
					self._screen.blit(self._p1u1_image, (x,y))
				if self._player1._getState() =="U2":
					self._screen.blit(self._p1u2_image, (x,y))
				if self._player1._getState() =="L1":
					self._screen.blit(self._p1l1_image, (x,y))
				if self._player1._getState() =="L2":
					self._screen.blit(self._p1l2_image, (x,y))
				if self._player1._getState() =="R1":
					self._screen.blit(self._p1r1_image, (x,y))
				if self._player1._getState() =="R2":
					self._screen.blit(self._p1r2_image, (x,y))

			if cont ==  GameConfigs.BOMB:
				self._screen.blit(self._bomb_image, (x,y))
				if cont2 == "P1":
					if self._player1._getState() =="D1":
						self._screen.blit(self._p1d1_image, (x,y))				
					if self._player1._getState() =="D2":
						self._screen.blit(self._p1d2_image, (x,y))
					if self._player1._getState() =="U1":
						self._screen.blit(self._p1u1_image, (x,y))
					if self._player1._getState() =="U2":
						self._screen.blit(self._p1u2_image, (x,y))
					if self._player1._getState() =="L1":
						self._screen.blit(self._p1l1_image, (x,y))
					if self._player1._getState() =="L2":
						self._screen.blit(self._p1l2_image, (x,y))
					if self._player1._getState() =="R1":
						self._screen.blit(self._p1r1_image, (x,y))
					if self._player1._getState() =="R2":
						self._screen.blit(self._p1r2_image, (x,y))

			if cont == GameConfigs.BONUS0 and self._map._getBoard()[idx]._isWalkable():
				self._screen.blit(self._bonus0_image, (x,y))
			if cont == GameConfigs.BONUS1 and self._map._getBoard()[idx]._isWalkable():
				self._screen.blit(self._bonus1_image, (x,y))
			if cont == GameConfigs.BONUS2 and self._map._getBoard()[idx]._isWalkable():
				self._screen.blit(self._bonus2_image, (x,y))

			if cont == GameConfigs.EXIT:
				self._screen.blit(self._exit_image, (x,y))
			if cont == GameConfigs.MONSTER0 or cont == GameConfigs.MONSTER1:
				if cont2 == GameConfigs.EXIT:
					self._screen.blit(self._exit_image, (x,y))
				self._screen.blit(self._monster_image, (x,y))

			if cont == GameConfigs.MONSTER2:
				if cont2 == GameConfigs.EXIT:
					self._screen.blit(self._exit_image, (x,y))
				self._screen.blit(self._monster1_image, (x,y))

			if cont == GameConfigs.MONSTER3:
				if cont2 == GameConfigs.EXIT:
					self._screen.blit(self._exit_image, (x,y))
				self._screen.blit(self._monster2_image, (x,y))



		for b_idx in range(len(self._map._getBombList())):


			if self._map._getBombList()[b_idx]._explosion():



				t_idx = self._map._getBombList()[b_idx]._getTileID()
				x = (t_idx%GameConfigs.BOARD_SIZE)*GameConfigs.TILE_RESOLUTION
				y = (t_idx/GameConfigs.BOARD_SIZE)*GameConfigs.TILE_RESOLUTION

				if(self._map._getBombList()[b_idx]._doneExplosion()== False):
					overallNexstate = self._map._getNextStates2(x/GameConfigs.TILE_RESOLUTION,y/GameConfigs.TILE_RESOLUTION,self._map._getBombList()[b_idx]._getRange(),self._map._getBoard() )
					states = overallNexstate[0]
					statesIdx = overallNexstate[1]

					bomb_tileID = self._map._getBombList()[b_idx]._getTileID()
					player1_tileID = self._player1._getTileID()


					if self._player1._isVulnerable()  and((self._player1._getTileID() in statesIdx) or (self._map._getBoard()[(self._map._getBombList()[b_idx]._getTileID())]._getNextContent()=="P1")):
						self._player1._decreaseLives()
						self._player1._resetInvulnerablePulse()
						self._map._getBoard()[self._player1._getTileID()]._setContent(GameConfigs.EMPTY)
						self._map._getBoard()[self._startIdx]._setContent("P1")
						self._player1._setTileID(self._startIdx)
					for m in range(len(self._monsters)):
						if  self._monsters[m]._getTileID() in statesIdx:
							#self._map._getBoard()[self._monsters[m]._getTileID()]._setContent(GameConfigs.EMPTY)
							#self._map._getBoard()[self._monsters[m]._getTileID()]._setWalkable(True)
							if self._map._getBombList()[b_idx]._getOwner() == self._player1._getID() and (not self._monsters[m]._isDead() ):
									self._player1._addToKills()
									self._highScoreDB.addNumKillsFor(self._player.username,1)
							self._monsters[m]._decreaseLives()

					# Enter explosion code here

					self._map._getBoard()[t_idx]._setWalkable(True)
					self._map._getBoard()[t_idx]._setContent(GameConfigs.EMPTY)	

					if self._map._getBombList()[b_idx]._getTick() > 35:
						self._screen.blit(self._expc1_image, (x,y))	
					elif self._map._getBombList()[b_idx]._getTick() > 25:
						self._screen.blit(self._expc2_image, (x,y))	
					elif self._map._getBombList()[b_idx]._getTick() > 15:
						self._screen.blit(self._expc3_image, (x,y))	
					else:
						self._screen.blit(self._expc4_image, (x,y))	



					left_index = 0
					right_index = 0
					down_index = 0
					up_index = 0

					for std_idx in range(len(states)):
						if states[std_idx] == "right":
							right_index = std_idx
						if states[std_idx] == "down":
							down_index = std_idx
						if states[std_idx] == "up":
							up_index = std_idx

					left = states[left_index:right_index]
					left_Idx = statesIdx[left_index:right_index]

					right = states[right_index:down_index]
					right_Idx = statesIdx[right_index:down_index]

					down = states[down_index:up_index]
					down_Idx = statesIdx[down_index:up_index]

					up = states[up_index:]
					up_Idx = statesIdx[up_index:]

					for st_idx in range(len(left)):
						if left[st_idx]!=GameConfigs.WALL and left[st_idx]!="left":
							x_left = (left_Idx[st_idx]%GameConfigs.BOARD_SIZE)*GameConfigs.TILE_RESOLUTION
							y_left = (left_Idx[st_idx]/GameConfigs.BOARD_SIZE)*GameConfigs.TILE_RESOLUTION
							if st_idx !=(len(left)-1):

								if self._map._getBombList()[b_idx]._getTick() > 35:
									self._screen.blit(self._explm1_image, (x_left,y_left))	
								elif self._map._getBombList()[b_idx]._getTick() > 25:
									self._screen.blit(self._explm2_image, (x_left,y_left))	
								elif self._map._getBombList()[b_idx]._getTick() > 15:
									self._screen.blit(self._explm3_image, (x_left,y_left))	
								else:
									self._screen.blit(self._explm4_image, (x_left,y_left))
							else:
								if self._map._getBombList()[b_idx]._getTick() > 35:
									self._screen.blit(self._expll1_image, (x_left,y_left))	
								elif self._map._getBombList()[b_idx]._getTick() > 25:
									self._screen.blit(self._expll2_image, (x_left,y_left))	
								elif self._map._getBombList()[b_idx]._getTick() > 15:
									self._screen.blit(self._expll3_image, (x_left,y_left))	
								else:
									self._screen.blit(self._expll4_image, (x_left,y_left))



					for st_idx in range(len(right)):
						if right[st_idx]!=GameConfigs.WALL and right[st_idx]!="right":
							x_right = (right_Idx[st_idx]%GameConfigs.BOARD_SIZE)*GameConfigs.TILE_RESOLUTION
							y_right = (right_Idx[st_idx]/GameConfigs.BOARD_SIZE)*GameConfigs.TILE_RESOLUTION
							if st_idx !=(len(right)-1):

								if self._map._getBombList()[b_idx]._getTick() > 35:
									self._screen.blit(self._exprm1_image, (x_right,y_right))	
								elif self._map._getBombList()[b_idx]._getTick() > 25:
									self._screen.blit(self._exprm2_image, (x_right,y_right))	
								elif self._map._getBombList()[b_idx]._getTick() > 15:
									self._screen.blit(self._exprm3_image, (x_right,y_right))	
								else:
									self._screen.blit(self._exprm4_image, (x_right,y_right))
							else:
								if self._map._getBombList()[b_idx]._getTick() > 35:
									self._screen.blit(self._exprr1_image, (x_right,y_right))	
								elif self._map._getBombList()[b_idx]._getTick() > 25:
									self._screen.blit(self._exprr2_image, (x_right,y_right))	
								elif self._map._getBombList()[b_idx]._getTick() > 15:
									self._screen.blit(self._exprr3_image, (x_right,y_right))	
								else:
									self._screen.blit(self._exprr4_image, (x_right,y_right))






					for st_idx in range(len(down)):
						if down[st_idx]!=GameConfigs.WALL and down[st_idx]!="down":
							x_down = (down_Idx[st_idx]%GameConfigs.BOARD_SIZE)*GameConfigs.TILE_RESOLUTION
							y_down = (down_Idx[st_idx]/GameConfigs.BOARD_SIZE)*GameConfigs.TILE_RESOLUTION
							if st_idx !=(len(down)-1):

								if self._map._getBombList()[b_idx]._getTick() > 35:
									self._screen.blit(self._expdm1_image, (x_down,y_down))	
								elif self._map._getBombList()[b_idx]._getTick() > 25:
									self._screen.blit(self._expdm2_image, (x_down,y_down))	
								elif self._map._getBombList()[b_idx]._getTick() > 15:
									self._screen.blit(self._expdm3_image, (x_down,y_down))	
								else:
									self._screen.blit(self._expdm4_image, (x_down,y_down))
							else:
								if self._map._getBombList()[b_idx]._getTick() > 35:
									self._screen.blit(self._expdd1_image, (x_down,y_down))	
								elif self._map._getBombList()[b_idx]._getTick() > 25:
									self._screen.blit(self._expdd2_image, (x_down,y_down))	
								elif self._map._getBombList()[b_idx]._getTick() > 15:
									self._screen.blit(self._expdd3_image, (x_down,y_down))	
								else:
									self._screen.blit(self._expdd4_image, (x_down,y_down))



					for st_idx in range(len(up)):
						if up[st_idx]!=GameConfigs.WALL and up[st_idx]!="up":
							x_up = (up_Idx[st_idx]%GameConfigs.BOARD_SIZE)*GameConfigs.TILE_RESOLUTION
							y_up = (up_Idx[st_idx]/GameConfigs.BOARD_SIZE)*GameConfigs.TILE_RESOLUTION
							if st_idx !=(len(up)-1):

								if self._map._getBombList()[b_idx]._getTick() > 35:
									self._screen.blit(self._expum1_image, (x_up,y_up))	
								elif self._map._getBombList()[b_idx]._getTick() > 25:
									self._screen.blit(self._expum2_image, (x_up,y_up))	
								elif self._map._getBombList()[b_idx]._getTick() > 15:
									self._screen.blit(self._expum3_image, (x_up,y_up))	
								else:
									self._screen.blit(self._expum4_image, (x_up,y_up))
							else:
								if self._map._getBombList()[b_idx]._getTick() > 35:
									self._screen.blit(self._expuu1_image, (x_up,y_up))	
								elif self._map._getBombList()[b_idx]._getTick() > 25:
									self._screen.blit(self._expuu2_image, (x_up,y_up))	
								elif self._map._getBombList()[b_idx]._getTick() > 15:
									self._screen.blit(self._expuu3_image, (x_up,y_up))	
								else:
									self._screen.blit(self._expuu4_image, (x_up,y_up))






		level = self._fontt.render("Level: "+str(self._level), True, OtherConfigs.COLOR_BLACK)
		timer = self._fontt.render("Time Left: " +str(self._Timer), True, OtherConfigs.COLOR_BLACK)


		self._screen.blit(level, ((GameConfigs.BOARD_SIZE)*GameConfigs.TILE_RESOLUTION+20,GameConfigs.TILE_RESOLUTION*2+10))
		nbKills = self._fontt.render("#Kills: "+str(self._player1._getNbKills()), True, OtherConfigs.COLOR_BLACK)
		self._screen.blit(nbKills, ((GameConfigs.BOARD_SIZE)*GameConfigs.TILE_RESOLUTION+20,GameConfigs.TILE_RESOLUTION*3-5))
		nbDeath = self._fontt.render("#Death: "+str(self._player1._getNbDeath()), True, OtherConfigs.COLOR_BLACK)
		self._screen.blit(nbDeath, ((GameConfigs.BOARD_SIZE)*GameConfigs.TILE_RESOLUTION+20,GameConfigs.TILE_RESOLUTION*3+20))


		nbLevelCompleted = self._fontt.render("#Levels Cleared: "+str(self._highScoreDB.getLevelsCompletedOf(self._player.username)), True, OtherConfigs.COLOR_BLACK)
		self._screen.blit(nbLevelCompleted, ((GameConfigs.BOARD_SIZE)*GameConfigs.TILE_RESOLUTION+20,GameConfigs.TILE_RESOLUTION*5+25))

		maxLevel = self._fontt.render("Best Level: "+str(self._highScoreDB.getMaxLevelAchievedOf(self._player.username)), True, OtherConfigs.COLOR_BLACK)
		self._screen.blit(maxLevel, ((GameConfigs.BOARD_SIZE)*GameConfigs.TILE_RESOLUTION+20,GameConfigs.TILE_RESOLUTION*6+10))

		overallKills = self._fontt.render("#Kills: "+str(self._highScoreDB.getNumKillsOf(self._player.username)), True, OtherConfigs.COLOR_BLACK)
		self._screen.blit(overallKills, ((GameConfigs.BOARD_SIZE)*GameConfigs.TILE_RESOLUTION+20,GameConfigs.TILE_RESOLUTION*6+35))

		overallKDR = self._fontt.render("KDR: "+str(self._highScoreDB.getKDROf(self._player.username)), True, OtherConfigs.COLOR_BLACK)
		self._screen.blit(overallKDR, ((GameConfigs.BOARD_SIZE)*GameConfigs.TILE_RESOLUTION+20,GameConfigs.TILE_RESOLUTION*7+20))


		self._screen.blit(timer, (10, 580))
		# Display thre amount of lives left

		# for player 1

		for p1_index in range(self._player1._getLives()):
			self._screen.blit(self._lives_image, (750-p1_index*GameConfigs.TILE_RESOLUTION,GameConfigs.TILE_RESOLUTION+13))	

		# remove from bomb list
		bombToRemove = []				
		for b_idx in range(len(self._map._getBombList())):
			if(self._map._getBombList()[b_idx]._doneExplosion()== True):
				bombToRemove.append(self._map._getBombList()[b_idx])
				t_idx = self._map._getBombList()[b_idx]._getTileID()
				x = (t_idx%GameConfigs.BOARD_SIZE)*GameConfigs.TILE_RESOLUTION
				y = (t_idx/GameConfigs.BOARD_SIZE)*GameConfigs.TILE_RESOLUTION
				overallNexstate = self._map._getNextStates2(x/GameConfigs.TILE_RESOLUTION,y/GameConfigs.TILE_RESOLUTION,self._map._getBombList()[b_idx]._getRange(),self._map._getBoard() )
				states = overallNexstate[0]
				statesIdx = overallNexstate[1]
				for s_idx in range(len(states)):
					if(states[s_idx]!="left"and states[s_idx]!="right" and states[s_idx]!="down" and states[s_idx]!="up"):
						if self._map._getBoard()[statesIdx[s_idx]]._getContent()== GameConfigs.EMPTY_CRATE:
							self._map._getBoard()[statesIdx[s_idx]]._setContent(GameConfigs.EMPTY)
							self._map._getBoard()[statesIdx[s_idx]]._setWalkable(True)
						elif states[s_idx] == GameConfigs.BONUS0 or  states[s_idx] == GameConfigs.BONUS1 or  states[s_idx] == GameConfigs.BONUS2:
							self._map._getBoard()[statesIdx[s_idx]]._setWalkable(True)
						for m in range(len(self._monsters)):
							if  self._monsters[m]._getTileID() in statesIdx:
								self._map._getBoard()[self._monsters[m]._getTileID()]._setContent(self._map._getBoard()[self._monsters[m]._getTileID()]._getNextContent())
								self._map._getBoard()[self._monsters[m]._getTileID()]._setNextContent(GameConfigs.EMPTY)
								self._map._getBoard()[self._monsters[m]._getTileID()]._setWalkable(True)

		for br_idx in range(len(bombToRemove)):
			if bombToRemove[br_idx]._getOwner() == self._player1._getID():
				self._player1._decreaseBombPlaced(); 
			self._map._removeBomb(bombToRemove[br_idx])

		del(bombToRemove)

		if self._player1._getTileID() == self._startIdx:
			x = (self._player1._getTileID()%GameConfigs.BOARD_SIZE)*GameConfigs.TILE_RESOLUTION
			y = (self._player1._getTileID()/GameConfigs.BOARD_SIZE)*GameConfigs.TILE_RESOLUTION
			if self._player1._getState() =="D1":
				self._screen.blit(self._p1d1_image, (x,y))				
			if self._player1._getState() =="D2":
				self._screen.blit(self._p1d2_image, (x,y))
			if self._player1._getState() =="U1":
				self._screen.blit(self._p1u1_image, (x,y))
			if self._player1._getState() =="U2":
				self._screen.blit(self._p1u2_image, (x,y))
			if self._player1._getState() =="L1":
				self._screen.blit(self._p1l1_image, (x,y))
			if self._player1._getState() =="L2":
				self._screen.blit(self._p1l2_image, (x,y))
			if self._player1._getState() =="R1":
				self._screen.blit(self._p1r1_image, (x,y))
			if self._player1._getState() =="R2":
				self._screen.blit(self._p1r2_image, (x,y))



