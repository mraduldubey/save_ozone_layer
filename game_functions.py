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

def create_fleet(ai_settings,screen,aliens):
	"""Create a full fleet of aliens"""
	#Create an alien. Will not be added to group. It's for dimensions.
	alien = Alien(ai_settings,screen)
	alien_width = alien.rect.width
	#Leaving margins on both sides.
	available_space_x = ai_settings.screen_width - 2*alien_width
	#Finding no of aliens that have apt spacing b/w them.
	number_aliens_x = int(available_space_x / (2*alien_width))

	#Create the first row of aliens.
	for alien_number in range(number_aliens_x):
		alien=Alien(ai_settings,screen)
		alien.x = alien_width + 2 * alien_width * alien_number
		alien.rect.x = alien.x
		#aliens the group, not alien the object.
		aliens.add(alien)

