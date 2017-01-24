import pygame

class Plane():
	def __init__(self,ol_settings,screen):
		"""Initialise the plane ans set its starting position."""
		self.screen=screen
		self.ol_settings=ol_settings
		#load the plane image
		self.image=pygame.image.load('images/plane.bmp')
		self.rect=self.image.get_rect()  #Pygame treats evry elem as rectangles
		self.screen_rect=screen.get_rect() 
		#start each new plane at the bottom center of the screen.
		self.rect.centerx=self.screen_rect.centerx
		self.rect.bottom=self.screen_rect.bottom
		#Store a decimal value for the plane's center.
		self.centerx=float(self.rect.centerx)
		self.centery=float(self.rect.centery)
		#MOvement flag
		self.moving_right=False
		self.moving_left=False
		self.moving_up=False
		self.moving_down=False

	def update(self):
		"""Update the plane's position based on movement flag"""
		#Update the plane center value not rect ---why?@mD
		#Movement due to gravity pull of the Earth.
		if self.rect.centery<self.screen_rect.bottom:
			self.centery+=self.ol_settings.gravity_factor
			#print self.rect.centerx, self.rect.centery, self.center
		#Movement due to keydown
		if self.moving_right and self.rect.right<self.screen_rect.right:
			self.centerx+=self.ol_settings.ship_speed_factor
		if self.moving_left and self.rect.left>self.screen_rect.left:
			self.centerx-=self.ol_settings.ship_speed_factor
		if self.moving_up and self.rect.top>0:
			self.centery-=self.ol_settings.ship_speed_factor
		if self.moving_down and self.rect.bottom<self.screen_rect.bottom:
			self.centery+=self.ol_settings.ship_speed_factor
		#Update rect object from self.center.
		self.rect.centerx=self.centerx
		self.rect.centery=self.centery

	def blitme(self):
		"""Draw the plane at its current locattion"""
		self.screen.blit(self.image,self.rect) #blit draws arg1 at arg2 pos


