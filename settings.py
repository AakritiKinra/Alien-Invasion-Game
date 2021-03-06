class Settings():
	def __init__(self):
		#screen
		self.screen_width=1000
		self.screen_height=600
		self.bg_colour=(255, 255, 255)
		
		#ship
		self.ship_limit=3
		
		#bullet
		self.bullet_width=3
		self.bullet_height=15
		self.bullet_colour=(60,60,60)
		self.bullets_allowed=3

		#fleet
		self.fleet_drop_speed=10
		
		#increase
		self.speedup_scale=1.1
		self.score_scale=1.5
		self.initialize_dynamic_settings()

	def initialize_dynamic_settings(self):
		self.ship_speed_factor=1.5
		self.bullet_speed_factor=3
		self.alien_speed_factor=0.5

		self.fleet_direction=1

		self.alien_points=50

	def increase_speed(self):
		self.ship_speed_factor*=self.speedup_scale
		self.bullet_speed_factor*=self.speedup_scale
		self.alien_speed_factor*=self.speedup_scale

		self.alien_points=int(self.alien_points*self.score_scale)
		