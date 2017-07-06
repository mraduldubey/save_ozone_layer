import os, os.path
import pickle

class GameStats(object):
	"""Save the stats for our game"""
	def __init__(self, ol_settings):
		self.ol_settings = ol_settings
		self.reset_stats()
		#Start gamein inactive mode
  		self.active_status =False
  		#High score should never resetted.
  		self.high_score = self.get_high_score()
		#This is set if new high score has been set.
		self.high_score_flag = False

	def reset_stats(self):
		"""Initialise stas that change during the game"""
	 	self.plane_left = self.ol_settings.plane_limit
	 	self.ol_settings.initialize_dynamic_settings()
	 	self.score=0
	 	self.level=1

	def get_high_score(self):
		'''Return the highest score from pickle file'''
		if os.path.isfile('bigscore.pkl'):
			with open('bigscore.pkl','rb') as f:
				return pickle.load(f)
		else:
			return 0

	def set_high_score(self,new_high_score):
		'''Set the high_score_flag and update the high score'''
		self.high_score_flag = True
		self.high_score = new_high_score

	def pickle_high_score(self):
		'''Save the new high score on disk as pickle'''
		with open('bigscore.pkl','wb') as fout:
			pickle.dump(self.high_score,fout)
