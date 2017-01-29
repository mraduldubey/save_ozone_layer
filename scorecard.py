import pygame.font
from pygame.sprite import Group
from plane import Plane

class ScoreCard():
	"""A class to report scoring information"""
	def __init__(self,ol_settings,screen,stats):
		"""Scoreboard atttributes"""
		self.screen=screen
		self.screen_rect =screen.get_rect()
		self.ol_settings=ol_settings
		self.stats=stats

		#Font settings
		self.text_color=(30,30,30)
		self.font=pygame.font.SysFont(None,48)

		#prepare the initial score image.
		self.prep_score()
		self.prep_high_score()
		self.prep_level()
		self.prep_planes()

	def prep_score(self):
		"""Render the scoreboard"""
		score_str="{:,}".format(self.stats.score)
		self.score_image=self.font.render(score_str,True,self.text_color,self.ol_settings.bg_color)
		#Display the scoreboard at top right of the screen
		self.score_rect=self.score_image.get_rect()
		self.score_rect.right=self.screen_rect.right-20
		self.score_rect.top=20


	def prep_high_score(self):
		"""Turn the high score into a rendered image"""
		high_score=int(round(self.stats.high_score,-1))
		high_score_str="{:,}".format(high_score)
		self.high_score_image=self.font.render(high_score_str,True,self.text_color,self.ol_settings.bg_color)

		#Center high score at the top.
		self.high_score_rect = self.high_score_image.get_rect()
		self.high_score_rect.centerx = self.screen_rect.centerx
		self.high_score_rect.top = self.score_rect.top

	def show_score(self):
		"""Draw score to the screen"""
		self.screen.blit(self.score_image,self.score_rect)
		self.screen.blit(self.high_score_image,self.high_score_rect)
		self.screen.blit(self.level_image,self.level_rect)
		self.planes.draw(self.screen)

	def prep_level(self):
		"""Render the levelbar"""
		self.level_image=self.font.render(str(self.stats.level),True,self.text_color,self.ol_settings.bg_color)

		#Put level below score
		self.level_rect=self.level_image.get_rect()
		self.level_rect.right=self.score_rect.right
		self.level_rect.top=self.score_rect.bottom+10

	def prep_planes(self):
		"""Show how many planes are left"""
		self.planes=Group()
		for plane_number in range(self.stats.plane_left):
			plane=Plane(self.ol_settings,self.screen)
			plane.rect.x=10+plane_number*plane.rect.width
			plane.rect.y=10
			self.planes.add(plane)

