import sys
import pygame
from bullet import Bullet

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

def update_screen(ai_settings,screen,ship,bullets,earth_base):
	"""Update images on the screen and flip to the new screen"""
	#Redraw whole window again
	screen.fill(ai_settings.bg_color)
	#Redraw all bullets 
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	#Redraw earth base
	earth_base.blitme()
	#Redraw ship
	ship.blitme()

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