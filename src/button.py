import pygame
from interactiveElement import InteractiveElement

class Button(InteractiveElement):

	def __init__(self,text, dimension,position=(0,0)):
		super().__init__(position)
		self.text 		= text
		self.dimension 	= dimension
		self.rectangle 	= pygame.Rect(self.position[0], self.position[1],self.dimension[0],self.dimension[1])
		self.container 	= None
		self.relativePosition = (0,0)

	def checkCollision(self,position):
		return self.rectangle.collidepoint(position[0],position[1])

	def collision(self):
		pass

	def hover(self):
		pass

	def setContainer(self,container):
		super().setContainer(container)
	
	def setPosition(self, position):
		super().setPosition(position)
		self.rectangle = pygame.Rect(self.container.position[0]+position[0],self.container.position[1]+position[1],self.dimension[0],self.dimension[1])

	def draw(self, gameDisplay):
		pygame.draw.rect(gameDisplay,(255,0,0),self.rectangle)
		pygame.gfxdraw.rectangle(gameDisplay,self.rectangle,(255,255,255))

