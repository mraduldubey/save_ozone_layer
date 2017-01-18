import pygame
import sys
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
	#INitialise game
	pygame.init()
	ai_settings=Settings()
	screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")
	ship=Ship(ai_settings,screen)

	#Start the main loop for the game.
	while True:
		#watch for keyboard and mouse events.
		gf.check_events(ship)
		ship.update()
		gf.update_screen(ai_settings,screen,ship)
run_game()

