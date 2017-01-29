import pygame.font

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

	def prep_score(self):
		"""Render the scoreboard"""
		score_str=str(self.stats.score)
		self.score_image=self.font.render(score_str,True,self.text_color,self.ol_settings.bg_color)
		#Display the scoreboard at top right of the screen
		self.score_rect=self.score_image.get_rect()
		self.score_rect.right=self.screen_rect.right-20
		self.score_rect.top=20

	def show_score(self):
		"""Draw score to the screen"""
		self.screen.blit(self.score_image,self.score_rect)