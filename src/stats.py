class GameStats(object):
	"""Save the stats for our game"""
	def __init__(self, ol_settings):
		self.ol_settings = ol_settings
		self.reset_stats()
		#Start gamein inactive mode
  		self.active_status =False
  		#High score should never resetted.
  		self.high_score=0

	def reset_stats(self):
		"""Initialise stas that change during the game"""
	 	self.plane_left = self.ol_settings.plane_limit
	 	self.ol_settings.initialize_dynamic_settings()
	 	self.score=0
	 	self.level=1