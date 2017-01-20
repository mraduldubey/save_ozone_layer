import pygame

class Earth():
	def __init__(self,ai_settings,screen):
		self.screen=screen
		self.ai_settings=ai_settings
		#load the earth pic
		self.image=pygame.image.load('images/earth.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect=screen.get_rect()
		#start with earth at the bottom center of the screen.
		self.rect.centerx=self.screen_rect.centerx
		self.rect.bottom=self.screen_rect.bottom

	def blitme(self):
		"""Draw the earth at current location"""
		self.screen.blit(self.image,self.rect)