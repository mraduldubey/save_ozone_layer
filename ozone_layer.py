import pygame
from settings import Settings
from plane import Plane
import game_events as ge
from pygame.sprite import Group
from stats import GameStats

#Since we create bullet=Group() and alien=Group()
#we remove the imports. ----- Why?@mD
#from bullet import Bullet
#from alien import Alien

def start_game():
	#INitialise game
	pygame.init()
	ol_settings=Settings()
	screen=pygame.display.set_mode((ol_settings.screen_width,ol_settings.screen_height))
	pygame.display.set_caption("Ozone Layer")
	#Store game stats
	stats = GameStats(ol_settings)
	#Making a plane.
	plane=Plane(ol_settings,screen)
	#alien=Alien(ol_settings,screen) --See top@import comment
	#Make a group to store bullets in.
	bullets=Group()
	alien_ships=Group()

	#Create swarm of alien eggs.
	ge.create_swarm(ol_settings,screen,plane,alien_ships)
	#Start the main loop for the game.
	while True:
		#watch for keyboard and mouse events.
		ge.check_events(ol_settings,screen,plane,bullets)
		if stats.active_status:
			plane.update()
			ge.update_bullets(ol_settings,screen,plane,alien_ships,bullets)
			ge.update_alien_ships(ol_settings,stats,screen,plane,alien_ships,bullets)
		ge.update_screen(ol_settings,screen,plane,bullets,alien_ships)

start_game()


