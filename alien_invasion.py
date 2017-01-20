import pygame
import sys
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from bullet import Bullet
from earth import Earth

def run_game():
	#INitialise game
	pygame.init()
	ai_settings=Settings()
	screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")
	ship=Ship(ai_settings,screen)
	earth_base=Earth(ai_settings,screen)
	#Make a group to store bullets in.
	bullets=Group()
	#Start the main loop for the game.
	while True:
		#watch for keyboard and mouse events.
		gf.check_events(ai_settings,screen,ship,bullets)
		ship.update()
		gf.update_bullets(bullets)
		gf.update_screen(ai_settings,screen,ship,bullets)

run_game()


