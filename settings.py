class Settings():
	"""A class to store all settings for the game"""
	def __init__(self):
		"""Initialising the game's setings."""
		#Screen settings
		self.screen_width=1500
		self.screen_height=1000
		self.bg_color=(150,225,218)
		#Ship Settting
		self.ship_speed_factor=1.5
		#Bullet Settings
		self.bullet_speed_factor=2.5
		self.bullet_width=3
		self.bullet_height=15
		self.bullet_color=60,60,60
		self.bullets_allowed=3

		