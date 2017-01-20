import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group

#Since we create bullet=Group() and alien=Group()
#we remove the imports. ----- Why?@mD
#from bullet import Bullet
#from alien import Alien

def run_game():
	#INitialise game
	pygame.init()
	ai_settings=Settings()
	screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")
	#Make a ship, group of bullets, group of aliens.
	ship=Ship(ai_settings,screen)
	#alien=Alien(ai_settings,screen) --See top@import comment
	#Make a group to store bullets in.
	bullets=Group()
	aliens=Group()

	#Create fleet of aliens.
	gf.create_fleet(ai_settings,screen,aliens)
	#Start the main loop for the game.
	while True:
		#watch for keyboard and mouse events.
		gf.check_events(ai_settings,screen,ship,bullets)
		ship.update()
		gf.update_bullets(bullets)
		gf.update_screen(ai_settings,screen,ship,bullets,aliens)

run_game()


