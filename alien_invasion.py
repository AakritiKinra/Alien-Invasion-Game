import pygame
from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
import game_functions as gf

def run_game():			# Initialize game and create a screen object.
	pygame.init()
	s_settings=Settings()
	screen = pygame.display.set_mode((s_settings.screen_width, s_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")	
	play_button=Button(s_settings,screen,"Play")
	stats=GameStats(s_settings)
	sb=Scoreboard(s_settings,screen,stats)	
	ship=Ship(s_settings, screen)
	bullets=Group()
	aliens=Group()
	gf.create_fleet(s_settings,screen,ship,aliens)

	while True:			# Start the main loop for the game	
		gf.check_events(s_settings,screen,stats,sb,play_button,ship,aliens,bullets)
		if stats.game_active:
			ship.update()	
			gf.update_bullets(s_settings,screen,stats,sb,ship,aliens,bullets)
			gf.update_aliens(s_settings,screen,stats,sb,ship,aliens,bullets)

		gf.update_screen(s_settings,screen,stats,ship,aliens,sb,bullets,play_button)
				
run_game()