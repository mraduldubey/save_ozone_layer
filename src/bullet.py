import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	"""A class to manage Bullet pellets fired from ship"""
	def __init__(self,ol_settings,screen,ship):
		"""Create a bullet object at the ship's curent position"""
		super(Bullet,self).__init__()
		self.screen=screen

		#Create a bullet rect at (0,0) and then set correct position
		self.rect=pygame.Rect(0,0,ol_settings.bullet_width,ol_settings.bullet_height)
		self.rect.centerx=ship.rect.centerx
		self.rect.top=ship.rect.top

		#Store the bullet position as a decimal value
		self.y=float(self.rect.y) #soas to have better control over its movement.

		self.color=ol_settings.bullet_color
		self.speed_factor=ol_settings.bullet_speed_factor
	
	def update(self):
		"""MOve the bullet up the screen"""
		#Update the decimal position of the bullet.
		self.y -= self.speed_factor
		#Update the rect positon.
		self.rect.y=self.y

	def draw_bullet(self):
		"""Draw the bullet to the screen """
		pygame.draw.rect(self.screen,self.color,self.rect)
