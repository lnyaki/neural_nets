import pygame

pygame.init()

white = (255,255, 255)
black = (0,0,0)

gameDisplay = pygame.display.set_mode((800,600))

gameDisplay.fill(black)

pixelArray = pygame.PixelArray(gameDisplay)

while True:
	manageGameEvents()	
	pygame.display.update()
