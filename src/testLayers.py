import pygame
import random
import sys
import vectorOperations
from artificialNeuron import ArtificialNeuron
from nnLayer import NNLayer
from neuralNet import NeuralNet
from button import Button
from guiContainer import GUIcontainer

INTERACTIONS = {
	"hoverableElements" : [],
	"hoveredElements" : [],
	"clickableElements" : [],
	"clickedElements" : []
}

GUIelements			= []

def startGame():
	WINDOW_SIZE 	= (1000,800)
	totalNeurons 	= 4

	pygame.init()
	
	gameDisplay 		= initializeGameDisplay(WINDOW_SIZE)
	neuralNetPosition 	= (200,100)
	layersStructure 	= [5,2,4,8]
	neuralNet 			= NeuralNet(neuralNetPosition,layersStructure,4)
	
	darkGrey 			= (50,50,50)

	buttonSize = (150,40)
	button = Button("Hello Button",buttonSize)
	button2 = Button("hi", (40,40))
	containerPosition = (50,750)
	container = GUIcontainer(containerPosition,GUIcontainer.HORIZONTAL,20)
	container.add(button)
	container.add(button2)
	GUIelements.append(container)

	while True:
		handleEvents(GUIelements)
		drawBackground(gameDisplay, darkGrey)
		neuralNet.draw(gameDisplay)
		drawUserInterface(gameDisplay, GUIelements)
		pygame.display.update()


def drawBackground(gameDisplay,color):
	gameDisplay.fill(color)

def drawUserInterface(gameDisplay, guiElements):
	for element in guiElements:
		element.draw(gameDisplay)


def handleEvents(guiElements):

	for event in pygame.event.get():
		if(isKeyboardEvent(event)):
			handleKeyboardEvents(event)

		elif(isMouseEvent(event)):
			handleMouseEvents(event,guiElements)


		elif(event.type == pygame.QUIT):
			pygame.quit()
			sys.exit()

def isKeyboardEvent(event):
	return event.type in [pygame.KEYDOWN]

def isMouseEvent(event):
	return event.type in [pygame.MOUSEBUTTONUP,pygame.MOUSEBUTTONDOWN,pygame.MOUSEMOTION]

def handleKeyboardEvents(event):
	pass

def handleMouseEvents(event,guiElements):
	
	if(event.type == pygame.MOUSEMOTION):
		hoveredElements = getHoveredElement(pygame.mouse.get_pos(),guiElements)

		if(hoveredElements):
			for elt in hoveredElements:
				elt.hover()

def getHoveredElement(mousePosition, hoverable_elements):
	hoveredElements = []

	for hoverable in hoverable_elements:
		if(hoverable.checkCollision(mousePosition)):
			hoveredElements.append(hoverable)
			hoverable.hover()

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