import random,sys,os,imghdr,pygame
from ConfigPack.ConfigMod import AppConfigs, GameConfigs, OtherConfigs
from GamePack.BombMod import Bomb
from FileManagementPack.DatabaseMod import MapDatabase
from pygame import*
sys.path.append("..")


from GamePack.TileMod import Tile 
class Map():

	def __init__(self):
		self._board =[]
		for i in range (14*14):
			x = Tile(i, GameConfigs.EMPTY)
			self._board.append(x) 
		self._BombList= []
		self._mapDB =MapDatabase()

	def _getBombList(self):
		return self._BombList

	def _addBomb(self,b):
		self._BombList.append(b)

	def _removeBomb(self, b):
		self._BombList.remove(b)

	#Used in explostion of range 1
	def _geNextTileState(self,x,y):

		#left
		xleft = x-1
		yleft = y

		leftState = GameConfigs.WALL # can't go left
		if xleft != -1 :
			leftState= self._board[yleft * 14 + xleft]._getContent()

		#right
		xRight = x+1
		yRight = y

		rightState = GameConfigs.WALL #Can't go right
		if xRight < 14 :
			rightState= self._board[yRight * 14 + xRight]._getContent()

		#down
		xDown = x
		yDown = y+1

		downState = GameConfigs.WALL #Can't go down
		if yDown < 14 :
			downState= self._board[yDown * 14 + xDown]._getContent()
		
		#UP
		xUp = x
		yUp = y-1

		upState = GameConfigs.WALL #Can't go up
		if yUp != -1 :
			upState= self._board[yUp * 14 + xUp]._getContent()


		return [leftState,upState,rightState,downState]	

