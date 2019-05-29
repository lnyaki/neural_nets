import pygame
import colors
from interactiveElement import InteractiveElement

class Button(InteractiveElement):

	pygame.init()
	font = pygame.font.Font('freesansbold.ttf',20)

	def __init__(self,text, dimension,position=(0,0)):
		super().__init__(position)
		self.borderColor = colors.WHITE
		self.textColor 	= colors.WHITE
		self.backgroundColor = colors.RED
		self.textValue 	= text
		self.textObject = self.getTextObject(text,self.font)
		self.dimension 	= dimension
		self.rectangle 	= pygame.Rect(self.position[0], self.position[1],self.dimension[0],self.dimension[1])
		self.container 	= None
		self.relativePosition = (0,0)
		

	def checkCollision(self,position):
		return self.rectangle.collidepoint(position[0],position[1])

	def collision(self):
		pass

	def hover(self):
		print("Test hover : "+self.textValue)
		self.setTextColor(colors.BLACK)
		self.setBackground(colors.GREEN)

	def unHover(self):
		print("Quitting : "+self.textValue)
		self.setTextColor(colors.WHITE)
		self.setBackground(colors.RED)

	def setContainer(self,container):
		super().setContainer(container)
	
	def setPosition(self, position):
		super().setPosition(position)
		print("Set position :"+str(position))
		print(str(self.rectangle))
		self.rectangle = pygame.Rect(self.container.position[0]+position[0],self.container.position[1]+position[1],self.dimension[0],self.dimension[1])

	def setTextColor(self, color):
		self.textColor 	= color
		self.textObject = self.getTextObject(self.textValue,self.font)

	def setBackground(self,color):
		self.backgroundColor = color

	def getTextObject(self,text,font):
		textSurface = font.render(text,True,self.textColor)
		return textSurface

	def draw(self, gameDisplay):
		pygame.draw.rect(gameDisplay,self.backgroundColor,self.rectangle)
		pygame.gfxdraw.rectangle(gameDisplay,self.rectangle,self.borderColor)
		gameDisplay.blit(self.textObject, self.textObject.get_rect(center=self.rectangle.center))


