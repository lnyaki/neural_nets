import pygame
import pygame.gfxdraw
import vectorOperations

class ArtificialNeuron:
	MINIMAL_MOVEMENT = (0.01,0.01)
	numberOfDecimals = 4

	position 			= None
	previousPosition 	= None
	previousMovement 	= (0,0)

	activationCharge 	= 0
	defaultDrawSize 	= 30

	layerID = 0

	conditions = {
		"reproductionEnergy" : 60
	}

	actions = {
		"reproduction" : {
			"conditions" : {
				"energy": 60,
				"actionPoint": 3
			}
		},
		"fire" : {
			"conditions" : {
				"activationCharge": 50
			},
			"output" : {
				"activationCharge" : 0
			}
		}
	}

	def __init__(self, position, id, layerID = 0):
		self.position 	= position
		self.id 		= id
		self.futureMove = (0,0)
		self.layerID = layerID

	def applyMove(self):
		print("Position : "+str(self.position)+ "	Move by VECTOR "+str(self.futureMove))

		#if(self.minimalMovementAchieved(self.futureMove) and vectorOperations.vectorBiggerThan(self.futureMove,(1,1))):
		if(self.minimalMovementAchieved(self.futureMove)):

			roundingDecimals = 2
			
			if not vectorOperations.isOppositeVector(self.previousMovement,self.futureMove, roundingDecimals):
				print("Not opposite "+str(self.previousMovement)+" "+str(self.futureMove))

				newPosition 	= vectorOperations.roundVector(self.addVector(self.futureMove),self.numberOfDecimals)
				self.position 	= newPosition
				
			else :
				print("Opposite movements vectors. Half movement "+str(self.position)+" "+str(self.previousMovement)+" "+str(self.futureMove))
				halfMovement 	= vectorOperations.divideVectorBy(self.futureMove,2)
				print("Half Movement : "+str(halfMovement))
				self.position 	= vectorOperations.roundVector(self.addVector(halfMovement),self.numberOfDecimals)

			print("new position "+str(self.position))

		else : print("No movement : "+str(self.futureMove))

		self.previousMovement 	= self.futureMove
		self.futureMove 		= (0,0)


	def minimalMovementAchieved(self, movementVector):
		return vectorOperations.vectorBiggerThan(movementVector, self.MINIMAL_MOVEMENT)

	def setFutureMove(self,vector):
		numberOfDecimals 	= 4
		self.futureMove 	= vectorOperations.roundVector(vector, numberOfDecimals)

	def addVector(self,vector):
		return (self.position[0] + vector[0], self.position[1] + vector[1])

	def getDistanceVector(self,neuron):
		print("Neuron 1 : "+str(neuron1.position))
		print("Neuron 2 : "+str(neuron2.position))
		return (neuron.position[0] - self.position[0], neuron.position[1] - self.position[1])

	def collision(self,neuron):
		return False

	def neuronDivision(self):
		return ArtificialNeuron(self.position)

	def draw(self, gameDisplay):
		white 	= (255,255, 255)
		blue	= (0,100,150,200)

		borderThickness = 2
		computedNeuronDrawRadius = self.defaultDrawSize

		self.positionNeuronWithinWindow(gameDisplay, computedNeuronDrawRadius)

		### Round ! int(round(number))
		position = (int(round(self.position[0])),int(round(self.position[1])))
		pygame.draw.circle(gameDisplay,blue,position,computedNeuronDrawRadius)
		#pygame.draw.circle(gameDisplay,white,position,computedNeuronDrawRadius,borderThickness)

		pygame.gfxdraw.aacircle(gameDisplay,position[0],position[1],computedNeuronDrawRadius, white)
		#pygame.gfxdraw.filled_circle(gameDisplay,position[0],position[1],computedNeuronDrawRadius, white)

	def positionNeuronWithinWindow(self, gameDisplay, computedNeuronDrawRadius):
		displayWidth, displayHeight = gameDisplay.get_size()

		positionX, positionY = self.position
		isNeuronOverLeftSideOfWindow 	= (positionX - computedNeuronDrawRadius < 0)
		isNeuronOverRightSideOfWindow 	= (positionX + computedNeuronDrawRadius > displayWidth)
		isNeuronOverTopSideOfWindow 	= (positionY + computedNeuronDrawRadius > displayHeight)
		isNeuronOverBottomSideOfWindow 	= (positionY - computedNeuronDrawRadius < 0)

		if isNeuronOverLeftSideOfWindow:
			self.position = (0 + computedNeuronDrawRadius,self.position[1])

		if isNeuronOverRightSideOfWindow:
			self.position = (displayWidth - computedNeuronDrawRadius, self.position[1])

		if isNeuronOverTopSideOfWindow:
			self.position = (self.position[0], displayHeight - computedNeuronDrawRadius)

		if isNeuronOverBottomSideOfWindow:
			self.position = (self.position[0], 0 + computedNeuronDrawRadius)