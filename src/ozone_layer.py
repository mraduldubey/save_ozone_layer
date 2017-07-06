import pygame
from settings import Settings
from plane import Plane
import game_events as ge
from pygame.sprite import Group
from stats import GameStats
from button import Button
from scorecard import ScoreCard

#Since we create bullet=Group() and alien=Group()
#we remove the imports. -----
#from bullet import Bullet
#from alien import Alien

def start_game():
	#INitialise game
	pygame.init()
	ol_settings = Settings()
	screen = pygame.display.set_mode((ol_settings.screen_width,ol_settings.screen_height))
	pygame.display.set_caption("Save Ozone Layer!")
	#The Play button is made.
	play_button = Button(ol_settings,screen,"Play")
	#Load game stats
	stats = GameStats(ol_settings)
	#Dislpay the score.
	sc=ScoreCard(ol_settings,screen,stats)
	#Making a plane.
	plane = Plane(ol_settings,screen)
	#alien=Alien(ol_settings,screen) --See top@import comment
	#Make a group to store bullets in.
	bullets = Group()
	alien_ships = Group()

	#Create swarm of alien egg ships.
	ge.create_swarm(ol_settings,screen,plane,alien_ships)

	#Start the main loop for the game.
	while True:

		#watch for keyboard and mouse events.
		ge.check_events(ol_settings,screen,plane,bullets,stats,play_button,alien_ships,sc)

		#active_status = False when Play button isnt clicked and when the plane limit of 3 is breached.
		if stats.active_status:
			plane.update()
			ge.update_bullets(ol_settings,screen,plane,alien_ships,bullets,stats,sc)
			ge.update_alien_ships(ol_settings,stats,screen,plane,alien_ships,bullets,sc)
		else:
			if stats.high_score_flag:
			#At this point the stats.high_score holds the new highest score.
			#But, it's not written into the file yet. So, let's do it now.
				stats.pickle_high_score()

		#Doesn't depend on active_status.
		ge.update_screen(ol_settings,screen,plane,bullets,alien_ships,play_button,stats,sc)


start_game()
