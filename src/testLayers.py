import pygame
import random
import sys
import vectorOperations
from artificialNeuron import ArtificialNeuron
from nnLayer import NNLayer
from neuralNet import NeuralNet

INTERACTIONS = {
	"hoverableElements" : [],
	"hoveredElements" : [],
	"clickableElements" : [],
	"clickedElements" : []
}

def startGame():
	WINDOW_SIZE 	= (1000,800)
	totalNeurons 	= 4

	pygame.init()
	
	gameDisplay 		= initializeGameDisplay(WINDOW_SIZE)
	neuralNetPosition 	= (200,100)
	layersStructure 	= [5,2,4,8]
	neuralNet 			= NeuralNet(neuralNetPosition,layersStructure,NeuralNet.FULLMESH)

	darkGrey 			= (50,50,50)

	while True:
		drawBackground(gameDisplay, darkGrey)
		handleEvents()
		neuralNet.draw(gameDisplay)
		pygame.display.update()


def drawBackground(gameDisplay,color):
	gameDisplay.fill(color)

def handleEvents():

	for event in pygame.event.get():
		if(isKeyboardEvent(event)):
			handleKeyboardEvents(event)

		elif(isMouseEvent(event)):
			handleMouseEvents(event)


		elif(event.type == pygame.QUIT):
			pygame.quit()
			sys.exit()

def isKeyboardEvent(event):
	return event.type in [pygame.KEYDOWN]

def isMouseEvent(event):
	return event.type in [pygame.MOUSEBUTTONUP,pygame.MOUSEBUTTONDOWN,pygame.MOUSEMOTION]

def handleKeyboardEvents(event):
	pass

def handleMouseEvents(event):
	
	if(event.type == pygame.MOUSEMOTION):
		hoveredElement = getHoveredElement(pygame.mouse.get_pos,INTERACTIONS["hoverableElements"])

		if(hoveredElement):
			hoveredElement.hover()

def getHoveredElement(mousePosition, hoverable_elements):
	hoveredElements = []

	for hoverable in hoverable_elements:
		if(hoverable.collision(mousePosition)):
			hoveredElements.append(hoverable)

	return hoveredElements

def drawNeuralNet(layers, gameDisplay):
	for layer in layers:
		layer.draw(gameDisplay)

def initializeGameDisplay(WINDOW_SIZE):
	black = (0,0,0)
	gameDisplay = pygame.display.set_mode(WINDOW_SIZE)
	gameDisplay.fill(black)

	return gameDisplay


if __name__ == "__main__":
	startGame()