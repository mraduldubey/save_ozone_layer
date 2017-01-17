import pygame

class Ship():
	def __init__(self,screen):
		"""Initialise the ship ans set its starting position."""
		self.screen=screen

		#load the ship image
		self.image=pygame.image.load('images/ship.bmp')
		self.rect=self.image.get_rect()  #Pygame treats evry elem as rectangles
		self.screen_rect=screen.get_rect() 
		#start each new ship at the bottom center of the screen.
		self.rect.centerx=self.screen_rect.centerx
		self.rect.bottom=self.screen_rect.bottom

	def blitme(self):
		"""Draw the ship at its current locattion"""
		self.screen.blit(self.image,self.rect) #blit draws arg1 at arg2 pos