#move left?
	def _canMoveLeft(self,x,y):
		canMove = False
		xLeft = x-1
		if xLeft!=-1:
			if self._board[y*14+xLeft]._isWalkable():
				canMove = True
		return canMove

	#move right?
	def _canMoveRight(self,x,y):
		canMove = False
		xRight = x+1
		if xRight!=14:
			if self._board[y*14+xRight]._isWalkable():
				canMove = True
		return canMove

	# Bomb already placed?
	def _canPlaceBomb(self, x,y):
		canPlace = False
		if self._board[y * 14 + x] != GameConfigs.BOMB:  # marker to be changed
				canPlace = True
		return canPlace	

	#move up?
	def _canMoveUp(self,x,y):
		canMove = False
		yUp = y-1
		if yUp!=-1:
			if self._board[yUp*14+x]._isWalkable():
				canMove = True
		return canMove	

	#move down?
	def _canMoveDown(self,x,y):
		canMove = False
		yDown = y+1
		if yDown!=14:
			if self._board[yDown*14+x]._isWalkable():
				canMove = True
		return canMove		


	def _getBoard(self):
		return self._board

	def _levelOne(self):
		__list = self._mapDB.getMapNo(1)
		for idx in range(len(__list)):
			self._board[idx]._setContent(__list[idx])
			if __list[idx] == GameConfigs.EMPTY_CRATE or __list[idx] == GameConfigs.WALL or __list[idx] == GameConfigs.BONUS0 or __list[idx] == GameConfigs.BONUS1 or __list[idx] == GameConfigs.BONUS2  or __list[idx] == "P1":
				self._board[idx]._setWalkable(False)

	def _levelTwo(self):
		__list = self._mapDB.getMapNo(2)
		for idx in range(len(__list)):
			self._board[idx]._setContent(__list[idx])
			if __list[idx] == GameConfigs.EMPTY_CRATE or __list[idx] == GameConfigs.WALL or __list[idx] == GameConfigs.BONUS0 or __list[idx] == GameConfigs.BONUS1 or __list[idx] == GameConfigs.BONUS2  or __list[idx] == "P1":
				self._board[idx]._setWalkable(False)

	def _levelThree(self):
		__list = self._mapDB.getMapNo(3)
		for idx in range(len(__list)):
			self._board[idx]._setContent(__list[idx])
			if __list[idx] == GameConfigs.EMPTY_CRATE or __list[idx] == GameConfigs.WALL or __list[idx] == GameConfigs.BONUS0 or __list[idx] == GameConfigs.BONUS1 or __list[idx] == GameConfigs.BONUS2  or __list[idx] == "P1":
				self._board[idx]._setWalkable(False)

	def _levelFour(self):
		__list = self._mapDB.getMapNo(4)
		for idx in range(len(__list)):
			self._board[idx]._setContent(__list[idx])
			if __list[idx] == GameConfigs.EMPTY_CRATE or __list[idx] == GameConfigs.WALL or __list[idx] == GameConfigs.BONUS0 or __list[idx] == GameConfigs.BONUS1 or __list[idx] == GameConfigs.BONUS2  or __list[idx] == "P1":
				self._board[idx]._setWalkable(False)

	def _levelFive(self):
		__list = self._mapDB.getMapNo(5)
		for idx in range(len(__list)):
			self._board[idx]._setContent(__list[idx])
			if __list[idx] == GameConfigs.EMPTY_CRATE or __list[idx] == GameConfigs.WALL or __list[idx] == GameConfigs.BONUS0 or __list[idx] == GameConfigs.BONUS1 or __list[idx] == GameConfigs.BONUS2  or __list[idx] == "P1":
				self._board[idx]._setWalkable(False)

	def _levelSix(self):
		__list = self._mapDB.getMapNo(6)
		for idx in range(len(__list)):
			self._board[idx]._setContent(__list[idx])
			if __list[idx] == GameConfigs.EMPTY_CRATE or __list[idx] == GameConfigs.WALL or __list[idx] == GameConfigs.BONUS0 or __list[idx] == GameConfigs.BONUS1 or __list[idx] == GameConfigs.BONUS2  or __list[idx] == "P1":
				self._board[idx]._setWalkable(False)

	def _levelSeven(self):
		__list = self._mapDB.getMapNo(7)
		for idx in range(len(__list)):
			self._board[idx]._setContent(__list[idx])
			if __list[idx] == GameConfigs.EMPTY_CRATE or __list[idx] == GameConfigs.WALL or __list[idx] == GameConfigs.BONUS0 or __list[idx] == GameConfigs.BONUS1 or __list[idx] == GameConfigs.BONUS2  or __list[idx] == "P1":
				self._board[idx]._setWalkable(False)

	def _levelEight(self):
		__list = self._mapDB.getMapNo(8)
		for idx in range(len(__list)):
			self._board[idx]._setContent(__list[idx])
			if __list[idx] == GameConfigs.EMPTY_CRATE or __list[idx] == GameConfigs.WALL or __list[idx] == GameConfigs.BONUS0 or __list[idx] == GameConfigs.BONUS1 or __list[idx] == GameConfigs.BONUS2  or __list[idx] == "P1":
				self._board[idx]._setWalkable(False)
	
	def _getMonsters(self):

		monsterType = []
		monsterIdx = []
		for idx in range (GameConfigs.BOARD_SIZE*GameConfigs.BOARD_SIZE):
			if self._board[idx]._getContent() == GameConfigs.MONSTER0 or self._board[idx]._getContent() == GameConfigs.MONSTER1 or self._board[idx]._getContent() == GameConfigs.MONSTER2 or self._board[idx]._getContent() == GameConfigs.MONSTER3:
				monsterType.append(self._board[idx]._getContent())
				monsterIdx.append(idx)
		return [monsterType, monsterIdx]
	def _getStartPosition(self):
		return_idx = -1
		for idx in range (GameConfigs.BOARD_SIZE*GameConfigs.BOARD_SIZE):
			if self._board[idx]._getContent() == "P1":
				return_idx = idx
				break
		return return_idx
		
	def _getExitIdx(self):
		return_idx = -1
		for idx in range (GameConfigs.BOARD_SIZE*GameConfigs.BOARD_SIZE):
			if self._board[idx]._getContent() == GameConfigs.EXIT:
				return_idx = idx
				break
		return return_idx


	def _clear(self):
		del(self._board)
		self._board =[]
		for i in range (14*14):
			x = Tile(i, GameConfigs.EMPTY)
			self._board.append(x) 
	def _random(self):
		size = 14 * 14

		wall = 45

		# Place Randomly undestrructible walls
		for i in range(wall):
			idx = random.choice(range(size))
			while(self._board[idx]._getContent()==GameConfigs.WALL or idx%GameConfigs.BOARD_SIZE == 0 or idx%GameConfigs.BOARD_SIZE == 13):
				idx=random.choice(range(size))
			self._board[idx]._setContent(GameConfigs.WALL)
			self._board[idx]._setWalkable(False)

		# Place Randomly Bonus crates
		for i in range(8):
			idx = random.choice(range(size))
			while(self._board[idx]._getContent()!=GameConfigs.EMPTY or idx%GameConfigs.BOARD_SIZE == 0 or idx%GameConfigs.BOARD_SIZE == 13):
				idx=random.choice(range(size))
			self._board[idx]._setContent(GameConfigs.BONUS0)
			self._board[idx]._setWalkable(False)

		# Place Randomly Bonus crates
		for i in range(9):
			idx = random.choice(range(size))
			while(self._board[idx]._getContent()!=GameConfigs.EMPTY or idx%GameConfigs.BOARD_SIZE == 0 or idx%GameConfigs.BOARD_SIZE == 13):
				idx=random.choice(range(size))
			self._board[idx]._setContent(GameConfigs.BONUS1)
			self._board[idx]._setWalkable(False)

		# Place Randomly Bonus crates
		for i in range(10):
			idx = random.choice(range(size))
			while(self._board[idx]._getContent()!=GameConfigs.EMPTY or idx%GameConfigs.BOARD_SIZE == 0 or idx%GameConfigs.BOARD_SIZE == 13):
				idx=random.choice(range(size))
			self._board[idx]._setContent(GameConfigs.BONUS2)
			self._board[idx]._setWalkable(False)	

		# Place Randomly empty crates
		for i in range(20):
			idx = random.choice(range(size))
			while(self._board[idx]._getContent()!=GameConfigs.EMPTY or idx%GameConfigs.BOARD_SIZE == 0 or idx%GameConfigs.BOARD_SIZE == 13):
				idx=random.choice(range(size))
			self._board[idx]._setContent(GameConfigs.EMPTY_CRATE)
			self._board[idx]._setWalkable(False)
		self._board[0]._setContent("P1")
		self._board[13]._setContent(GameConfigs.MONSTER0)
		self._board[182]._setContent(GameConfigs.MONSTER0)
		self._board[0]._setWalkable(False)
		self._board[GameConfigs.BOARD_SIZE* GameConfigs.BOARD_SIZE-1]._setContent(GameConfigs.EXIT);


	def _setTileContent(self, tileId, content):
		self._board[tileId]._setContent(c)

	def _canMoveOnTile(self,tileId):
		return self._board[tileId]._getWalkable()

	def _setWalkableTile(self, tileId,w):
		self._board[tileId]._setWalkable(w)

	def _getNextStates2(self, x,y, _range,board):

		states = []
		statesIdx =[]
		#left

		states.append("left")
		statesIdx.append(-1)
		for idx in range(_range):
			xleft = x-(idx+1)
			yleft = y

			leftState = GameConfigs.WALL # can't go left
			if xleft >=0 :
				leftState= board[yleft * 14 + xleft]._getContent()
				states.append(leftState)
				statesIdx.append(yleft * 14 + xleft)
				idx2 = (yleft * 14 + xleft)
				if idx2<= ((14*14)-1):
					if board[idx2]._isWalkable() == False:
						break
				else:
					break

		#right
		
		states.append("right")
		statesIdx.append(-1)
		
		for idx in range(_range):
			xright = x+(idx+1)
			yright = y
			rightState = GameConfigs.WALL #Can't go right
			if xright < 14 :
				rightState= self._board[yright * 14 + xright]._getContent()
				states.append(rightState)
				statesIdx.append(yright * 14 + xright)
				idx2 = (yright * 14 + xright)
				if idx2<= ((14*14)-1):
					if board[idx2]._isWalkable() == False:
						break
				else:
					break

		#down
		states.append("down")
		statesIdx.append(-1)
		for idx in range(_range):
			xdown = x
			ydown = y+(idx+1)

			downState = GameConfigs.WALL #Can't go down
			if ydown < 14 :
				downState= self._board[ydown * 14 + xdown]._getContent()
				states.append(downState)
				statesIdx.append(ydown * 14 + xdown)
				idx2 = (ydown * 14 + xdown)
				if idx2<= ((14*14)-1):
					if board[idx2]._isWalkable() == False:
						break
				else:
					break
			
				
			
		#UP
		states.append("up")
		statesIdx.append(-1)
		for idx in range(_range):
			xup = x
			yup = y-(idx +1)

			upState = GameConfigs.WALL #Can't go up
			if yup >=0 :
				upState= self._board[yup * 14 + xup]._getContent()
				states.append(upState)
				statesIdx.append(yup * 14 + xup)
				idx2 = (yup * 14 + xup)
				if idx2<= ((14*14)-1):
					if board[idx2]._isWalkable() == False:
						break
				else:
					break
				


		return [states,statesIdx]	



