import math
import functools


def getScalarDistance(vector):
	return math.sqrt((vector[0] ** 2) + (vector[1] ** 2))

def getMovementVector(angle, vector, distance):
	return (math.cos(angle)*distance,math.sin(angle)*distance)

def getVectorAngle(vector):
	return math.atan2(vector[1],vector[0])


def scalarVectorMultiplication(vector, multiplier):
	return (vector[0] * multiplier,vector[1] * multiplier)

def getGravityScalar(distance, mass1, mass2):
	return (GRAVITY * mass1 * mass2)/ (distance ** 2)

def getDistanceVector(neuron1, neuron2):
	print("Neuron 1 : "+str(neuron1.position))
	print("Neuron 2 : "+str(neuron2.position))
	return (neuron2.position[0] - neuron1.position[0], neuron2.position[1] - neuron1.position[1])

def addVectorList(vectorList):
	print("Add Vector List")
	print(vectorList)
	
	result = functools.reduce(addVectors, vectorList)
	print("Resulting vector")
	print(result)
	return result

def addVectors(vector1, vector2):
	return (vector1[0] + vector2[0], vector1[1] + vector2[1])


def computeGravityVectors(originalNeuron, neuronList):
	allGravityVectors = []

	for neuron in neuronList:
		if originalNeuron.id == neuron.id : continue

		gravityVector = getVectorDistance(originalNeuron,neuron)
		allGravityVectors.append(gravityVector)

	return allGravityVectors

def getVectorDistance(neuron1,neuron2):
	decimals = 4
	distanceVector 	= getDistanceVector(neuron1,neuron2)
	distanceScalar	= getScalarDistance(distanceVector)
	angle 			= getVectorAngle(distanceVector)
	print("Distance vector between neurons : "+str(distanceVector))
	#return 1+ getGravityScalar(distanceScalar,neuron1.mass, neuron2.mass)
	return roundVector(distanceVector, decimals)

def roundVector(vector, numberOfDecimals):
	return (round(vector[0],numberOfDecimals),round(vector[1], numberOfDecimals))

def vectorBiggerThan(vector1,vector2):
	vector1 = absoluteValueVector(vector1)
	vector2 = absoluteValueVector(vector2)
	return (vector1[0]> vector2[0]) or (vector1[1] > vector2[1])

def absoluteValueVector(vector):
	return (absoluteValue(vector[0]), absoluteValue(vector[1]))
def absoluteValue(number):
	return math.sqrt(number ** 2)

def isOppositeVector(vector1, vector2, rounding = 4):
	return (round(vector1[0],rounding) + round(vector2[0], rounding) == 0) and (round(vector1[1], rounding) + round(vector2[1],rounding) == 0)

def divideVectorBy(vector, divider):
	return (vector[0]/divider, vector[1]/divider)
