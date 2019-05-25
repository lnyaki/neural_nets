import pygame
import random
import vectorOperations
from artificialNeuron import ArtificialNeuron
from nnLayer import NNLayer
from neuralNet import NeuralNet

def startGame():
	WINDOW_SIZE = (1000,800)
	pygame.init()
	totalNeurons 	= 4
	gameDisplay 	= initializeGameDisplay(WINDOW_SIZE)
	pixelArray 		= pygame.PixelArray(gameDisplay)

	'''
	layerPosition 	= (100,150)
	layerPosition2 	= (300,150)
	layerPosition3 	= (500,150)

	layer 			= NNLayer(layerPosition,totalNeurons)
	layer2 			= NNLayer(layerPosition2,3)
	layer3 			= NNLayer(layerPosition3,2)
	neuralNet 		= [layer,layer2,layer3]
	'''
	neuralNetPosition = (300,250)
	layersStructure = [5,4,3]
	neuralNet = NeuralNet(neuralNetPosition,layersStructure)

	while True:
		gameDisplay.fill((50,50,50))

		#drawNeuralNet(neuralNet,gameDisplay)

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