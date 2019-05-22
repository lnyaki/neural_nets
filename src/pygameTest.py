import pygame
import random
import copy
import functools
import math

from artificialNeuron import ArtificialNeuron

neurons = None
GRAVITY = 10

def startGame():
	pygame.init()

	gameDisplay 	= initializeGameDisplay()
	pixelArray 		= pygame.PixelArray(gameDisplay)
	totalNeurons 	= 5
	neurons 		= generateNeurons(totalNeurons)

	drawNeurons(gameDisplay, neurons)

	i = 0
	while True:
		

		if i >= 10000 : continue

		i += 1
		print("*************************************************")
		gameDisplay.fill((0,0,0))
		manageGameEvents(pygame)

		setNeuronMovements(neurons)
		print("---------------- Neuron Movements calculated")
		applyNeuronMovements(neurons)
		print("---------------- Neuron Movements applied")
		drawNeurons(gameDisplay, neurons)

		pygame.display.update()
		print("-- --")


def setNeuronMovements(neurons):

	for neuron in neurons:
		setSingleNeuronMovement(neuron,neurons)


def setSingleNeuronMovement(neuron, neuronList):
	gravityVectors 		= computeGravityVectors(neuron, neuronList)
	finalGravityVector	= addVectorList(gravityVectors)

	movementAngle 		= getVectorAngle(finalGravityVector)
	distanceScalar		= getScalarDistance(finalGravityVector)
	'''multiplier = 10/distanceScalar
	movementVector = scalarVectorMultiplication(finalGravityVector, multiplier)

	print(" *** Distance scalar : "+str(distanceScalar))
	print(" *** MOVEMENT : "+ str(movementVector))
	'''

	movementDistance = 1

	if movementDistance <  distanceScalar :
		movementVector = getMovementVector(movementAngle,finalGravityVector,movementDistance)
		neuron.setFutureMove(movementVector)


def applyNeuronMovements(neurons):
	print("------- Apply neuron movements, inside")
	print("------- List of neurons to move")
	print(neurons)

	for neuron in neurons:
		print("loop "+str(neuron.id))
		if not isNeuronCollision(neuron,neurons):
			neuron.applyMove()
			print("---- Apply move ---")

		else :
			print("collision!")
			pass

	print("applyNeuronMovments : end of loop")


def isNeuronCollision(originalNeuron,neuronList):
	collision 	= False
	exit 		= False
	i 			= 0
	total 		= len(neuronList)

	while not exit:

		neuron = neuronList[i]

		print("length : "+str(total)+" i :"+str(i)+" neuron.id : "+str(neuron.id))

		collisionWithOtherNeuron = (neuron.id != originalNeuron.id) and  originalNeuron.collision(neuron)
		
		if collisionWithOtherNeuron :
			collision 	= True
			exit 		= True

		i += 1
		
		print("---	i : "+str(i)+" 	total : "+str(total))
		if i >= total :
			exit = True

	print("End of neuron collision")
	return collision

def getMovementVector(angle, vector, distance):
	return (math.cos(angle)*distance,math.sin(angle)*distance)

def getVectorAngle(vector):
	return math.atan2(vector[1],vector[0])

def computeGravityVectors(originalNeuron, neuronList):
	allGravityVectors = []

	for neuron in neuronList:
		if originalNeuron.id == neuron.id : continue

		gravityVector = computeSingleGravityVector(originalNeuron,neuron)
		allGravityVectors.append(gravityVector)

	return allGravityVectors

def computeSingleGravityVector(neuron1,neuron2):
	distanceVector 	= getDistanceVector(neuron1,neuron2)
	distanceScalar	= getScalarDistance(distanceVector)
	angle 			= math.atan2(distanceVector[0], distanceVector[1])
	print("Distance vector between neurons : "+str(distanceVector))
	#return 1+ getGravityScalar(distanceScalar,neuron1.mass, neuron2.mass)
	return distanceVector

def scalarVectorMultiplication(vector, multiplier):
	return (vector[0] * multiplier,vector[1] * multiplier)

def getGravityScalar(distance, mass1, mass2):
	return (GRAVITY * mass1 * mass2)/ (distance ** 2)

def getScalarDistance(vector):
	return math.sqrt((vector[0] ** 2) + (vector[1] ** 2))

def getDistanceVector(neuron1, neuron2):
	print("Neuron 1 : "+str(neuron1.position))
	print("Neuron 2 : "+str(neuron2.position))
	return (neuron2.position[0] - neuron1.position[0], neuron2.position[1] - neuron1.position[1])

def addVectorList(vectorList):
	print("Vector List")
	print(vectorList)
	return functools.reduce(addVectors, vectorList)

def addVectors(vector1, vector2):
	print(vector1)
	print(vector2)
	return (vector1[0] + vector2[0], vector1[1] + vector2[1])

def generateNeurons(totalNeurons):
	neuronList = []
	neuronID = 0
	for i in range(totalNeurons):
		neuronID += 1
		coordinates = (random.randint(0,600),random.randint(0,600))
		neuronList.append(ArtificialNeuron(coordinates, neuronID))

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