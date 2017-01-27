import sys
import pygame
from bullet import Bullet
from alien import Alien

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

def check_events(ol_settings,screen,plane,bullets):
	"""Respond to keypresses and mouse events"""
	for event in pygame.event.get():
			if event.type==pygame.QUIT:
				sys.exit()
			elif event.type==pygame.KEYDOWN:
				check_keydown_events(event,ol_settings,screen,plane,bullets)
			elif event.type==pygame.KEYUP:
				check_keyup_events(event,ol_settings,screen,plane,bullets)

def update_screen(ol_settings,screen,plane,bullets,aliens):
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
	#Making most recently drawn screen visible
	pygame.display.flip()

def update_bullets(ol_settings,screen,plane,aliens,bullets):
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
	check_bullet_alien_collisions(ol_settings,screen,plane,aliens,bullets)

def check_bullet_alien_collisions(ol_settings,screen,plane,aliens,bullets):
	"""Check bullet alien collision"""
	collisions=pygame.sprite.groupcollide(bullets,aliens,True,True)
	if len(aliens) == 0:
		#Destroy bullets and create new fleet
		bullets.empty()
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

def update_alien_ships(ol_settings,plane,aliens):
	"""Update the positions of all aliens in the swarm"""
	#Check first whether swarm is at edge.
	check_swarm_edges(ol_settings,aliens)
	aliens.update()

	#Check alien and plane collision
	if pygame.sprite.spritecollideany(plane,aliens):
		print "SHIP HIT!!!"

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

