import pygame
import random
import copy
from artificialNeuron import ArtificialNeuron

neurons = None

def startGame():
	pygame.init()

	gameDisplay 	= initializeGameDisplay()
	pixelArray 		= pygame.PixelArray(gameDisplay)
	totalNeurons 	= 10
	neurons 		= generateNeurons(totalNeurons)

	drawNeurons(gameDisplay, neurons)

	
	while True:
		manageGameEvents(pygame)

		repelNeurons(neurons)
		drawNeurons(gameDisplay, neurons)

		pygame.display.update()


def repelNeurons(neurons):

	for neuron in neurons:
		neuronsToTest = copy.copy(neurons)

		repelSingleNeuron(neuron,neuronsToTest)

def repelSingleNeuron(neuron, neuronList):

	nearbyNeurons = selectNearbyNeurons(neuron,neuronList)

	repositionBasedOnNearbyNeurons(neuron, nearbyNeurons)

def selectNearbyNeurons(neuron, neuronList):
	pass

def repositionBasedOnNearbyNeurons(neuron,nearbyNeurons):
	pass

def generateNeurons(totalNeurons):
	neuronList = []
	
	for i in range(totalNeurons):
		coordinates = (random.randint(0,600),random.randint(0,600))
		neuronList.append(ArtificialNeuron(coordinates))

	return neuronList

def drawNeurons(gameDisplay, neurons):
	for neuron in neurons:
		neuron.draw(gameDisplay)


def drawShapes(gameDisplay):
	white 	= (255,255, 255)
	blue	= (0,0,255)
	green 	= (0,255,0)
	red		= (255,0,0)

	pygame.draw.line(gameDisplay,blue, (100,200), (400,500),10)
	pygame.draw.rect(gameDisplay,red,(400,400,50, 25))
	pygame.draw.circle(gameDisplay,blue,(150,150),75)
	pygame.draw.circle(gameDisplay,white,(150,150),75,10)

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