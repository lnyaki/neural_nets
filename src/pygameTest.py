import pygame
import random
import vectorOperations
from artificialNeuron import ArtificialNeuron

neurons = None
GRAVITY = 10

def startGame():
	pygame.init()
	totalNeurons 	= 4
	gameDisplay 	= initializeGameDisplay()
	pixelArray 		= pygame.PixelArray(gameDisplay)
	
	'''
	neurons 		= testGenerateNeurons2(totalNeurons)

	drawNeurons(gameDisplay, neurons)
	'''

	layerPosition = (100,100)
	layer = nnLayer(layerPosition,totalNeurons)
	neuralNet = None

	i = 0

	while True:
		
		if i >= 30000 : continue

		i += 1

		print("*************************************************")
		gameDisplay.fill((0,0,0))

		manageGameEvents(pygame)
'''
		setNeuronMovements(neurons)
		print("---------------- Neuron Movements calculated")
		applyNeuronMovements(neurons)
		print("---------------- Neuron Movements applied")
		drawNeurons(gameDisplay, neurons)
'''

		pygame.display.update()
		print("-- --")

def testGenerateNeurons(whatever):
	neurons = []

	neurons.append(ArtificialNeuron( (400,200) ,1))
	neurons.append(ArtificialNeuron( (400,400) ,2))
	neurons.append(ArtificialNeuron( (400,100) ,3))
	neurons.append(ArtificialNeuron( (100,200) ,4))

	return neurons

def testGenerateNeurons2(whatever):
	neurons = []

	neurons.append(ArtificialNeuron( (410,501) ,1))
	neurons.append(ArtificialNeuron( (400,440) ,2))
	neurons.append(ArtificialNeuron( (450,107) ,3))
	neurons.append(ArtificialNeuron( (104,218) ,4))
	return neurons

def setNeuronMovements(neurons):

	for neuron in neurons:
		setSingleNeuronMovement(neuron,neurons)


def setSingleNeuronMovement(neuron, neuronList):
	gravityVectors 		= vectorOperations.computeGravityVectors(neuron, neuronList)
	finalGravityVector	= vectorOperations.addVectorList(gravityVectors)

	movementAngle 		= vectorOperations.getVectorAngle(finalGravityVector)
	distanceScalar		= vectorOperations.getScalarDistance(finalGravityVector)

	movementDistance = 1

	if movementDistance <  distanceScalar :
		movementVector = vectorOperations.getMovementVector(movementAngle,finalGravityVector,movementDistance)

	else :
		movementVector = finalGravityVector

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

		collisionWithOtherNeuron = (neuron.id != originalNeuron.id) and  originalNeuron.collision(neuron)
		
		if collisionWithOtherNeuron :
			collision 	= True
			exit 		= True

		i += 1

		if i >= total :
			exit = True

	print("End of neuron collision")
	return collision



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