import pygame.font

class Button():
	def __init__(self,ol_settings,screen,msg):
		"""Initialise button attributees"""
		self.screen = screen
		self.screen_rect = screen.get_rect()

		#Set the dimensions and proprties of the button.
		self.width,self.height = 200,50
		self.button_color = (0,0,0)
		self.text_color=(255,255,255)
		self.font = pygame.font.SysFont(None, 48) #None->default font

		#Build the button's rect object.
		self.rect = pygame.Rect(0,0,self.width,self.height)
		self.rect.center = self.screen_rect.center

		#Render the message i.e. msg as a image for the button
		self.prep_msg(msg)

	def prep_msg(self,msg):
		"""The message rendered as a image on button"""
		#True->antialiasing
		self.msg_image = self.font.render(msg,True,self.text_color,self.button_color)
		self.msg_image_rect = self.msg_image.get_rect()
		self.msg_image_rect.center=self.rect.center

	def draw_button(self):
		#Draw blank button and then draw message
		self.screen.fill(self.button_color,self.rect)
		self.screen.blit(self.msg_image,self.msg_image_rect)

