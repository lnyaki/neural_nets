import pygame

class ArtificialNeuron:

	position 	= None
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

	def __init__(self, position):
		self.position 		= position


	def move(self):
		pass

	def neuronDivision(self):
		return ArtificialNeuron(self.position)

	def draw(self, gameDisplay):
		white 	= (255,255, 255)
		blue	= (0,0,255)

		computedNeuronDrawRadius = self.defaultDrawSize+(int(self.energy/10))

		self.positionNeuronWithinWindow(gameDisplay, computedNeuronDrawRadius)

		pygame.draw.circle(gameDisplay,blue,self.position,computedNeuronDrawRadius)
		pygame.draw.circle(gameDisplay,white,self.position,computedNeuronDrawRadius,5)

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