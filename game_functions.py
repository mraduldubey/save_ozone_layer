import sys
import pygame
from bullet import Bullet
from alien import Alien

def check_keydown_events(event,ai_settings,screen,ship,bullets): 
	"""Responds to keypresses"""	
	if event.key==pygame.K_RIGHT:
		ship.moving_right=True
	elif event.key ==pygame.K_LEFT:
		ship.moving_left=True
	elif event.key==pygame.K_UP:
		ship.moving_up=True
	elif event.key==pygame.K_DOWN:
		ship.moving_down=True
	elif event.key==pygame.K_SPACE:
		fire_bullet(ai_settings,screen,ship,bullets)

def check_keyup_events(event,ai_settings,screen,ship,bullets):
	"""Respond to key releases"""
	if event.key==pygame.K_RIGHT:
		ship.moving_right=False
	elif event.key==pygame.K_LEFT:
		ship.moving_left=False
	elif event.key==pygame.K_UP:
		ship.moving_up=False
	elif event.key==pygame.K_DOWN:
		ship.moving_down=False

def check_events(ai_settings,screen,ship,bullets):
	"""Respond to keypresses and mouse events"""
	for event in pygame.event.get():
			if event.type==pygame.QUIT:
				sys.exit()
			elif event.type==pygame.KEYDOWN:
				check_keydown_events(event,ai_settings,screen,ship,bullets)
			elif event.type==pygame.KEYUP:
				check_keyup_events(event,ai_settings,screen,ship,bullets)

def update_screen(ai_settings,screen,ship,bullets,aliens):
	"""Update images on the screen and flip to the new screen"""
	#Redraw whole window again
	screen.fill(ai_settings.bg_color)
	#Redraw all bullets 
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	#Redraw ship
	ship.blitme()
	#draw() on a group, draws all the elments of the group.
	aliens.draw(screen) 
	#Making most recently drawn screen visible
	pygame.display.flip()

def update_bullets(bullets):
	"""Update positions of bullets and get rid of old ones"""
	#Update bullet positions i.e. move them upwards continously.
	bullets.update()
	#Get rid of bullets that have disappeared.
	for bullet in bullets.copy():
		if bullet.rect.bottom<=0:
			bullets.remove(bullet)
	#print len(bullets)

def fire_bullet(ai_settings,screen,ship,bullets):
	"""Fire a bullet if limit not reached yet"""
	#Crete a new bullet and add it bullets group
	if len(bullets)<ai_settings.bullets_allowed:
		new_bullet=Bullet(ai_settings,screen,ship)
		bullets.add(new_bullet) #Add bullet to the bullet group

def get_number_aliens_x(ai_settings,alien_width):
	"""Determine the number of aliens in a row"""
	#Leaving margins on both sides
	available_space_x = ai_settings.screen_width - 2*alien_width
	#Finding no of aliens that have apt spacing b/w them.
	number_aliens_x = int(available_space_x / (2*alien_width))
	return number_aliens_x

def create_alien(ai_settings,screen,aliens,alien_number,row_number):
	"""Create an alien and place it on screen"""
	#Create an alien. Add it to row.
	alien = Alien(ai_settings,screen)
	alien_width = alien.rect.width
	alien.x = alien_width + 2 * alien_width * alien_number
	alien.rect.x = alien.x
	alien.rect.y = alien.rect.height + 2*alien.rect.height* row_number
	#aliens the group, not alien the object.
	aliens.add(alien)

def create_fleet(ai_settings,screen,ship,aliens):
	"""Create a full fleet of aliens"""
	#This alien is for alien.rect access when get_number_aliens_x is called
	alien = Alien(ai_settings,screen)
	number_aliens_x=get_number_aliens_x(ai_settings,alien.rect.width)
	number_rows= get_number_rows(ai_settings,ship.rect.height,alien.rect.height)
	#Create the fleet of aliens
	for row_number in range(number_rows):
		for alien_number in range(number_aliens_x):
			create_alien(ai_settings,screen,aliens,alien_number,row_number)

def get_number_rows(ai_settings,ship_height,alien_height):
	"""Determine the number ofs rows of aliens that fir on the screen."""
	available_space_y= (ai_settings.screen_height - (3 * alien_height)- ship_height)
	number_rows = int(available_space_y / (2*alien_height)) -1
	print number_rows
	return number_rows

