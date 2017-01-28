class GameStats(object):
	"""Save the stats for our game"""
	def __init__(self, ol_settings):
		self.ol_settings = ol_settings
		self.reset_stats()
  		self.active_status =True

	def reset_stats(self):
		"""Initialise stas that change during the game"""
	 	self.plane_left = self.ol_settings.plane_limit
	 