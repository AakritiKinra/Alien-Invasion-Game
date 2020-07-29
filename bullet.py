import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	def __init__(self,s_settings,screen,ship):
		super().__init__()	#settings
		self.screen=screen
		self.rect=pygame.Rect(0,0,s_settings.bullet_width,s_settings.bullet_height)
		self.rect.centerx=ship.rect.centerx
		self.rect.top=ship.rect.top
		self.y=float(self.rect.y)
		self.speed_factor=s_settings.bullet_speed_factor
		self.colour=s_settings.bullet_colour

	def update(self):
		self.y -= self.speed_factor
		self.rect.y=self.y

	def draw_bullet(self):
		pygame.draw.rect(self.screen,self.colour,self.rect)
