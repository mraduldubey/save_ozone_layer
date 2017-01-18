import pygame

class Ship():
	def __init__(self,ai_settings,screen):
		"""Initialise the ship ans set its starting position."""
		self.screen=screen
		self.ai_settings=ai_settings
		#load the ship image
		self.image=pygame.image.load('images/ship.bmp')
		self.rect=self.image.get_rect()  #Pygame treats evry elem as rectangles
		self.screen_rect=screen.get_rect() 
		#start each new ship at the bottom center of the screen.
		self.rect.centerx=self.screen_rect.centerx
		self.rect.bottom=self.screen_rect.bottom
		#Store a decimal value for the ship's center.
		self.center=float(self.rect.centerx)
		#MOvement flag
		self.moving_right=False
		self.moving_left=False

	def update(self):
		"""Update the ship's position based on movement flag"""
		#Update the ship center value not rect
		if self.moving_right and self.rect.right<self.screen_rect.right:
			self.center+=self.ai_settings.ship_speed_factor
		if self.moving_left and self.rect.left>self.screen_rect.left:
			self.center-=self.ai_settings.ship_speed_factor
		#Update rect object from self.center.
		self.rect.centerx=self.center

	def blitme(self):
		"""Draw the ship at its current locattion"""
		self.screen.blit(self.image,self.rect) #blit draws arg1 at arg2 pos


