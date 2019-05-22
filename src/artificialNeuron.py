import pygame

class ArtificialNeuron:
	position 	= None
	mass 		= 100
	energy		= 40
	actionPoints= 10
	activationCharge = 0
	defaultDrawSize = 30
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

	def __init__(self, position, id):
		self.position 	= position
		self.id 		= id
		self.futureMove = (0,0)

	def applyMove(self):
		print("Position : "+str(self.position)+ "	Move by VECTOR "+str(self.futureMove))
		newPosition 	= self.addVector(self.futureMove)
		self.futureMove = (0,0)
		self.position 	= newPosition
		print("new position "+str(self.position))

	def setFutureMove(self,vector):
		self.futureMove = vector

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
		blue	= (0,0,255)

		computedNeuronDrawRadius = self.defaultDrawSize+(int(self.energy/10))

		self.positionNeuronWithinWindow(gameDisplay, computedNeuronDrawRadius)

		### Round ! int(round(number))
		position = (int(round(self.position[0])),int(round(self.position[1])))
		pygame.draw.circle(gameDisplay,blue,position,computedNeuronDrawRadius)
		pygame.draw.circle(gameDisplay,white,position,computedNeuronDrawRadius,5)

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