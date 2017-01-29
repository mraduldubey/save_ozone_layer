import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep


def check_keydown_events(event,ol_settings,screen,plane,bullets): 
	"""Responds to keypresses"""	
	if event.key==pygame.K_RIGHT:
		plane.moving_right=True
	elif event.key ==pygame.K_LEFT:
		plane.moving_left=True
	elif event.key==pygame.K_UP:
		plane.moving_up=True
	elif event.key==pygame.K_DOWN:
		plane.moving_down=True
	elif event.key==pygame.K_SPACE:
		fire_bullet(ol_settings,screen,plane,bullets)

def check_keyup_events(event,ol_settings,screen,plane,bullets):
	"""Respond to key releases"""
	if event.key==pygame.K_RIGHT:
		plane.moving_right=False
	elif event.key==pygame.K_LEFT:
		plane.moving_left=False
	elif event.key==pygame.K_UP:
		plane.moving_up=False
	elif event.key==pygame.K_DOWN:
		plane.moving_down=False

def check_events(ol_settings,screen,plane,bullets,stats,play_button,aliens,sc):
	"""Respond to keypresses and mouse events"""
	for event in pygame.event.get():
			if event.type==pygame.QUIT:
				sys.exit()
			elif event.type==pygame.KEYDOWN:
				check_keydown_events(event,ol_settings,screen,plane,bullets)
			elif event.type==pygame.KEYUP:
				check_keyup_events(event,ol_settings,screen,plane,bullets)
			elif event.type==pygame.MOUSEBUTTONDOWN:
				mouse_x,mouse_y=pygame.mouse.get_pos()
				check_play_button(ol_settings,screen,stats,play_button,plane,aliens,bullets,mouse_x,mouse_y,sc)


def update_screen(ol_settings,screen,plane,bullets,aliens,play_button,stats,sb):
	"""Update images on the screen and flip to the new screen"""
	#Redraw whole window again
	screen.fill(ol_settings.bg_color)
	#Redraw all bullets 
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	#Redraw plane
	plane.blitme()
	#draw() on a group, draws all the elments of the group.
	aliens.draw(screen)  
	#Draw score information.
	sb.show_score()
	#Draw the play button if the   game is inactive.
	if not stats.active_status:
		play_button.draw_button()
	#Making most recently drawn screen visible i.e. fipping to new screen.
	pygame.display.flip()

def update_bullets(ol_settings,screen,plane,aliens,bullets,stats,sc):
	"""Update positions of bullets and get rid of old ones"""
	#Check for any bullets that have hit aliens.
	#If yes then get rid    of the bulet and alien_ship.
	collisions=pygame.sprite.groupcollide(bullets,aliens,True,True)
	#Update bullet positions i.e. move them upwards continously.
	bullets.update()
	#Get rid of bullets that have disappeared.
	for bullet in bullets.copy():
		if bullet.rect.bottom<=0:
			bullets.remove(bullet)
	#print len(bullets)
	check_bullet_alien_collisions(ol_settings,screen,plane,aliens,bullets,stats,sc)

def check_bullet_alien_collisions(ol_settings,screen,plane,aliens,bullets,stats,sc):
	"""Check bullet alien collision"""
	collisions=pygame.sprite.groupcollide(bullets,aliens,True,True)
	if collisions:
		for alien_ships in collisions.values():
			stats.score+=ol_settings.alien_points *len(alien_ships)
			sc.prep_score()
		check_high_score(stats,sc)
	if len(aliens) == 0:
		#Destroy bullets and create new fleet
		bullets.empty()
		#Speedup the game and level up.
		ol_settings.game_speedup()
		#Increase level
		stats.level+=1
		sc.prep_level()
		create_swarm(ol_settings,screen,plane,aliens)

def fire_bullet(ol_settings,screen,plane,bullets):
	"""Fire a bullet if limit not reached yet"""
	#Crete a new bullet and add it bullets group
	if len(bullets)<ol_settings.bullets_allowed:
		new_bullet=Bullet(ol_settings,screen,plane)
		bullets.add(new_bullet) #Add bullet to the bullet group

def get_number_aliens_x(ol_settings,alien_width):
	"""Determine the number of aliens in a row"""
	#Leaving margins on both sides
	available_space_x = ol_settings.screen_width - 2*alien_width
	#Finding no of aliens that have apt spacing b/w them.
	number_aliens_x = int(available_space_x / (2*alien_width))
	return number_aliens_x

