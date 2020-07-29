class GameStats():
	def __init__(self, s_settings):
		self.s_settings=s_settings
		self.reset_stats()
		self.game_active=False
		self.high_score=0
		
	def reset_stats(self):
		self.ships_left=self.s_settings.ship_limit
		self.score=0
		self.level=1