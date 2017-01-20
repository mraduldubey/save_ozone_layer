import pygame
from pygame.sprite import Sprite 

class Alien(Sprite):
	"""A class to represent a single alien in the fleet"""

	def __init__(self,ai_settings,screen):
		"""Initalise the alien and set its starting positon"""
		super(Alien,self).__init__()
		self.screen=screen
		self.ai_settings=ai_settings

		#Load the alien image and set its rect attribute.
		self.image=pygame.image.load('images/alien.bmp')
		self.rect=self.image.get_rect()

		#Start the alien's near top left for now
		#Apply random function here later.
		self.rect.x=self.rect.width
		self.rect.y=self.rect.height

		#Store exact location of alien
		self.x=float(self.rect.x)

	def blitme(self):
		"""Draw the alien at its current location."""
		self.screen.blit(self.image,self.rect)
