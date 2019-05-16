import pygame

def startGame():
	pygame.init()

	gameDisplay = initializeGameDisplay()
	pixelArray 	= pygame.PixelArray(gameDisplay)

	drawShapes(pixelArray)
	
	while True:
		manageGameEvents(pygame)	
		pygame.display.update()

		

def drawShapes(pixelArray):
	white 	= (255,255, 255)
	blue	= (0,0,255)
	green 	= (0,255,0)
	red		= (255,0,0)

	pixelArray[10][20] = green

	pygame.draw.line(gameDisplay,blue, (100,200), (400,500),10)
	pygame.draw.rect(gameDisplay,red,(400,400,50, 25))
	pygame.draw.circle(gameDisplay,white,(150,150),75)

def initializeGameDisplay():
	black = (0,0,0)
	gameDisplay = pygame.display.set_mode((800,600))
	gameDisplay.fill(black)

	return gameDisplay

def manageGameEvents(pygame):

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			quit()



if __name__ == "__main__":
	startGame()