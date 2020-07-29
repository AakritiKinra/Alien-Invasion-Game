import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
	def __init__(self,s_settings,screen):
		super().__init__()
		self.screen=screen
		self.s_settings=s_settings
		self.image=pygame.image.load("ship_pic4.bmp")
		self.rect=self.image.get_rect()
		self.screen_rect=screen.get_rect()

		self.rect.centerx=self.screen_rect.centerx
		self.rect.bottom=self.screen_rect.bottom
		
		self.center=float(self.rect.centerx)
		
		self.moving_right_flag=False
		self.moving_left_flag=False

	def update(self):
		if self.moving_right_flag and self.rect.right< self.screen_rect.right:
			self.center+=self.s_settings.ship_speed_factor
		if self.moving_left_flag and self.rect.left>0:
			self.center-=self.s_settings.ship_speed_factor

		self.rect.centerx=self.center

	def blitme(self):
		self.screen.blit(self.image,self.rect)
	
	def center_ship(self):
		self.center=self.screen_rect.centerx	