def create_alien(ol_settings,screen,aliens,alien_number,row_number):
	"""Create an alien and place it on screen"""
	#Create an alien. Add it to row.
	alien = Alien(ol_settings,screen)
	alien_width = alien.rect.width
	alien.x = alien_width + 2 * alien_width * alien_number
	alien.rect.x = alien.x
	alien.rect.y = alien.rect.height + 2*alien.rect.height* row_number
	#aliens the group, not alien the object.
	aliens.add(alien)

def create_swarm(ol_settings,screen,plane,aliens):
	"""Create a full swarm of aliens"""
	#This alien is for alien.rect access when get_number_aliens_x is called
	alien = Alien(ol_settings,screen)
	number_aliens_x=get_number_aliens_x(ol_settings,alien.rect.width)
	number_rows= get_number_rows(ol_settings,plane.rect.height,alien.rect.height)
	#Create the swarm of aliens
	for row_number in range(number_rows):
		for alien_number in range(number_aliens_x):
			create_alien(ol_settings,screen,aliens,alien_number,row_number)

def get_number_rows(ol_settings,ship_height,alien_height):
	"""Determine the number ofs rows of aliens that fir on the screen."""
	available_space_y= (ol_settings.screen_height - (3 * alien_height)- ship_height)
	number_rows = int(available_space_y / (2*alien_height)) -1
	#print number_rows
	return number_rows

def update_alien_ships(ol_settings,stats,screen,plane,aliens,bullets,sc):
	"""Update the positions of all aliens in the swarm and check collisions"""
	#Check first whether swarm is at edge.
	check_swarm_edges(ol_settings,aliens)
	aliens.update()

	#Check alien and plane collision
	if pygame.sprite.spritecollideany(plane,aliens):
		plane_hit(ol_settings,stats,screen,plane,aliens,bullets,sc)
	#Check for aliens passed through the ozone hole.
	check_aliens_bottom(ol_settings,stats,screen,plane,aliens,bullets,sc)

def check_swarm_edges(ol_settings,aliens):
	"""If aliens at edge, change direction"""
	for alien in aliens.sprites():
		if alien.check_edges():
			change_swarm_direction(ol_settings,aliens)
			break

def change_swarm_direction(ol_settings,aliens):
	"""Drop swarm and change direction"""
	for alien in aliens.sprites():
		alien.rect.y+=ol_settings.swarm_drop_speed
	ol_settings.swarm_direction*=-1 

def plane_hit(ol_settings,stats,screen,plane,aliens,bullets,sc):
	"""Respond to ship being hit"""
	if stats.plane_left > 0:	
		stats.plane_left-=1
		#Update Scorecard.
		sc.prep_planes()
		#Empty list of aliens and bullets
		aliens.empty()
		bullets.empty()
		#Create new swarm and posiiton the plane.
		create_swarm(ol_settings,screen,plane,aliens)
		plane.center_plane()
		#Pause
		sleep(0.5)
	else:
		stats.active_status = False
		pygame.mouse.set_visible(True)

def check_aliens_bottom(ol_settings,stats,screen,plane,aliens,bullets,sc):
	"""Check if any aliens have reached the bottom of the screen"""
	screen_rect = screen.get_rect()
	for alien in aliens.sprites():
		if alien.rect.bottom >= screen_rect.bottom:
			#Just as when the plane got hit
			plane_hit(ol_settings,stats,screen,plane,aliens,bullets,sc)
			break

def check_play_button(ol_settings,screen,stats,play_button,plane,aliens,bullets,mouse_x,mouse_y,sc):
	"""Start  new game when the player clicks Play"""
	#collidepoint test whether a point is inside a rect
	button_clicked=play_button.rect.collidepoint(mouse_x,mouse_y)
	#print "button clicked"
	if button_clicked and not stats.active_status:
		#Reset the game only when it is paused and mouse is clicked on button.
		stats.reset_stats()
		stats.active_status = True
		#Reset the scorebard images.
		sc.prep_score()
		sc.prep_high_score()
		sc.prep_level()
		sc.prep_planes()
		#print "BULL"
		#Hide mouse cursor.
		pygame.mouse.set_visible(False)
		#Remove the list of aliens and bullets.
		aliens.empty()
		bullets.empty()
		#Create a new fleet and center the ship.
		create_swarm(ol_settings,screen,plane,aliens)
		plane.center_plane()

def check_high_score(stats,sc):
	"""Check to see if there's a new high score"""
	if stats.score>stats.high_score:
		stats.high_score=stats.score
		sc.prep_high_score()