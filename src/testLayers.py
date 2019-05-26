import pygame
import random
import vectorOperations
from artificialNeuron import ArtificialNeuron
from nnLayer import NNLayer
from neuralNet import NeuralNet

def startGame():
	WINDOW_SIZE 	= (1000,800)
	totalNeurons 	= 4

	pygame.init()
	
	gameDisplay 		= initializeGameDisplay(WINDOW_SIZE)
	neuralNetPosition 	= (200,200)
	layersStructure 	= [5,4,3,4]
	neuralNet 			= NeuralNet(neuralNetPosition,layersStructure)

	darkGrey 			= (50,50,50)

	while True:
		gameDisplay.fill(darkGrey)

		neuralNet.draw(gameDisplay)
		pygame.display.update()

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