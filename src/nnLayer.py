from artificialNeuron import ArtificialNeuron
import vectorOperations

class NNLayer():
	NEURON_SPACING = 10
	layerIndex	= 0
	position 	= None
	neurons		= []
	neuronSize 	= 30


	def __init__(self, startPosition, layerSize, layerIndex):
	
		self.layerIndex	= layerIndex
		self.position 	= startPosition
		self.neurons 	= self.generateNeurons(startPosition,layerSize, self.neuronSize)

	def __str__(self):
		result = "["+str(self.layerIndex)+"]"

		for neuron in self.neurons:
			result = result + "O "

		return result

	def generateNeurons(self,layerStartPosition,layerSize,neuronSize):
		neuronList = []

		neuronPosition 			= layerStartPosition
		neuronPositionIncrement = self.getNeuronSpacingVector()

		for neuronId in range(layerSize):
			neuron = ArtificialNeuron(neuronPosition, neuronId, self.layerIndex, neuronSize)
			neuronList.append(neuron)

			neuronPosition = vectorOperations.addVectors(neuron.position,neuronPositionIncrement)

		return neuronList


	def linkNeuronLayers(self, connectionsPerNeuron):
		pass

	def getNeuron(self,neuronIndex):
		return self.neurons[neuronIndex]

	def getNeuronSpacingVector(self):
		return (0, self.NEURON_SPACING+(2*self.neuronSize))

	def append(self,neuron):
		self.neurons.append(neuron)

	def draw(self,gameDisplay):
		for neuron in self.neurons:
			neuron.draw(gameDisplay)
