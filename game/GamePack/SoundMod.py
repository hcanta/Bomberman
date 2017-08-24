#Imports
import pygame, sys, math
from pygame.locals import*


#Play Game Sound and Music
"""
		This class allows the game to play the music on the background and also it includes 
		the sound effect of explosion, death and power up. All the sound files can be found 
		in the the Sounds folder. (C:Documents\GitHub\ team2\game\Sounds) We also chose 2 
		instrumental songs for this game. They are Gangnam Style by Psy and Baby by Justin Bieber.
"""

class Sound():

	musicPlaying=False
	"""
		Class Constructor for the sound class. This method creates the instance 
		of the object itself.
	"""

	def __init__(self):

		self.music_path='Sounds/leveltheme.ogg'
		self.music_path2='Sounds/baby.ogg'
		self.sound1 = pygame.mixer.Sound('Sounds/gangnam.ogg')
		self.sound2 = pygame.mixer.Sound('Sounds/baby.ogg')
		self.chan1 = pygame.mixer.find_channel()
		self.chan2 = pygame.mixer.find_channel()
		#Initialize mixer
		pygame.mixer.init()
		
	#Play/Stop music
	"""
		This method define 2 states (play and stop). 
	"""

	def playmusic(self,type):

		
		if type=="Play":
			
			self.chan1.queue(self.sound1)
			self.chan2.queue(self.sound2)

		elif type=="Stop":

			self.chan1.stop()
			self.chan2.stop()

	#Play/Stop sound
	"""
		The method plays the sounds of explosion or power-up 
	"""

	def playsound(self,type):

		if type=="Bomb":

			pygame.mixer.music.load('Sounds/explosion.wav')
			pygame.mixer.music.play(1)
		elif type=="Powerup":
			pygame.mixer.music.load('Sounds/powerup.wav')
			pygame.mixer.music.play(1)
	"""
		This method allows to play the sound
	"""

	def playSound(self):
		pygame.mixer.music.load()
