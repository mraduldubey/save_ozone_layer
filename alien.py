import pygame
from pygame.sprite import Sprite 

class Alien(Sprite):
	"""A class to represent a single alien in the swarm"""

	def __init__(self,ol_settings,screen):
		"""Initalise the alien and set its starting positon"""
		super(Alien,self).__init__()
		self.screen=screen
		self.ol_settings=ol_settings

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

	def update(self):
		"""Move them right"""
		self.x+=(self.ol_settings.alien_speed_factor*self.ol_settings.swarm_direction)
		self.rect.x=self.x

	def check_edges(self):
		"""Return True if alien is at edge of screen"""
		screen_rect=self.screen.get_rect()
		if self.rect.right >= screen_rect.right:
			return True
		elif self.rect.left<=0:
			return True
