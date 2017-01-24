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
		#Gravity Settings
		self.gravity_factor=0.2
		#Alien settings
		self.alien_speed_factor = 1
		self.swarm_drop_speed=10
		#fleet_direction of 1 is right; -1 is left
		self.swarm_direction=1


		