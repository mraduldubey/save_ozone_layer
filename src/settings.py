class Settings():
	"""A class to store all settings for the game"""
	def __init__(self):
		"""Initialising the game's setings."""
		#Screen settings
		self.screen_width=1000
		self.screen_height=800
		self.bg_color=(150,225,218)
		#Plane Settting
		self.plane_limit = 2
		#Bullet Settings
		self.bullet_width=4
		self.bullet_height=15
		self.bullet_color=255,102,0
		self.bullets_allowed=4
		#Gravity Settings
		self.gravity_factor=0.2
		#Alien settings
		self.swarm_drop_speed=10
		#Scale up for he game speed
		self.speedup_scale=1.1
		#Alien point values
		self.score_scale=1.5
		self.initialize_dynamic_settings()

	def initialize_dynamic_settings(self):
		"""Inititalise settings that change throughout the game"""
		self.plane_speed_factor=1.5
		self.bullet_speed_factor=3
		self.alien_speed_factor = 1
		#fleet_direction of 1 is right; -1 is left
		self.swarm_direction=1
		self.alien_points=50

	def game_speedup(self):
		"""Increase speed settings."""
		self.plane_speed_factor*=self.speedup_scale
		self.bullet_speed_factor*=self.speedup_scale
		self.alien_speed_factor*=self.speedup_scale
		#Increase alien point values.
		self.alien_points=int(self.alien_points * self.score_scale)
